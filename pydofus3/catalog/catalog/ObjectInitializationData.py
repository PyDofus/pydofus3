from typing import Annotated

from pydantic import ConfigDict, Field
from pydantic.dataclasses import dataclass

from pydofus3.catalog.binary.CatalogBinaryReader import CatalogBinaryReader

from .SerializedType import SerializedType


@dataclass(config=ConfigDict(validate_by_name=True, validate_by_alias=True))
class ObjectInitializationData:
    Id: Annotated[str, Field(alias='m_Id')]
    ObjectType: Annotated[SerializedType, Field(alias='m_ObjectType')]
    Data: Annotated[str, Field('m_Data')]

    @staticmethod
    def read(reader: CatalogBinaryReader, offset: int) -> 'ObjectInitializationData':
        id_offset, object_type_offset, data_offset = reader.offset(offset).read_u32_multiple(3)

        return ObjectInitializationData(
            Id=reader.read_encoded_string(id_offset),
            ObjectType=SerializedType.read(reader, object_type_offset),
            Data=reader.read_encoded_string(data_offset),
        )
