from pydofus3.binaryReader import BinaryReader
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..catalog import ResourceLocation # noqa

class CatalogBinaryReader(BinaryReader):
    def __init__(self, data: bytes):
        super().__init__(data)
        self.version = 0
        self._obj_cache: dict[int|tuple[int,str|bool], str | tuple[int, ...]] = {}
        self.cached_locations : dict[int, 'ResourceLocation']= {}

    def read_encoded_string(self, encoded_offset: int, dynstr_sep: str|None =None) -> str:
        if encoded_offset == 0xFFFFFFFF:
            return ""
        if cached := self._obj_cache.get(encoded_offset):
            return cached  # ty:ignore[invalid-return-type]

        offset = encoded_offset & 0x3FFFFFFF

        if dynstr_sep and (encoded_offset & 0x40000000) != 0:
            value = self.read_dynamic_string(offset, dynstr_sep)
        else:
            unicode = (encoded_offset & 0x80000000) != 0
            value = self.read_basic_string(offset, unicode)
        self._obj_cache[encoded_offset] = cached  # ty:ignore[invalid-assignment]
        return value

    def read_basic_string(self, offset: int, unicode: bool) -> str:
        if cached:=self._obj_cache.get((offset,unicode)):
            return cached  # ty:ignore[invalid-return-type]
        str_= self.offset(offset-4).read_str(self.i32(), "utf-16" if unicode else "ascii")
        self._obj_cache[(offset,unicode)] = str_
        return str_

    def read_dynamic_string(self, offset: int, sep: str) -> str:
        if cached:= self._obj_cache.get((offset,sep)):
            return cached  # ty:ignore[invalid-return-type]

        part_str = []
        next_part = offset
        while True:
            part, next_part = self.offset(next_part).read_u32_multiple(2)
            part_str.append(self.read_encoded_string(part))
            if next_part == 0xFFFFFFFF:
                break

        if self.version > 1:
            part_str = reversed(part_str)

        dyn_str= sep.join(part_str)
        self._obj_cache[(offset,sep)] = dyn_str
        return dyn_str

    def read_offset_array(self, encoded_offset: int) -> tuple[int, ...]:
        if encoded_offset == 0xFFFFFFFF:
            return ()
        if cached := self._obj_cache.get(encoded_offset):
            return cached  # ty:ignore[invalid-return-type]
        size = self.offset(encoded_offset-4).i32()
        if size % 4 != 0:
            raise Exception("Array size must be a multiple of 4")
        count = size // 4
        result = self.read_u32_multiple(count)
        self._obj_cache[encoded_offset] = result
        return result
