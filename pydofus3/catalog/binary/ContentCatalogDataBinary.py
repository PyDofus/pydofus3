from dataclasses import dataclass
from pathlib import Path

from pydofus3.catalog.catalog import (
    ContentCatalogData,
    ObjectInitializationData,
    ResourceLocation,
    SerializedObjectDecoder,
)

from .CatalogBinaryReader import CatalogBinaryReader
from .ContentCatalogDataBinaryHeader import ContentCatalogDataBinaryHeader


@dataclass(kw_only=True)
class ContentCatalogDataBinary(ContentCatalogData):
    reader: CatalogBinaryReader
    header: ContentCatalogDataBinaryHeader

    @classmethod
    def read(cls, path: Path)->'ContentCatalogDataBinary':
        reader = CatalogBinaryReader(path.read_bytes())
        header = ContentCatalogDataBinaryHeader.read(reader)
        reader.version = header.version

        catalog = ContentCatalogDataBinary(
            reader=reader,
            header=header,
            LocatorId=reader.read_encoded_string(header.idOffset),
            BuildResultHash=reader.read_encoded_string(header.buildResultHashOffset),
            InstanceProviderData=ObjectInitializationData.read(reader, header.instanceProviderOffset),
            SceneProviderData=ObjectInitializationData.read(reader, header.sceneProviderOffset),
            ResourceProviderData=[
                ObjectInitializationData.read(reader, offset)
                for offset in reader.read_offset_array(header.initObjectsArrayOffset)
            ],
        )
        catalog.read_resources()
        return catalog

    def read_resources(self) -> None:
        offsets = self.reader.read_offset_array(self.header.keysOffset)
        self.ressources = {  # ty:ignore[invalid-assignment]
            SerializedObjectDecoder.decode_v2(self.reader, keyOffset): [ # noqa
                ResourceLocation.read(self.reader, pos)
                for pos in self.reader.read_offset_array(locationListOffset)
            ]
            for keyOffset, locationListOffset in zip(offsets[::2], offsets[1::2])
        }

        for key, locations in self.ressources.items():
            for location in locations:
                location.keys.append(key)
        for location in self.reader.cached_locations.values():
                self.internal_id_mapping[location.InternalId].append(location)
