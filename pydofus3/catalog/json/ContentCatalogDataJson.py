from base64 import b64decode
from io import BytesIO
from pathlib import Path
from typing import Annotated

from pydantic import BaseModel
from pydantic.fields import Field

from pydofus3.binaryReader import BinaryReader
from pydofus3.catalog.catalog import (
    Bucket,
    ContentCatalogData,
    ObjectInitializationData,
    ResourceLocation,
    SerializedObjectDecoder,
    SerializedType,
)


class ContentCatalogDataJson(BaseModel, ContentCatalogData):
    LocatorId: Annotated[str, Field(alias='m_LocatorId')]
    BuildResultHash: Annotated[str, Field('', alias='m_BuildResultHash')]
    InstanceProviderData: Annotated[ObjectInitializationData, Field(alias='m_InstanceProviderData')]
    SceneProviderData: Annotated[ObjectInitializationData, Field(alias='m_SceneProviderData')]
    ResourceProviderData: Annotated[list[ObjectInitializationData], Field(alias='m_ResourceProviderData')]

    ProviderIds: Annotated[list[str], Field(alias='m_ProviderIds')]
    InternalIds: Annotated[list[str], Field(alias='m_InternalIds')]
    m_KeyDataString: str
    m_BucketDataString: str
    m_EntryDataString: str
    m_ExtraDataString: str
    Keys: Annotated[list[str], Field(default_factory=list, alias='m_Keys')]
    ResourceTypes: Annotated[list[SerializedType], Field(alias='m_resourceTypes')]
    InternalIdPrefixes: Annotated[list[str], Field(default_factory=list, alias='m_InternalIdPrefixes')]

    @classmethod
    def read(cls, path: Path) -> 'ContentCatalogDataJson':
        catalog = cls.model_validate_json(path.read_bytes())
        catalog.read_resources()
        return catalog

    def read_resources(self) -> None:
        bucket_reader = BinaryReader(BytesIO(b64decode(self.m_BucketDataString)))
        buckets = bucket_reader.read_class_multiple(Bucket, bucket_reader.i32())

        key_reader = BinaryReader(BytesIO(b64decode(self.m_KeyDataString)))
        keys = [SerializedObjectDecoder.decode_v1(key_reader, buckets[key].offset) for key in range(key_reader.i32())]

        entry_reader = BinaryReader(BytesIO(b64decode(self.m_EntryDataString)))
        extra_reader = BinaryReader(BytesIO(b64decode(self.m_ExtraDataString)))
        locations = []
        for i in range(entry_reader.i32()):
            (
                internal_id_i,
                provider_i,
                dependency_key_i,
                dep_hash,
                data_i,
                primary_key_i,
                resource_type_i,
            ) = entry_reader.read_i32_multiple(7)

            locations.append(
                ResourceLocation(
                    InternalId=self.get_internal_id(internal_id_i),
                    ProviderId=self.ProviderIds[provider_i],
                    DependencyKey=keys[dependency_key_i] if dependency_key_i >= 0 else None,  # ty:ignore[invalid-argument-type]
                    Dependencies=[],
                    Data=(SerializedObjectDecoder.decode_v1(extra_reader, data_i) if data_i >= 0 else None),  # ty:ignore[invalid-argument-type]
                    DependencyHashCode=dep_hash,
                    PrimaryKey=self.Keys[primary_key_i] if self.Keys else keys[primary_key_i],  # ty:ignore[invalid-argument-type]
                    Type=self.ResourceTypes[resource_type_i],
                )
            )

        for key, bucket in zip(keys, buckets):
            for entry in bucket.entries:
                locations[entry].keys.append(key)

        self.ressources = {key: [locations[entry] for entry in bucket.entries] for key, bucket in zip(keys, buckets)} # noqa  # ty:ignore[invalid-assignment]

        for location in locations:
            self.internal_id_mapping[location.InternalId].append(location)

    def get_internal_id(self, internal_id_index: int) -> str:
        internal_id = self.InternalIds[internal_id_index]
        if (index := internal_id.find('#')) != -1:
            prefix = self.InternalIdPrefixes[int(internal_id[:index])]
            internal_id = prefix + internal_id[index + 1 :]
        return internal_id
