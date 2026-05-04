from dataclasses import dataclass

from pydantic import Field

from pydofus3.binaryReader import BinaryReader
from pydofus3.catalog.binary.CatalogBinaryReader import CatalogBinaryReader


@dataclass
class SerializedType:
    AssemblyName: str = Field(alias='m_AssemblyName')
    ClassName: str = Field(alias='m_ClassName')

    @staticmethod
    def read(reader: CatalogBinaryReader | BinaryReader, offset: int | None = None) -> 'SerializedType':
        if not isinstance(reader, CatalogBinaryReader):
            return SerializedType(reader.read_str(reader.u8(), 'ascii'), reader.read_str(reader.u8(), 'ascii'))

        if offset is not None:
            reader.pos = offset

        assembly_name_offset = reader.u32()
        class_name_offset = reader.u32()

        return SerializedType(
            reader.read_encoded_string(assembly_name_offset, '.'), reader.read_encoded_string(class_name_offset, '.')
        )

    def get_match_name(self) -> str:
        return f'{self.get_assembly_short_name()}; {self.ClassName}'

    def get_assembly_short_name(self) -> str:
        if ',' not in self.AssemblyName:
            raise Exception('Assembly name must have commas')
        return self.AssemblyName.split(',')[0]
