from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class UnityExtractorOptionConfig:
    """
    extractor option config
    """

    output: Path = Path('output')
    compress: bool = False
    files: Iterable[Path] | None = None
    force_texture2d: bool = False
    type_tree: bool = False
    add_script: bool = False
    reference: bool = False
    force_object: bool = False
    sprite_rect_size: bool = False
    process_datacenter: bool = False
    load_all_files: bool = False
    force_gc_collect: bool = False
    no_big_int:bool = False
    indent: bool = False
    skin_png: bool = False
    skin_webp: bool = False
