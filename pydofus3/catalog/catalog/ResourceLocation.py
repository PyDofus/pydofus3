from dataclasses import dataclass, field

from pydofus3.catalog.binary.CatalogBinaryReader import CatalogBinaryReader

from .SerializedObjectDecoder import SerializedObjectDecoder
from .SerializedType import SerializedType
from .WrappedSerializedObject import WrappedSerializedObject


@dataclass
class ResourceLocation:
    InternalId: str
    ProviderId: str
    DependencyKey: str | None
    Dependencies: list["ResourceLocation"]
    Data: WrappedSerializedObject | None
    DependencyHashCode: int
    PrimaryKey: str
    Type: SerializedType
    keys: list[str | int] = field(default_factory=list)

    @staticmethod
    def read(reader: CatalogBinaryReader, offset: int) -> "ResourceLocation":
        if cached := reader.cached_locations.get(offset):
            return cached

        data = reader.offset(offset).read_u32_multiple(7)

        location = ResourceLocation(
            PrimaryKey=reader.read_encoded_string(data[0], "/"),
            InternalId=reader.read_encoded_string(data[1], "/"),
            ProviderId=reader.read_encoded_string(data[2], "."),
            DependencyKey=None,
            Dependencies=[
                ResourceLocation.read(reader, offset)
                for offset in reader.read_offset_array(data[3])
            ],
            DependencyHashCode=data[4],
            Data=SerializedObjectDecoder.decode_v2(reader, data[5]),  # ty:ignore[invalid-argument-type]
            Type=SerializedType.read(reader, data[6]),
        )
        reader.cached_locations[offset] = location
        return location

    def serialize(self) -> dict:
        return {
            "InternalId": self.InternalId,
            "ProviderId": self.ProviderId,
            "DependencyKey": self.DependencyKey,
            "Dependencies": [d.InternalId for d in self.Dependencies],
            "Data": self.Data,
            "DependencyHashCode": self.DependencyHashCode,
            "PrimaryKey": self.PrimaryKey,
            "Type": self.Type,
            "keys": self.keys,
        }
