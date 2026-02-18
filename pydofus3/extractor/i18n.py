from collections import defaultdict
from compression import zstd
from itertools import batched, chain
from pathlib import Path
from struct import Struct
from typing import TypedDict

import orjson
from Sbr import BinaryReader, EnumStructBase
from tqdm import tqdm


class I18N(TypedDict):
    id: int
    fr: str
    en: str
    de: str
    es: str
    pt: str


def read(i18n_dir: Path | str) -> dict[int, I18N]:
    """
    read dofus i18n binary files
    """
    if isinstance(i18n_dir, str):
        i18n_dir = Path(i18n_dir)
    i18n: dict[int, dict[str, str]] = defaultdict(dict)
    for file in tqdm(list(i18n_dir.rglob('*.bin')), desc='load i18n'):
        with file.open('rb') as f:
            reader = BinaryReader(f)
            reader.str(reader.u8)  # can't be used, always fr
            lang = file.stem
            text = reader.read_struct(Struct(f'<{EnumStructBase.u32 * reader.u32 * 2}'))
            text_ui = reader.read_struct(Struct(f'<{f"{EnumStructBase.u64}{EnumStructBase.u32}" * reader.u32}'))

            for key, pos in batched(chain(text, text_ui), 2):
                i18n[key][lang] = reader.offset(pos).str(reader.read_varint())
    return {
            k: {
                    'id': k,
                    'fr': v.get('fr', f'UNKNOWN_TEXT_ID_{k}'),
                    'en': v.get('en', f'UNKNOWN_TEXT_ID_{k}'),
                    'de': v.get('de', f'UNKNOWN_TEXT_ID_{k}'),
                    'es': v.get('es', f'UNKNOWN_TEXT_ID_{k}'),
                    'pt': v.get('pt', f'UNKNOWN_TEXT_ID_{k}'),
                    }
            for k, v in i18n.items()
            }


def extract_i18n(i18n_dir: Path, output_dir: Path, compress: bool = False) -> dict[int, I18N]:
    """
    read and save dofus binary i18n files
    """
    output_dir.mkdir(exist_ok=True, parents=True)
    output_file = output_dir / 'i18n.json'
    data = read(i18n_dir)
    json_bytes = orjson.dumps(data, option=orjson.OPT_NON_STR_KEYS)
    if compress:
        json_bytes = zstd.compress(json_bytes)
        output_file = output_file.with_name(f'{output_file.name}.zst')
    output_file.write_bytes(json_bytes)
    return data
