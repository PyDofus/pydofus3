import struct
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import UnityPy
from UnityPy.enums import ClassIDType, TextureFormat
from UnityPy.helpers.ContainerHelper import ContainerHelper
from UnityPy.classes import Font, GameObject, Material, Mesh, MonoBehaviour, Shader, Sprite, TextAsset, Texture2D
import texture2ddecoder

from pydofus3.enum_data import TypeData, get_data_path

try:
    from fpng_py import fpng_encode_image_to_file
    _HAS_FPNG = True
except ImportError:
    _HAS_FPNG = False
    fpng_encode_image_to_file = None  # ty:ignore[invalid-assignment]

from PIL import Image
from UnityPy.config import UnityVersionFallbackWarning

from pydofus3.config import settings


class SingletonMeta(type):
    """
    Singleton meta class
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


def save_img(output: Path, img: Image.Image) -> None:
    """
    save img with fpng if possible for speed else save with PIL
    :param output: output path
    :param img: pil image
    """
    if output.suffix not in ['.png', '.jpg']:
        ext = '.png' if img.mode in ['RGBA', 'RGB'] else '.jpg'
        output = output.with_suffix(ext)
    if output.suffix == '.png' and _HAS_FPNG and img.mode in ('RGB', 'RGBA'):
        w, h = img.size
        fpng_encode_image_to_file(str(output), img.tobytes(), w, h, len(img.mode))
    else:
        if output.suffix == '.jpg' and img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(output)


DDS_FORMATS = {
    TextureFormat.DXT1: b'DXT1',
    TextureFormat.DXT1Crunched: b'DXT1',
    TextureFormat.DXT5: b'DXT5',
    TextureFormat.DXT5Crunched: b'DXT5',
}


def texture_dds(texture: Texture2D) -> bytes | None:
    """
    the texture's first mip level as a DDS file
    """
    texture_format = TextureFormat(texture.m_TextureFormat)
    fourcc = DDS_FORMATS.get(texture_format)
    if fourcc is None or not texture.m_Width or not texture.m_Height:
        return None
    data = bytes(texture.get_image_data())
    if 'Crunched' in texture_format.name:
        data = texture2ddecoder.unpack_unity_crunch(data)
    block_size = 8 if fourcc == b'DXT1' else 16
    level_size = ((texture.m_Width + 3) // 4) * ((texture.m_Height + 3) // 4) * block_size
    return dds_bytes(data[:level_size], texture.m_Width, texture.m_Height, fourcc)

def dds_bytes(blocks: bytes, width: int, height: int, fourcc: bytes = b'DXT5') -> bytes:
    """
    wrap compressed blocks in a DDS file
    """
    flags = 0x1 | 0x2 | 0x4 | 0x1000 | 0x80000
    header = struct.pack('<7I44x', 124, flags, height, width, len(blocks), 0, 1)
    pixel_format = struct.pack('<2I4s5I', 32, 0x4, fourcc, 0, 0, 0, 0, 0)
    caps = struct.pack('<4I4x', 0x1000, 0, 0, 0)
    return b'DDS ' + header + pixel_format + caps + blocks


def find_directory_containing_file(starting_path: Path, target_filename: str) -> Path | None:
    """
    search file in parents directory
    """
    target_filename = target_filename.lower()
    current_dir = starting_path.parent

    while current_dir != current_dir.parent:
        if any(file.name.lower().startswith(target_filename) for file in current_dir.iterdir()):
            return current_dir
        current_dir = current_dir.parent
    return None


def group_file_by_catalog(files: Iterable[Path], dofus_path: Path) -> dict[str, list[Path]]:
    """
    groupe file by catalog
    :param files: list of file, iterable path
    :param dofus_path: dofus game folder
    :return: dict of catalog as key and list of file as value
    """
    result = defaultdict(list)
    catalogs_gen = (str(i.parent.relative_to(dofus_path)) for i in dofus_path.rglob('**catalog*.bin'))
    catalogs = sorted(catalogs_gen, key=lambda f: f.count('/'), reverse=True)
    for file in files:
        str_file = str(file)
        for catalog in catalogs:
            if catalog in str_file:
                result[catalog].append(file)
                break
    return result


def get_unity_version(game_data: Path|None) -> str:
    """
    :param game_data: game_data folder
    :return: unity version
    get unity version
    """
    if game_data is None or not game_data.is_dir():
        return settings.unity_fallback_version

    try:
        path = get_data_path(game_data, TypeData.Dofus_Data)
        env = UnityPy.load(str(path/'level0'))
        return env.file.unity_version  # ty:ignore[unresolved-attribute]
    except (AttributeError, UnityVersionFallbackWarning):
        print(f"can't read unity version from level0 {game_data}, use default value {settings.unity_fallback_version}")
    return settings.unity_fallback_version


def set_unity_version(game_data: Path|None) -> None:
    """
    set unitypy fallback unity version with the unity version of the game
    :param game_data: game_data folder
    """
    UnityPy.config.FALLBACK_UNITY_VERSION = get_unity_version(game_data)  # ty:ignore[possibly-missing-submodule]


_preload_table_enabled = False


def set_preload_table(enabled: bool) -> None:
    """
    enable or disable UnityPy (>= 1.25.3) preload table parsing.
    """
    global _preload_table_enabled
    _preload_table_enabled = enabled


def _patch_preload_table() -> None:
    original = getattr(ContainerHelper, 'parse_preload_table', None)
    if original is None or getattr(original, '_pydofus3_patched', False):
        return

    def parse_preload_table(self) -> None:
        if _preload_table_enabled:
            original(self)

    parse_preload_table._pydofus3_patched = True  # ty:ignore[unresolved-attribute]
    ContainerHelper.parse_preload_table = parse_preload_table


_patch_preload_table()
