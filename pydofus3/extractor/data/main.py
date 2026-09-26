import gc
import importlib
import logging
from collections import defaultdict
from compression.zstd import compress
from itertools import chain
from pathlib import Path
from typing import Callable, Generator

import orjson
import UnityPy
from PIL import Image
from tqdm import tqdm
from UnityPy import Environment
from UnityPy.classes import Font, GameObject, Material, Mesh, MonoBehaviour, Shader, Sprite, TextAsset, Texture2D
from UnityPy.enums import ClassIDType
from UnityPy.export.Texture2DConverter import get_image_from_texture2d
from UnityPy.files import ObjectReader, BundleFile
from UnityPy.tools.extractor import crawl_obj

from pydofus3.catalog import ContentCatalogData, load_catalog
from pydofus3.enum_data import TypeData, TypeDataMac, TypeDataOther, adapt_path, get_data_other_path
from pydofus3.extractor.data.config import UnityExtractorOptionConfig
from pydofus3.extractor.data.references import annotate, dependencies, display_name, file_key, object_key, outgoing, read_tree, resolve
from pydofus3.extractor.data.tools import get_monoscript, process_references
from pydofus3.extractor.i18n import read as read_i18n
from pydofus3.not_generated import i18n
from pydofus3.tools import save_img, set_unity_version

logger = logging.getLogger(__name__)


class UnityExtractor:

    def __init__(self, dofus: Path, type_folder: TypeData | str, config: UnityExtractorOptionConfig):
        set_unity_version(dofus)
        self.config = config
        self.type_folder = type_folder

        self.output_path: Path = self.config.output / Path(adapt_path(type_folder))
        self.dofus_path: Path = dofus
        self.dofus_data: Path = dofus / Path(str(type_folder))
        self.files = self.config.files if self.config.files else list(self.dofus_data.iterdir())
        self.env: Environment | None = None
        self.is_build_data = adapt_path(type_folder) == TypeData.Dofus_Data.value
        self.requested: set[str] = {Path(i).name for i in self.files}
        self.paths: dict[str, Path] = {}
        self.index_objects: dict[str, dict] = {}
        self.index_files: dict[str, dict] = {}
        if self.config.process_datacenter and not i18n.i18n_dict:
            i18n_path = get_data_other_path(self.dofus_path, TypeDataOther.I18n)
            if i18n_path and i18n_path.is_dir():
                i18n.i18n_dict.update(read_i18n(i18n_path))  # ty:ignore[no-matching-overload]

        # catalog
        catalog_file = next(chain(self.dofus_data.glob('catalog*.bin'), self.dofus_data.glob('catalog*.json')), None)
        self.catalog: ContentCatalogData|None = load_catalog(catalog_file) if catalog_file else None

        self.EXPORT_TYPES: dict[ClassIDType, Callable[[ObjectReader, Path], set[tuple[str, int]]]] = {
                ClassIDType.GameObject: self.export_game_object,
                ClassIDType.MonoBehaviour: self.export_mono_behaviour,
                ClassIDType.TextAsset: self.export_text_asset,
                ClassIDType.Sprite: self.export_sprite,
                ClassIDType.Texture2D: self.export_texture_2d,
                ClassIDType.Font: self.export_font,
                ClassIDType.Material: self.export_material,
                ClassIDType.Shader: self.export_shader,
                ClassIDType.Mesh: self.export_mesh,
                ClassIDType.Renderer: self.export_mesh_render,
                ClassIDType.MeshRenderer: self.export_mesh_render,
                ClassIDType.SkinnedMeshRenderer: self.export_mesh_render,
                }

    def extract(self):
        if self.config.force_object:
            self.extract_objects()
        else:
            self.extract_container()

    def load_file(self) -> Generator[dict[str, dict[str, list[ObjectReader]]]]:
        monoscript = self.monoscript_paths()
        files = list(map(str, self.files))
        extras = self.build_extras()

        if self.config.load_all_files:
            if monoscript:
                files.extend(monoscript)
            files.extend(i for i in extras if i not in files)
            self.env = env = UnityPy.load(*files)
            yield self.containers(env, self.requested)
            return

        for file in tqdm(files, desc=f'Extract (container) {self.type_folder}'):
            if self.config.force_gc_collect:
                self.force_gc_collect()
            self.env = env = UnityPy.load(str(file))
            if monoscript:
                env.load_files(monoscript)
            if others := [i for i in extras if i != str(file)]:
                env.load_files(others)
            yield self.containers(env, {Path(file).name})

    def build_extras(self) -> list[str]:
        """
        player's own files (globalgamemanagers, resources, sharedassets, level ...)
        """
        if not self.is_build_data:
            return []
        names = ['globalgamemanagers', 'globalgamemanagers.assets', 'resources.assets']
        found = [self.dofus_data / i for i in names]
        found += sorted(self.dofus_data.glob('sharedassets*.assets')) + sorted(self.dofus_data.glob('level[0-9]*'))
        return [str(i) for i in found if i.is_file() and i.suffix != '.resS']

    def containers(self, env: Environment, requested: set[str]) -> dict[str, dict[str, list[ObjectReader]]]:
        result = self.build_container_dict(env)
        if self.is_build_data:
            result.update(self.build_player_containers(env, requested))
        return result

    def monoscript_paths(self) -> list[str] | None:
        if self.config.add_script or self.config.type_tree or self.config.process_datacenter or self.config.dependencies or self.config.index:
            script_bundles = sorted(self.dofus_data.glob('*monoscripts*bundle')) or sorted(self.dofus_data.glob('*/*monoscripts*bundle'))
            if script_bundles:
                return [str(i) for i in script_bundles]
        return None

    def container_entries(self, container: dict[str, dict[str, list[ObjectReader]]]) -> Generator[tuple[str, str, ObjectReader, Path]]:
        """Each object a container exports, and where: ``(container, object name, object, output)``."""
        for container_name, value in container.items():
            use_sub_dir = True if (len(value) > 2 or (len(value) == 2 and '' not in value)) else False
            if use_sub_dir and len(value) == 2 and all(len(objs) == 1 for objs in value.values()) and set(
                    i.type for objs in value.values() for i in objs) == {ClassIDType.Sprite, ClassIDType.Texture2D}:
                value = {k: v for k, v in value.items() if v[0].type == ClassIDType.Texture2D}
                use_sub_dir = False
            for obj_name, objs in value.items():
                if use_sub_dir and obj_name == '':
                    continue
                if len(objs) == 2 and set(i.type for i in objs) == {ClassIDType.Sprite, ClassIDType.Texture2D}:
                    obj = next(i for i in objs if i.type == ClassIDType.Texture2D)
                else:
                    obj = objs[0]
                file_output = self.catalog.get_output_path(self.output_path, container_name) if self.catalog else self.output_path /container_name
                if use_sub_dir:
                    file_output /= obj_name
                yield container_name, obj_name, obj, file_output

    def extract_container(self):
        for container in self.load_file():
            exported: set[tuple[str, int]] = set()
            entries = list(self.container_entries(container))
            if self.config.dependencies or self.config.index:
                for _, _, obj, file_output in entries:
                    self.register(obj, file_output)
            planned = self.plan_dependencies(entries) if self.config.dependencies else []
            for container_name, obj_name, obj, file_output in tqdm(entries, desc='container', leave=False):
                if (obj.assets_file.name, obj.path_id) not in exported:
                    file_output.parent.mkdir(parents=True, exist_ok=True)
                    try:
                        exported.update(self.extract_obj(obj, file_output))
                    except Exception:
                        file_name = getattr(getattr(obj.assets_file, 'parent', None), 'name', None)
                        logger.exception(
                            f'file {file_name} output {file_output} container {container_name} obj {obj_name} type {obj.type.name} extraction error'
                            )
            for obj, output in tqdm(planned, desc='dependencies', leave=False):
                if (obj.assets_file.name, obj.path_id) not in exported:
                    output.parent.mkdir(parents=True, exist_ok=True)
                    try:
                        exported.update(self.extract_obj(obj, output))
                    except Exception:
                        logger.exception(f'dependency {object_key(obj)} output {output} type {obj.type.name} extraction error')
            if self.config.index:
                self.index_env()
        if self.catalog:
            self.catalog.save(self.output_path / 'catalog.json')
        if self.config.index:
            self.write_index()

    def plan_dependencies(self, entries: list[tuple[str, str, ObjectReader, Path]]) -> list[tuple[ObjectReader, Path]]:
        """
        for --deps option, what the exported containers reference and is not exported on its own
        """
        planned: list[tuple[ObjectReader, Path]] = []
        used: dict[Path, set[str]] = defaultdict(set)
        for _, _, root, file_output in tqdm(entries, desc='dependencies (plan)', leave=False):
            folder = file_output.parent / f'{file_output.name}.deps'
            try:
                found = dependencies(root)
            except Exception:
                logger.exception(f'dependencies of {object_key(root)} ({file_output})')
                continue
            for group, obj in found:
                if object_key(obj) in self.paths:
                    continue
                if obj.type == ClassIDType.MonoBehaviour and read_tree(obj) is None:
                    logger.debug(f'dependency {object_key(obj)} not readable (no typetree): left out')
                    continue
                directory = folder / group if group else folder
                names = used[directory]
                name = display_name(obj)
                if name.lower() in names:
                    name = f'{name}_{obj.path_id}'
                names.add(name.lower())
                output = directory / name
                self.register(obj, output)
                planned.append((obj, output))
        return planned

    def register(self, obj: ObjectReader, output: Path) -> None:
        """Keep where an object is written"""
        if (path := self.planned_output(obj, output)) is not None:
            self.paths[object_key(obj)] = path

    def planned_output(self, obj: ObjectReader, output: Path) -> Path | None:
        """The file an object's export writes to output"""
        match obj.type:
            case ClassIDType.Texture2D | ClassIDType.Sprite:
                return output if output.suffix in ('.png', '.jpg') else output.with_suffix('.png')
            case ClassIDType.Material:
                return output if output.suffix else output.with_suffix('.json')
            case ClassIDType.Mesh:
                return output if output.suffix else output.with_suffix('.obj')
            case ClassIDType.Font:
                try:
                    data = obj.parse_as_object().m_FontData
                except Exception:
                    logger.debug(f'font {object_key(obj)} not read', exc_info=True)
                    return None
                return output.with_suffix('.otf' if data and data[0:4] == b'OTTO' else '.ttf') if data else None
            case ClassIDType.Shader | ClassIDType.MeshRenderer | ClassIDType.SkinnedMeshRenderer | ClassIDType.Renderer:
                return None
            case ClassIDType.MonoBehaviour if self.config.compress:
                return output.with_name(output.name + '.zst')
            case _:
                return output

    def annotate_references(self, data: dict, obj: ObjectReader) -> None:
        if self.config.dependencies or self.config.index:
            annotate(data, obj.assets_file, self.paths, self.output_path)

    def index_env(self) -> None:
        """Add the objects to the index"""
        if not self.env:
            return
        for obj in tqdm(self.env.objects, desc='index', leave=False):
            file = obj.assets_file
            parent = getattr(file, 'parent', None)
            source = parent.name if type(parent) == BundleFile else file.name
            if Path(str(source)).name not in self.requested:
                continue
            name = file_key(file.name)
            if name not in self.index_files:
                self.index_files[name] = {
                    'source': Path(str(source)).name,
                    'externals': [file_key(i.name) for i in file.externals],
                }
            key = object_key(obj)
            record: dict = {'type': obj.type.name, 'file': name}
            try:
                if object_name := obj.peek_name():
                    record['name'] = object_name
            except Exception:
                logger.debug(f'name of {key} not read', exc_info=True)
            if obj.type == ClassIDType.MonoBehaviour and (script := get_monoscript(obj)):
                record['class'] = script.parse_as_dict().get('m_ClassName')
            if obj.container:
                record['container'] = obj.container
            if (path := self.paths.get(key)) is not None:
                record['path'] = path.relative_to(self.output_path).as_posix() if path.is_relative_to(self.output_path) else path.as_posix()
            if refs := list(dict.fromkeys(ref for _, ref, _ in outgoing(obj))): # keep order
                record['refs'] = refs
            self.index_objects[key] = record

    def write_index(self) -> None:
        path = self.output_path / 'objects.json'
        index = orjson.loads(path.read_bytes()) if path.exists() else {}
        index = {
            'files': {**index.get('files', {}), **self.index_files},
            'objects': {**index.get('objects', {}), **self.index_objects},
        }
        path.parent.mkdir(parents=True, exist_ok=True)
        option = orjson.OPT_INDENT_2 if self.config.indent else None
        path.write_bytes(orjson.dumps(index, option=option))

    def extract_objects(self):
        exported: set[tuple[str, int]] = set()
        # avoid recursive load from folder for Dofus_data (if load with folder it will load all the game)
        file = [str(i) for i in self.files if (i.is_file() or self.type_folder not in [TypeData.Dofus_Data, TypeDataMac.Dofus_Data])]
        if monoscript := self.monoscript_paths():
            file.extend(monoscript)
        self.env = env  = UnityPy.load(*file)

        output_objects = self.output_path / 'objects_type'
        entries: list[tuple[ObjectReader, Path]] = []
        for obj in env.objects:
            try:
                output_dir = output_objects / obj.type.name
                name = str(obj.path_id)
                if hasattr(obj, 'container') and obj.container:
                    name += f'_{obj.container}'.replace('.', '-')
                elif obj_name := obj.peek_name():
                    name += f'_{obj_name}'
                elif obj.type == ClassIDType.MonoBehaviour and (script := get_monoscript(obj)):
                    name += f'_{script.parse_as_dict()["m_ClassName"]}'
                entries.append((obj, output_dir / name.replace('/', '_')))
            except Exception:
                logger.exception(f'file {file} id {obj.path_id} type {obj.type.name} extraction error')
        if self.config.dependencies or self.config.index:
            for obj, output_file in entries:
                self.register(obj, output_file)
        for obj, output_file in tqdm(entries, desc='Bundle process (object)', leave=False):
            try:
                output_file.parent.mkdir(parents=True, exist_ok=True)
                exported.update(self.extract_obj(obj, output_file))
            except Exception:
                logger.exception(f'file {file} id {obj.path_id} type {obj.type.name} extraction error')
        if self.config.index:
            self.index_env()
            self.write_index()

    def extract_obj(self, obj: ObjectReader, output: Path) -> set[tuple[str, int]]:
        export_func = self.EXPORT_TYPES.get(obj.type)
        if export_func:
            return export_func(obj, output)
        else:
            try:
                option = orjson.OPT_INDENT_2 if self.config.indent else None
                data = obj.read_typetree()
                self.annotate_references(data, obj)
                output.write_bytes(orjson.dumps(data, option=option))
                return {(obj.assets_file.name, obj.path_id)}
            except:
                logger.warning(f'{output} {obj.type.name} not handled')
                return set()

    def _need_script(self)-> bool:
        return (self.config.add_script or self.config.type_tree or self.config.process_datacenter
                or self.type_folder in {TypeData.Bones, TypeData.Skins, TypeData.Animations, TypeDataMac.Bones, TypeDataMac.Skins, TypeData.Animations})

    def export_mono_behaviour(self, obj: ObjectReader[MonoBehaviour], output: Path) -> set[tuple[str, int]]:
        data = obj.parse_as_dict()
        extracted = {(obj.assets_file.name, obj.path_id)}
        if self._need_script() and (script := get_monoscript(obj)):
            data['m_Script'] = script.parse_as_dict()
            class_name = data['m_Script'].get('m_ClassName')
            if class_name == 'SkinAsset':
                self.extract_skin(data, obj, output.parent / data['m_Name'])
                return extracted
            elif class_name == 'AnimatedObjectDefinition':
                self.extract_bone(data, obj, output.parent / data['m_Name'])
                return extracted
            elif data['m_Script'].get('m_AssemblyName') == 'Ankama.Dofus.Core.DataCenter' and self.config.process_datacenter:
                data, output = self.extract_datacenter(data, output)
        elif self.config.no_big_int:
            del data['m_Script']
            del data['m_GameObject']
        elif self.config.reference:
            process_references(data)
        if 'm_AtlasTextures' in data and 'm_FaceInfo' in data:
            extracted.update(self.export_font_atlases(obj, data, output))
        self.annotate_references(data, obj)
        json_data = orjson.dumps(data, option=orjson.OPT_NON_STR_KEYS)
        if self.config.compress:
            output = output.with_name(output.name + '.zst')
            json_data = compress(json_data)
        output.write_bytes(json_data)
        if data.get('m_Name') == 'spriteAsset' and 'm_SpriteAtlasTexture' in data:
            self.extract_text_icon(obj, output.parent)
        return extracted

    @staticmethod
    def export_text_asset(obj: ObjectReader[TextAsset], output: Path) -> set[tuple[str, int]]:
        data = obj.read()
        output.write_bytes(data.m_Script.encode('utf-8', 'surrogateescape'))
        return {(obj.assets_file.name, obj.path_id)}

    def export_game_object(self, obj: ObjectReader[GameObject], output: Path) -> set[tuple[str, int]]:
        option = orjson.OPT_INDENT_2 if self.config.indent else None
        data = obj.parse_as_dict()
        self.annotate_references(data, obj)
        output.write_bytes(orjson.dumps(data, option=option))
        exported = {(obj.assets_file.name, obj.path_id)}
        if self.config.dependencies:
            return exported
        for ref_id, ref in crawl_obj(obj).items():
            if ref.type == ClassIDType.GameObject:
                continue
            exported_tuple = (ref.assetsfile.name, ref_id)
            if exported_tuple in exported:
                continue
            try:
                exported.update(self.extract_obj(ref.deref(), output / str(ref.path_id)))
            except Exception:
                logger.exception(f'Failed to export {ref_id}')
        return exported

    def export_sprite(self, obj: ObjectReader[Sprite], output: Path) -> set[tuple[str, int]]:
        data = obj.parse_as_object()
        if self.config.force_texture2d:
            exported = {(data.assets_file.name, data.object_reader.path_id)}
            texture2d = data.m_RD.texture
            exported.update(self.export_texture_2d(texture2d.deref(), output))
            return exported
        else:
            if self.config.sprite_rect_size:
                texture2d_img = data.m_RD.texture.read().image
                rect = data.m_Rect
                y = texture2d_img.height - rect.y
                bbox = (rect.x, y - rect.height, rect.x + rect.width, y)
                img = texture2d_img.crop(bbox)
                save_img(output, img)
            else:
                save_img(output, data.image)
            exported = {
                    (data.assets_file.name, data.object_reader.path_id),
                    (data.m_RD.texture.assetsfile.name, data.m_RD.texture.path_id),
                    }
            alpha_assets_file = getattr(data.m_RD.alphaTexture, 'assetsfile', None)
            alpha_path_id = getattr(data.m_RD.alphaTexture, 'path_id', None)
            if alpha_path_id and alpha_assets_file:
                exported.add((alpha_assets_file.name, alpha_path_id))
            return exported

    @staticmethod
    def export_texture_2d(obj: ObjectReader[Texture2D], output: Path) -> set[tuple[str, int]]:
        data = obj.parse_as_object()
        if not output.suffix:
            output = output.with_suffix('.png')
        if data.m_Width:  # textures can be empty
            save_img(output, data.image)
        return {(data.assets_file.name, data.object_reader.path_id)}

    @staticmethod
    def export_font(obj: ObjectReader[Font], output: Path) -> set[tuple[str, int]]:
        data = obj.parse_as_object()
        if data.m_FontData:
            extension = '.otf' if data.m_FontData[0:4] == b'OTTO' else '.ttf'
            output = output.with_suffix(extension)
            output.write_bytes(bytes(data.m_FontData))
        return {(data.assets_file.name, data.object_reader.path_id)}

    def export_material(self, obj: ObjectReader[Material], output: Path) -> set[tuple[str, int]]:
        def to_dict(entries) -> dict:
            return dict(entries.items() if isinstance(entries, dict) else entries)

        data = obj.read_typetree()
        properties = data.get('m_SavedProperties', {})
        shader_name = None
        if (pptr:=data.get('m_Shader')) and (shader := resolve(obj.assets_file, pptr.get('m_FileID', 0), pptr.get('m_PathID', 0))):
            try:
                parsed = shader.parse_as_object().m_ParsedForm
                shader_name = parsed.m_Name if parsed else None
            except Exception:
                logger.warning(f'{output} shader name not read', exc_info=True)

        data['shaderName'] = shader_name
        data['m_Floats'] = to_dict(properties['m_Floats'])
        data['m_Ints'] = to_dict(properties['m_Ints'])
        data['m_Colors'] = to_dict(properties['m_Colors'])
        data['m_TexEnvs'] = to_dict(properties['m_TexEnvs'])

        self.annotate_references(data, obj)
        if not output.suffix:
            output = output.with_suffix('.json')
        option = orjson.OPT_INDENT_2 if self.config.indent else None
        output.write_bytes(orjson.dumps(data, option=option))
        return {(obj.assets_file.name, obj.path_id)}

    def export_font_atlases(self, obj: ObjectReader[MonoBehaviour], data: dict, output: Path) -> set[tuple[str, int]]:
        exported: set[tuple[str, int]] = set()
        for number, reference in enumerate(data.get('m_AtlasTextures') or []):
            if not isinstance(reference, dict):
                continue
            texture = resolve(obj.assets_file, reference.get('m_FileID', 0), reference.get('m_PathID', 0))
            if texture is None or object_key(texture) in self.paths:
                continue
            path = output.parent / f'{output.name}.atlas{number}.png'
            try:
                exported.update(self.export_texture_2d(texture, path))
                self.paths[object_key(texture)] = path
            except Exception:
                logger.exception(f'{output} atlas {number} not exported')
        return exported

    @staticmethod
    def export_shader(obj: ObjectReader[Shader], output: Path) -> set[tuple[str, int]]:
        data = obj.parse_as_object()
        if data.m_ParsedForm:
            name = data.m_ParsedForm.m_Name
            if name:
                name = name.replace(' ', '_').replace('/', '_')
                output = output.with_stem(f'{output.stem}_{name}')
        if not output.suffix:
            output = output.with_suffix('.txt')
        output.write_text(data.export(), encoding='utf-8', newline='')
        return {(data.assets_file.name, data.object_reader.path_id)}

    @staticmethod
    def export_mesh(obj: ObjectReader[Mesh], output: Path) -> set[tuple[str, int]]:
        data = obj.parse_as_object()
        if not output.suffix:
            output = output.with_suffix('.obj')
        output.write_text(data.export(), encoding='utf-8', newline='')
        return {(data.assets_file.name, data.object_reader.path_id)}

    @staticmethod
    def export_mesh_render(obj: ObjectReader, output: Path) -> set[tuple[str, int]]:
        obj = obj.read()
        if obj.m_GameObject:
            game_object = obj.m_GameObject.read()
            output = output.parent / game_object.m_Name
        else:
            output = output.parent / output.stem
        output.mkdir(exist_ok=True)
        obj.export(str(output))
        return {(obj.assets_file.name, obj.object_reader.path_id)}

    @staticmethod
    def extract_text_icon(obj: ObjectReader, output: Path) -> set[tuple[str, int]]:
        output.mkdir(exist_ok=True, parents=True)
        data = obj.parse_as_object()
        texture = get_image_from_texture2d(data.m_SpriteAtlasTexture.read(), flip=False)
        w, _ = texture.size
        for character, glyph in zip(data.m_SpriteCharacterTable, data.m_SpriteGlyphTable):
            output_file = output / f'{character.m_Name}.png'
            glyph_rect = glyph.m_GlyphRect
            cropped_sprite = texture.crop(
                (
                        glyph_rect.m_X,
                        glyph_rect.m_Y,
                        glyph_rect.m_Width + glyph_rect.m_X,
                        glyph_rect.m_Y + glyph_rect.m_Height,
                        )
                )
            w, h = cropped_sprite.size
            scale = glyph.m_Scale
            (cropped_sprite.resize((int(w * scale), int(scale * h)))
            .transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            .save(output_file))
        return {(data.assets_file.name, data.object_reader.path_id)}

    def extract_bone(self, bone_data: dict, obj: ObjectReader[MonoBehaviour], output: Path):
        output.mkdir(exist_ok=True, parents=True)
        skin = obj.assets_file.files[bone_data['boneAsset']['m_PathID']].parse_as_dict()
        self.extract_skin(skin, obj, output)
        for anim in bone_data['animations']:
            (output / f'{anim["name"]}.dat').write_bytes(bytes(anim['dataBytes']))
            del anim['dataBytes']
        if self.config.no_big_int:
            del bone_data['m_GameObject']
            del bone_data['m_Script']
            del bone_data['boneAsset']
            for i in bone_data['animations']:
                del i['data']
            for i in bone_data['graphics']:
                del i['asset']

        (output / 'bone.json').write_bytes(orjson.dumps(bone_data))

    def extract_skin(self, skin_data: dict, obj: ObjectReader[MonoBehaviour], output: Path):
        output.mkdir(exist_ok=True, parents=True)
        skin_data['textures'] = [t for t in skin_data['textures'] if t['m_PathID'] in obj.assets_file.files]
        for nb, texture_ref in enumerate(skin_data['textures']):
            texture = obj.assets_file.files[texture_ref['m_PathID']].read()
            img = get_image_from_texture2d(texture, False)
            if self.config.skin_png or not self.config.skin_webp:
                save_img(output / f'{nb}.png', img)
            if self.config.skin_webp:
                img.save(output/ f'{nb}.webp')

        if self.config.no_big_int:
            del skin_data['m_GameObject']
            del skin_data['m_Script']
            for i in skin_data['textures']:
                del i['m_PathID']

        (output / 'skin.json').write_bytes(orjson.dumps(skin_data))

    @staticmethod
    def extract_datacenter(data: dict, output: Path) -> tuple[dict, Path]:
        process_references(data)
        script = data.get('m_Script')
        import_path = f'pydofus3.generated.pydantic.{script.get("m_Namespace")}.{script.get("m_ClassName")}'
        try:
            class_ = importlib.import_module(import_path).__getattribute__(script['m_ClassName'])
            obj = class_.model_validate(data).model_dump()
        except Exception as e:
            logger.exception(f'Failed to validate datacenter monobehaviour {output.stem} {e}')
            obj = data
        output = output.with_name(f'{output.stem.lower()}.json')
        return obj, output

    @staticmethod
    def build_container_dict(env: Environment) -> dict[str, dict[str, list[ObjectReader]]]:
        result = defaultdict[str, dict[str, list[ObjectReader]]](lambda: defaultdict(list))
        for obj in env.objects:
            if container_name := obj.container:
                result[container_name][obj.peek_name()].append(obj)
        return result

    def force_gc_collect(self):
        if self.env:
            self.env = None
            gc.collect()

    @staticmethod
    def build_player_containers(env: Environment, names: set[str]) -> dict[str, dict[str, list[ObjectReader]]]:
        wanted = {file_key(name) for name in names}
        result: dict[str, dict[str, list[ObjectReader]]] = defaultdict(lambda: defaultdict(list))
        scenes: list[str] = []
        for obj in env.objects:
            if obj.type == ClassIDType.ResourceManager:
                for name, pptr in obj.read().m_Container:
                    if file_key(pptr.assetsfile.name) in wanted:
                        target = pptr.deref()
                        result[f'Resources/{name}'][target.peek_name()].append(target)
            elif obj.type == ClassIDType.BuildSettings:
                scenes = list(obj.read_typetree().get('scenes', []))
        for index, scene in enumerate(scenes):
            level = f'level{index}'
            if level not in wanted or (cab := env.cabs.get(level)) is None:
                continue
            for obj in cab.objects.values():
                if obj.type != ClassIDType.GameObject:
                    continue
                # check if it is scene root
                data = obj.read()
                first = data.m_Component[0].component if data.m_Component else None
                deref = first.deref() if first else None
                if deref is None or deref.read().m_Father.m_PathID:
                    continue
                container = f'Scenes/{Path(scene).stem}/{display_name(obj)}'
                if container in result:
                    container += f'_{obj.path_id}'
                result[container] = {data.m_Name: [obj]}
        return result
