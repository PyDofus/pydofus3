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
from UnityPy.classes import Font, GameObject, Mesh, MonoBehaviour, Shader, Sprite, TextAsset, Texture2D
from UnityPy.enums import ClassIDType
from UnityPy.export.Texture2DConverter import get_image_from_texture2d
from UnityPy.files import ObjectReader
from UnityPy.tools.extractor import crawl_obj

from pydofus3.catalog import ContentCatalogData, load_catalog
from pydofus3.enum_data import TypeData, TypeDataMac, TypeDataOther, adapt_path, get_data_other_path
from pydofus3.extractor.data.config import UnityExtractorOptionConfig
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

        if self.config.load_all_files:
            if monoscript:
                files.extend(monoscript)
            self.env = env = UnityPy.load(*files)
            yield self.build_container_dict(env)
            return

        for file in tqdm(files, desc=f'Extract (container) {self.type_folder}'):
            if self.config.force_gc_collect:
                self.force_gc_collect()
            self.env = env = UnityPy.load(str(file))
            if monoscript:
                env.load_files(monoscript)
            yield self.build_container_dict(env)

    def monoscript_paths(self) -> list[str] | None:
        if self.config.add_script or self.config.type_tree or self.config.process_datacenter:
            if script_bundles := self.dofus_data.glob('*monoscripts*bundle'):
                return [str(i) for i in script_bundles]
        return None

    def extract_container(self):
        for container in self.load_file():
            exported: set[tuple[str, int]] = set()
            for container_name, value in tqdm(container.items(), desc='container', leave=False):
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
                    if (obj.assets_file.name, obj.path_id) not in exported:
                        file_output = self.catalog.get_output_path(self.output_path, container_name) if self.catalog else self.output_path /container_name
                        if use_sub_dir:
                            file_output /= obj_name
                        file_output.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            exported.update(self.extract_obj(obj, file_output))
                        except Exception:
                            file_name = obj.assets_file.parent.name if hasattr(obj.assets_file, 'parent') else None
                            logger.exception(
                                f'file {file_name} output {file_output} container {container_name} obj {obj_name} type {obj.type.name} extraction error'
                                )
        if self.catalog:
            self.catalog.save(self.output_path / 'catalog.json')

    def extract_objects(self):
        exported: set[tuple[str, int]] = set()
        # avoid recursive load from folder for Dofus_data (if load with folder it will load all the game)
        file = [str(i) for i in self.files if (i.is_file() or self.type_folder not in [TypeData.Dofus_Data, TypeDataMac.Dofus_Data])]
        if monoscript := self.monoscript_paths():
            file.extend(monoscript)
        self.env = env  = UnityPy.load(*file)

        output_objects = self.output_path / 'objects_type'
        for obj in tqdm(env.objects, desc='Bundle process (object)', leave=False):
            try:
                output_dir = output_objects / obj.type.name
                name = str(obj.path_id)
                if hasattr(obj, 'container') and obj.container:
                    name += f'_{obj.container}'.replace('.', '-')
                elif obj_name := obj.peek_name():
                    name += f'_{obj_name}'
                elif obj.type == ClassIDType.MonoBehaviour and (script := get_monoscript(obj)):
                    name += f'_{script.parse_as_dict()["m_ClassName"]}'
                output_file = output_dir / name.replace('/', '_')
                output_file.parent.mkdir(parents=True, exist_ok=True)
                exported.update(self.extract_obj(obj, output_file))
            except Exception:
                logger.exception(f'file {file} id {obj.path_id} type {obj.type.name} extraction error')

    def extract_obj(self, obj: ObjectReader, output: Path) -> set[tuple[str, int]]:
        export_func = self.EXPORT_TYPES.get(obj.type)
        if export_func:
            return export_func(obj, output)
        else:
            try:
                option = orjson.OPT_INDENT_2 if self.config.indent else None
                output.write_bytes(orjson.dumps(obj.read_typetree(), option=option))
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
        output.write_bytes(orjson.dumps(obj.parse_as_dict(), option=option))
        exported = {(obj.assets_file.name, obj.path_id)}
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
