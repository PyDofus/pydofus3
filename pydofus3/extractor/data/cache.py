import time
from pathlib import Path

import orjson

from pydofus3.enum_data import TypeData


def process_character_cache(output:Path)->None:
    result = {}
    for type_ in (TypeData.Skins, TypeData.Bones):
        folder = output/ type_
        result[type_.split('/')[-1]] = {str(p.parent.relative_to(folder)).lower(): int(p.stat().st_mtime) for p in folder.rglob("skin.json")}

    output_file = (output / TypeData.Bones).parent / "table.json"
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_bytes(orjson.dumps(result))

def update_character_cache(grouped_file:  dict[str, list[Path]], output :Path)-> None:
    cache_file = (output / TypeData.Bones).parent / "table.json"
    if not cache_file.is_file():
        process_character_cache(output)
        return
    cache_data = orjson.loads(cache_file.read_bytes())
    time_now = int(time.time())
    for type_, prefix in ((TypeData.Skins,'skins_assets_skin_'), (TypeData.Bones, 'bones_assets_bone_')):
        cache_type = cache_data.get(type_.split('/')[-1], {})
        for f in grouped_file.get(type_, []):
            key = f.stem.removeprefix(prefix).lower()
            cache_type[key] = time_now
    cache_file.write_bytes(orjson.dumps(cache_data))
