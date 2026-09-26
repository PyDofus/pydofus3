"""
Follow the references (PPtr) between Unity objects
"""

import logging
from collections import deque
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from UnityPy import Environment
from UnityPy.enums import ClassIDType
from UnityPy.files import ObjectReader, SerializedFile

from pydofus3.extractor.data.tools import get_monoscript

logger = logging.getLogger(__name__)

SKIP_TYPES = {
    ClassIDType.Texture2D,
    ClassIDType.Shader,
    ClassIDType.Font,
    ClassIDType.TextAsset,
    ClassIDType.AudioClip,
    ClassIDType.Mesh,
    ClassIDType.MonoScript,
}

NOT_EXPORTED = {
    ClassIDType.Transform,
    ClassIDType.RectTransform,
    ClassIDType.CanvasRenderer,
    ClassIDType.MeshFilter,
    ClassIDType.MeshRenderer,
    ClassIDType.SkinnedMeshRenderer,
    ClassIDType.SpriteRenderer,
    ClassIDType.MonoScript,
    ClassIDType.AssetBundle,
    ClassIDType.PreloadData,
}


def file_key(name: str) -> str:
    return name.lower()


def object_key(obj: ObjectReader) -> str:
    """``<file name>:<path_id>`` of an object."""
    return f'{file_key(obj.assets_file.name)}:{obj.path_id}'


def reference_file(assets_file: SerializedFile, file_id: int) -> str | None:
    if file_id == 0:
        return assets_file.name
    if 0 < file_id <= len(assets_file.externals):
        return assets_file.externals[file_id - 1].name
    return None


def reference_key(assets_file, file_id: int, path_id: int) -> str | None:
    if not path_id:
        return None
    name = reference_file(assets_file, file_id)
    return f'{file_key(name)}:{path_id}' if name else None


def resolve(assets_file, file_id: int, path_id: int) -> ObjectReader | None:
    """The object a reference points to, when its file is loaded in the environment."""
    if not path_id:
        return None
    if file_id == 0:
        return assets_file.objects.get(path_id)
    if not(name := reference_file(assets_file, file_id)):
        return None
    target = assets_file.environment.cabs.get(file_key(name))
    return target.objects.get(path_id) if target is not None and hasattr(target, 'objects') else None


def is_reference(value: Any) -> bool:
    return isinstance(value, dict) and len(value) == 2 and 'm_FileID' in value and 'm_PathID' in value


def iter_references(data: Any, field: str = '') -> Iterator[tuple[str, int, int]]:
    if is_reference(data):
        if data['m_PathID']:
            yield field, data['m_FileID'], data['m_PathID']
    elif isinstance(data, dict):
        for key, value in data.items():
            yield from iter_references(value, field or str(key))
    elif isinstance(data, (list, tuple)):
        for value in data:
            yield from iter_references(value, field)


def read_tree(obj: ObjectReader) -> dict | None:
    if obj.type in SKIP_TYPES:
        return None
    try:
        return obj.read_typetree()
    except Exception:
        logger.debug(f'{object_key(obj)} {obj.type.name} not read as a typetree', exc_info=True)
        return None


def outgoing(obj: ObjectReader, tree: dict | None = None) -> list[tuple[str, str, ObjectReader | None]]:
    """What an object references"""
    tree = read_tree(obj) if tree is None else tree
    if not tree:
        return []
    result = []
    for field, file_id, path_id in iter_references(tree):
        if key := reference_key(obj.assets_file, file_id, path_id):
            result.append((field, key, resolve(obj.assets_file, file_id, path_id)))
    return result


def dependencies(root: ObjectReader) -> list[tuple[str, ObjectReader]]:
    """
    extract all dependencies
    """
    group_by_field = root.type == ClassIDType.MonoBehaviour
    seen = {object_key(root)}
    queue: deque[tuple[str, ObjectReader]] = deque()
    for field, key, target in outgoing(root):
        if target is not None and key not in seen:
            seen.add(key)
            queue.append((field if group_by_field else '', target))
    result = []
    while queue:
        group, obj = queue.popleft()
        if obj.type not in NOT_EXPORTED:
            result.append((group, obj))
        for _, key, target in outgoing(obj):
            if target is not None and key not in seen:
                seen.add(key)
                queue.append((group, target))
    return result


def display_name(obj: ObjectReader) -> str:
    """name or script's class for a nameless or its type."""
    try:
        name = obj.peek_name()
    except Exception:
        logger.debug(f'name of {object_key(obj)} not read', exc_info=True)
        name = ''
    if not name and obj.type == ClassIDType.MonoBehaviour and (script := get_monoscript(obj)):
        name = script.parse_as_dict().get('m_ClassName', '')
    name = name or obj.type.name
    return ''.join('_' if c in '/\\:*?"<>|' else c for c in name).strip() or obj.type.name


def annotate(data: Any, assets_file, paths: dict[str, Path], base: Path) -> None:
    """
    Write, next to every reference the key of its target and path.
    """
    if is_reference(data):
        if key := reference_key(assets_file, data['m_FileID'], data['m_PathID']):
            data['$key'] = key
            if (path := paths.get(key)) is not None:
                try:
                    data['$path'] = path.relative_to(base).as_posix()
                except ValueError:
                    data['$path'] = path.as_posix()
    elif isinstance(data, dict):
        for value in list(data.values()):
            annotate(value, assets_file, paths, base)
    elif isinstance(data, list):
        for value in data:
            annotate(value, assets_file, paths, base)
