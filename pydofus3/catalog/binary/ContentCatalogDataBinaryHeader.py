from dataclasses import dataclass

from .CatalogBinaryReader import CatalogBinaryReader


@dataclass
class ContentCatalogDataBinaryHeader:
    magic: int
    version: int
    keysOffset: int
    idOffset: int
    instanceProviderOffset: int
    sceneProviderOffset: int
    initObjectsArrayOffset: int
    buildResultHashOffset: int = 0xFFFFFFFF

    @staticmethod
    def read(reader: CatalogBinaryReader) -> 'ContentCatalogDataBinaryHeader':
        content = ContentCatalogDataBinaryHeader(*reader.read_i32_multiple(7))
        if content.version == 1 and content.keysOffset == 0x20:
            content.buildResultHashOffset = reader.u32()
        return content
