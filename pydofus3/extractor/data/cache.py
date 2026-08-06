import time
from pathlib import Path

import orjson

from pydofus3.enum_data import TypeData


def process_character_cache(output:Path)->None:
    result = {}
    for type_ in (TypeData.Skins, TypeData.Bones):
        folder = output/ type_
        result[type_.split('/')[-1]] = {str(p.parent.relative_to(folder)) : int(p.stat().st_mtime) for p in folder.rglob("skin.json")}

    output_file = (output / TypeData.Bones).parent / "table.json"
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_bytes(orjson.dumps(result))

def update_character_cache(grouped_file:  dict[str, list[Path]], output :Path)-> None:
    cache_file = (output / TypeData.Bones).parent / "table.json"
    if not cache_file.is_file():
        process_character_cache(output)
        return
    bone_output = output / TypeData.Bones
    bone_mapping = {p.stem.lower() : p.stem for p in bone_output.iterdir()} if bone_output.is_dir() else {}
    cache_data = orjson.loads(cache_file.read_bytes())
    time_now = int(time.time())
    for type_, prefix, mapping in ((TypeData.Skins,'skins_assets_skin_', {}), (TypeData.Bones, 'bones_assets_bone_', bone_mapping)):
        cache_type = cache_data.get(type_.split('/')[-1], {})
        for f in grouped_file.get(type_, []):
            if not f.stem.startswith(prefix):
                continue
            key = f.stem.removeprefix(prefix)
            folder = mapping.get(key, key)
            cache_type[folder] = time_now
    cache_file.write_bytes(orjson.dumps(cache_data))
