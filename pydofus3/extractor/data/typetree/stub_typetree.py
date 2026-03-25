from collections.abc import Iterable
from dataclasses import dataclass, field
from itertools import chain
from pathlib import Path
from typing import Any, ClassVar, TextIO

import UnityPy
from UnityPy.classes import generated
from UnityPy.enums import ClassIDType
from UnityPy.environment import Environment
from UnityPy.files.SerializedFile import LocalSerializedObjectIdentifier, SerializedType
from UnityPy.helpers.TypeTreeNode import TypeTreeNode
from pydofus3.enum_data import TypeData, TypeDataOther
from tqdm import tqdm

GENERATED_HEADER = """from UnityPy.classes.PPtr import PPtr
from UnityPy.classes.generated import MonoBehaviour
from typing import Union
"""

GENERATED_HEADER_TYPEDDICT = """from __future__ import annotations
from typing import TypedDict, Any, Union

class PPtr(TypedDict):
    m_FileID: int
    m_PathID: int

class MonoBehaviour(TypedDict):
    m_Enabled: int
    m_GameObject: PPtr
    m_Name: str
    m_Script: PPtr
"""

BASE_TYPE_MAP: dict[str, str] = {
        'char': 'str',
        'short': 'int',
        'int': 'int',
        'long long': 'int',
        'unsigned short': 'int',
        'unsigned int': 'int',
        'unsigned long long': 'int',
        'UInt8': 'int',
        'UInt16': 'int',
        'UInt32': 'int',
        'UInt64': 'int',
        'SInt8': 'int',
        'SInt16': 'int',
        'SInt32': 'int',
        'SInt64': 'int',
        'Type*': 'int',
        'FileSize': 'int',
        'float': 'float',
        'double': 'float',
        'bool': 'bool',
        'string': 'str',
        'TypelessData': 'bytes',
        }


interface_mapping = {
        'IClientInteractiveElement': ['ClientInteractiveAnimatedElementTransform', 'ClientInteractiveElementTransform'],
        'Element': ['AnimatedElement', 'GfxElement'],
        'IPostProcessParameters': ['PPBloomParameters', 'PPChromaticAberrationParameters', 'PPFilmGrainParameters'],
        'IShaderParameters': [
                'ShaderBlendingParameters',
                'ShaderColorAnimationParameters',
                'ShaderCustomFramerateParameters',
                'ShaderDepthAlphaClipParameters',
                'ShaderDissolveParameters',
                'ShaderDistortionParameters',
                'ShaderEmissiveParameters',
                'ShaderRefractionAlphaParameters',
                'ShaderRefractionParameters',
                'ShaderRotationParameters',
                'ShaderScaleParameters',
                'ShaderTextureOffsetParameters',
                'ShaderTranslationParameters',
                'ShaderWaveParameters',
                'ShaderWindParameters',
                ],
        'IStagingEffect': [
                'ChangePlaylistStagingEffect',
                'PlayFmodEventStagingEffect',
                'SequenceEventStagingEffect',
                'SetFmodParamStagingEffect',
                'StopLocalizedFmodEventsStagingEffect',
                'ColorAnimationStagingEffect',
                'DissolveStagingEffect',
                'DistortionStagingEffect',
                'EmissiveStagingEffect',
                'NoAnimAlphaStagingEffect',
                'RotationStagingEffect',
                'ScaleStagingEffect',
                'TranslationStagingEffect',
                'ParticleEmissionStagingEffect',
                'ParticleMainStagingEffect',
                'ParticlesPlayStagingEffect',
                'ParticlesStopStagingEffect',
                ],
        'StagingSequence': ['StagingSequence'],
        }

manage_ref_mapping = {
        'shaderOutlineParameters': 'ShaderOutlineParameters',
        'mapWindConfiguration': 'MapWindConfiguration',
        'mapPostProcessConfiguration': 'MapPostProcessConfiguration',
        'mapWaveConfiguration': 'MapWaveConfiguration',
        'mapNoiseModifierConfiguration': 'MapNoiseModifierConfiguration',
        }


def clean_name(name: str) -> str:
    return name.replace('`1', '').replace('/', '_')


@dataclass
class Type:
    default_sub: ClassVar[set[str]] = {'tuple', 'list'}

    name: str
    subTypes: list['Type'] = field(default_factory=list)

    def to_str(self, typed_dict: bool = False) -> str:
        if typed_dict and self.name == 'MetadataDictionaryContainer':
            return f'dict[str, {self.subTypes[0].name}]' if self.subTypes else 'dict[str, Any]'
        if typed_dict and self.subTypes and self.name in ['managedReference', 'managedRefArrayItem']:
            return self.subTypes[0].to_str(typed_dict)
        sub = ', '.join(
            i.to_str(typed_dict) for i in self.subTypes if (not typed_dict or self.name in self.default_sub)
            )
        return f'{self.name}[{sub}]' if sub else self.name

    def __post_init__(self):
        self.name = clean_name(self.name)


@dataclass
class Field:
    reserved_name: ClassVar[list[str]] = []
    name: str
    type: Type

    def write(self, file: TextIO, typed_dict: bool = False):
        file.write(f'    {self.clean_field_name}: {self.type.to_str(typed_dict)}\n')

    @property
    def clean_field_name(self) -> str:
        if self.name in Field.reserved_name:
            return self.name + '_'
        return self.name


@dataclass
class StubClass:
    class_name: str
    base: list[str] = field(default_factory=list)
    attributes: list[Field] = field(default_factory=list)
    generic: bool = False

    def write(self, file: TextIO, typed_dict: bool = False) -> None:
        if typed_dict and len(self.attributes) == 2 and all(i.name in ['m_keys', 'm_values'] for i in self.attributes):
            type_dict = {i.name: i.type.subTypes[0].name for i in self.attributes if len(i.type.subTypes) == 1}
            if len(type_dict) == 2:
                file.write(f'\ntype {self.class_name} = dict[{type_dict["m_keys"]}, {type_dict["m_values"]}]\n')
                return
        default_base = '(TypedDict)' if typed_dict else ''
        base = f'({", ".join(self.base)})' if self.base else default_base
        class_name = f'{self.class_name}[T]' if not typed_dict and self.generic else self.class_name
        file.write(f'\nclass {class_name}{base}:\n')
        if not self.attributes:
            file.write('    pass\n')
        for attr in self.attributes:
            if typed_dict and attr.type.name == 'ManagedReferencesRegistry':
                continue
            attr.write(file, typed_dict)

    def __post_init__(self):
        self.class_name = clean_name(self.class_name)


class StubTypeTree:
    """
    generate python stub and typed dict for typetree
    """

    pattern_aa: ClassVar[str] = 'Standalone*'
    pattern_skin: ClassVar[str] = 'skins_assets_skin_*.bundle'
    pattern_anim: ClassVar[str] = 'props_assets_prop_*.bundle'
    pattern_bone: ClassVar[list[str]] = ['bones_assets_bone_*.bundle', 'bones_assets_boneanim*.bundle',
                                         'bones_assets_boneindex*.bundle']  # fmt: skip

    def __init__(self, game_path: Path, output_path: Path, grouped_file: dict[str, list[Path]] | None = None) -> None:
        self.stubs: dict[str, StubClass] = {}
        self.import_: set[str] = set()
        self.game_path = game_path
        self.game_content_dir = game_path / TypeDataOther.Content
        self.output_path = output_path
        self.env = Environment()
        self.monoscript_env = Environment()
        self.well_known_types: set[str] = set()
        self.interface_mapping: dict[str, list[Type]] = {}
        self.manage_ref_mapping: dict[str, list[Type]] = {}

        d2o = game_path / TypeData.Data
        dlm = game_path / TypeData.Map_Data
        aa = next((game_path / TypeData.aa).glob(self.pattern_aa), None)
        skin = next((game_path / TypeData.Skins).glob(self.pattern_skin), None)
        anim_bundle = next((game_path / TypeData.Animations).glob(self.pattern_anim), None)
        bone = self.glob_list(game_path / TypeData.Bones, self.pattern_bone)

        if grouped_file is not None:
            to_process = []
            if TypeData.Data in grouped_file:
                to_process.append(d2o)
            if TypeData.Map_Data in grouped_file:
                to_process.append(dlm)
            if TypeData.aa in grouped_file:
                to_process.append(aa)
            if TypeData.Skins in grouped_file:
                to_process.append(skin)
            if TypeData.Animations in grouped_file:
                to_process.append(anim_bundle)
            if TypeData.Bones in grouped_file:
                to_process.append(bone)
        else:
            to_process = [d2o, anim_bundle, bone, skin, aa, dlm]

        for i in tqdm(to_process, desc='stub'):
            self.process_path(i)
        (self.output_path / 'typed_dict/__init__.py').touch()

    def process_path(self, input_data: Path | list[Path]) -> None:
        if not self.check_valid_path(input_data):
            return
        self.load_save_type()
        self.stubs = {}
        self.import_ = set()
        files, base_folder = self.get_files(input_data)
        self.monoscript_env = UnityPy.load(str(next(base_folder.glob('*monoscripts*'), None)))
        game_content = self.game_content_dir
        if str(game_content) not in str(base_folder):
            game_content = game_content.parent  # aa
        output_file_name = str(base_folder.relative_to(game_content)).lower().replace('/', '_')
        for file in tqdm(files, desc=f'stub {output_file_name}', leave=False):
            self.env = UnityPy.load(str(file))
            for asset in self.env.assets:
                script_name = [self.get_name_from_local_identifier(i) for i in asset.script_types]
                script_types = {
                        script_name[i.script_type_index]: i for i in asset.types if
                        i.class_id == ClassIDType.MonoBehaviour
                        }
                ref_types = {i.m_ClassName: i for i in asset.get('ref_types', [])}

                self.well_known_types = {'MonoBehaviour', 'EffectInstanceData'}
                self.well_known_types.update(script_types.keys())
                self.well_known_types.update(ref_types.keys())

                for name, serialized_type in script_types.items():
                    if name and name not in self.stubs:
                        self.generate_stub(serialized_type.node, name, script_types, True)
                for ref_name, ref in ref_types.items():
                    if ref_name not in self.stubs:
                        self.generate_stub(ref.node, ref_name)
        self.check_save_type()
        self.write_stub(self.output_path / f'stub/{output_file_name}.pyi')
        self.write_stub(self.output_path / f'typed_dict/{output_file_name}.py', True)

    @staticmethod
    def get_files(input_path: Path | list[Path]) -> tuple[list[Path], Path]:
        if isinstance(input_path, list):
            return input_path, input_path[0].parent
        elif input_path.is_file():
            return [input_path], input_path.parent
        else:
            return list(input_path.iterdir()), input_path

    @staticmethod
    def check_valid_path(i: Any) -> bool:
        if isinstance(i, Path):
            return i.exists()
        if isinstance(i, Iterable):
            return all(j.is_file() for j in i)
        return False

    @staticmethod
    def glob_list(path: Path, patterns: list[str]) -> list[Path]:
        result = set()
        for i in patterns:
            if match := next(path.glob(i), None):
                result.add(match)
        return list(result)

    def get_name_from_local_identifier(self, local_obj: LocalSerializedObjectIdentifier) -> None | str:
        for asset in chain(self.env.assets, self.monoscript_env.assets):
            if local_obj.local_identifier_in_file in asset.files:
                return asset.files[local_obj.local_identifier_in_file].read().m_Name
        return None

    def generate_stub(
            self,
            typetree: TypeTreeNode,
            name: str,
            script_types: None | dict[str, SerializedType] = None,
            monobehaviour: bool = False,
            generic: bool = False,
            ):
        stub = StubClass(name, generic=generic)
        if monobehaviour:
            stub.base.append('MonoBehaviour')
            typetree.m_Children = typetree.m_Children[4:]
        self.stubs[name] = stub
        for child in typetree.m_Children:
            stub.attributes.append(Field(child.m_Name, self.get_type(child, script_types, generic=generic)))

    def get_type(
            self, node: TypeTreeNode, script_types: None | dict[str, SerializedType] = None, generic: bool = False
            ) -> Type:
        if node.m_Type in BASE_TYPE_MAP:
            return Type(BASE_TYPE_MAP[node.m_Type])
        elif node.m_Type.startswith('PPtr<'):
            sub_type = node.m_Type[5:-1]
            if sub_type.startswith('$'):
                sub_type = sub_type[1:]
                if sub_type not in self.stubs and script_types is not None and sub_type in script_types:
                    self.generate_stub(script_types[sub_type].node, sub_type, script_types, monobehaviour=True)
            type_ = Type('PPtr')
            if self.is_known(sub_type):
                type_.subTypes.append(Type(sub_type))
            return type_
        elif node.m_Type == 'pair':
            return Type('tuple', [self.get_type(node.m_Children[0]), self.get_type(node.m_Children[1])])
        elif node.m_Children and node.m_Children[0].m_Type == 'Array':
            sub_node = node.m_Children[0].m_Children[1]
            if sub_node.m_Type == 'managedRefArrayItem':
                if sub_node.m_Type not in self.stubs:
                    self.generate_stub(sub_node, sub_node.m_Type, script_types, generic=True)
                if not generic:
                    sub = [Type(node.m_Type)] if self.is_known(node) else self.interface_mapping.get(node.m_Type, [])
                    return Type('list', [Type('managedRefArrayItem', sub)])
            return Type('list', [self.get_type(sub_node)])
        elif node.m_Type == 'managedReference':
            if node.m_Type not in self.stubs:
                self.generate_stub(node, node.m_Type, script_types, generic=True)
            return Type('managedReference', self.manage_ref_mapping.get(node.m_Name, []))
        elif node.m_Type == 'MetadataDictionaryContainer`1':
            if node.m_Type not in self.stubs:
                self.generate_stub(node, node.m_Type, script_types, generic=True)
            type_ = Type('MetadataDictionaryContainer')
            if self.is_known(node.m_Children[1].m_Type):
                type_.subTypes.append(Type(node.m_Children[1].m_Type))
            return type_
        else:
            if node.m_Type not in self.stubs:
                self.generate_stub(node, node.m_Type, script_types, generic=generic)
            return Type(node.m_Type)

    def write_stub(self, output_file: Path, typed_dict: bool = False):
        Field.reserved_name = ['class'] if typed_dict else []
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with output_file.open('w') as file:
            file.write(GENERATED_HEADER_TYPEDDICT if typed_dict else GENERATED_HEADER)
            file.write(self.get_str_import(typed_dict))

            for _, stub in sorted(self.stubs.items(), key=lambda item: item[0]):
                stub.write(file, typed_dict)

    def get_str_import(self, typed_dict: bool = False) -> str:
        if not self.import_:
            return ''
        if typed_dict:
            result = []
            for i in sorted(self.import_):
                result.append(f"""class {i}(TypedDict):
    pass""")
            result.append('')
            return '\n'.join(result)
        else:
            return f'from UnityPy.classes.generated import {", ".join(sorted(self.import_))}\n'

    def is_known(self, node: TypeTreeNode | str) -> bool:
        type_name = node.m_Type if isinstance(node, TypeTreeNode) else node
        if type_name in self.well_known_types:
            return True
        elif hasattr(generated, type_name):
            self.import_.add(type_name)
            self.well_known_types.add(type_name)
            return True
        elif type_name in self.stubs:
            self.well_known_types.add(type_name)
            return True
        return False

    def load_save_type(self) -> None:
        self.interface_mapping = {k: [Type(i) for i in value] for k, value in interface_mapping.items()}
        self.manage_ref_mapping = {
                k: self.interface_mapping.get(v, [Type(v)]).copy() for k, v in manage_ref_mapping.items()
                }

    def check_save_type(self) -> None:
        for i in chain(self.interface_mapping.values(), self.manage_ref_mapping.values()):
            j = 0
            while j < len(i):
                if not self.is_known(i[j].name):
                    del i[j]
                else:
                    j += 1
            if len(i) > 1:
                i[0].name = f'Union[{"| ".join(t.name for t in i)}]'
                del i[1:]
