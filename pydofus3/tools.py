from collections import defaultdict
from pathlib import Path
from typing import Iterable

import UnityPy
from fpng_py import fpng_encode_image_to_file
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
    if output.suffix == '.png':
        w, h = img.size
        fpng_encode_image_to_file(str(output), img.tobytes(), w, h, len(img.mode))
    else:
        if output.suffix == '.jpg' and img.mode != 'RGB':
            img = img.convert('RGB')
        img.save(output)


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
    if game_data:
        try:
            if game_data.is_dir():
                env = UnityPy.load(str(game_data / 'Dofus_Data/level0'))
                return env.file.unity_version
        except (AttributeError, UnityVersionFallbackWarning):
            print(f"can't read unity version from level0 {game_data}, use default value {settings.unity_fallback_version}")
    return settings.unity_fallback_version


def set_unity_version(game_data: Path) -> None:
    """
    set unitypy fallback unity version with the unity version of the game
    :param game_data: game_data folder
    """
    UnityPy.config.FALLBACK_UNITY_VERSION = get_unity_version(game_data)
