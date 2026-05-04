from pydofus3.enum_data import TypeData
from pathlib import Path
import orjson
import time

def process_character_cache(output:Path)->None:
    result = {}
    for type_ in (TypeData.Skins, TypeData.Bones):
        folder = output/ type_
        result[type_.split('/')[-1]] = {str(p.parent.relative_to(folder)): int(p.stat().st_mtime) for p in folder.rglob("skin.json")}

    output_file = (output / TypeData.Bones).parent / "table.json"
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_bytes(orjson.dumps(result))

def update_character_cache(grouped_file:  dict[str, list[Path]], output)-> None:
    cache_file = (output / TypeData.Bones).parent / "table.json"
    cache_data = orjson.loads(cache_file.read_bytes())
    time_now = int(time.time())
    for type_ in (TypeData.Skins, TypeData.Bones):
        cache_type = cache_data.get(type_.split('/')[-1], {})
        for f in grouped_file.get(type_, []):
            cache_type[f.stem] = time_now
    cache_file.write_bytes(orjson.dumps(cache_data))
