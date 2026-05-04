import logging
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import field
from pathlib import Path
from typing import Self

import orjson
from pydantic.dataclasses import dataclass

from pydofus3.binaryReader import BinaryReader

from .ObjectInitializationData import ObjectInitializationData
from .ResourceLocation import ResourceLocation

logger = logging.getLogger(__name__)

@dataclass(kw_only=True)
class ContentCatalogData(ABC):
    LocatorId: str
    BuildResultHash: str
    InstanceProviderData: ObjectInitializationData
    SceneProviderData: ObjectInitializationData
    ResourceProviderData: list[ObjectInitializationData]

    ressources: dict[str, list[ResourceLocation]] = field(default_factory=dict)
    internal_id_mapping: dict[str, list[ResourceLocation]] = field(default_factory=lambda : defaultdict(list))

    @classmethod
    @abstractmethod
    def read(cls, path: Path) -> "ContentCatalogData":
        pass

    @abstractmethod
    def read_resources(self) -> None:
        pass

    def save(self, path: Path|str):
        if isinstance(path, str):
            path: Path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {key:val[0].serialize() for key,val in self.internal_id_mapping.items() if val}
        path.write_bytes(orjson.dumps(data))

    def get_output_path(self, base_path: Path, container_name:str) -> Path:
        ressources = self.internal_id_mapping.get(container_name)
        if not ressources:
            logger.info(f'key "{container_name}" not in catalog, use key as path output')
            return base_path / container_name
        ressource = ressources[0]
        if len(ressource.keys)>=2 and (sub_key := next((i for i in ressource.keys if i != ressource.PrimaryKey and i in ['1x', '2x']), None)):
            entry_path = Path(ressource.PrimaryKey)
            return base_path / entry_path.parent / str(sub_key) / entry_path.name
        return base_path / ressource.PrimaryKey


@dataclass
class Bucket:
    offset: int
    entries: tuple[int, ...]

    @classmethod
    def read(cls, reader: BinaryReader) -> "Bucket":
        return Bucket(reader.i32(), reader.read_i32_multiple(reader.i32()))
