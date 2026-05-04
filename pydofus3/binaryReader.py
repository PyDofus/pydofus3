import base64
import codecs
import io
from io import SEEK_CUR, SEEK_END
from struct import Struct, unpack
from typing import BinaryIO, Protocol, Self

import numpy as np
import numpy.typing as npt


class Readable(Protocol):
    @classmethod
    def read[K:BinaryReader](cls, reader: K) -> Self: ...

class BinaryReader:
    def __init__(self, stream: BinaryIO | bytes | bytearray, big_endian: bool = False):
        if isinstance(stream, (bytes, bytearray)):
            self._stream = io.BytesIO(stream)
        else:
            self._stream = stream
            self._stream.seek(0)

        self._format_head = '>' if big_endian else '<'
        self._set_struct()

    def _set_struct(self):
        self._i8 = Struct(f'{self._format_head}b')
        self._u8 = Struct(f'{self._format_head}B')
        self._i16 = Struct(f'{self._format_head}h')
        self._u16 = Struct(f'{self._format_head}H')
        self._i32 = Struct(f'{self._format_head}i')
        self._u32 = Struct(f'{self._format_head}I')
        self._i64 = Struct(f'{self._format_head}q')
        self._u64 = Struct(f'{self._format_head}Q')
        self._f32 = Struct(f'{self._format_head}f')
        self._f64 = Struct(f'{self._format_head}d')

    @property
    def pos(self) -> int:
        return self._stream.tell()

    @pos.setter
    def pos(self, new_pos: int):
        if new_pos >= 0:
            self._stream.seek(new_pos)
        else:
            self._stream.seek(-new_pos, SEEK_END)

    def __len__(self) -> int:
        pos = self._stream.tell()
        place = self._stream.seek(0, SEEK_END)
        self._stream.seek(pos)
        return place

    @property
    def big_endian(self) -> bool:
        return self._format_head == '>'

    @big_endian.setter
    def big_endian(self, big_endian: bool):
        new_format = '>' if big_endian else '<'
        if new_format != self._format_head:
            self._format_head = new_format
            self._set_struct()

    def offset(self, offset: int) -> 'BinaryReader':
        self._stream.seek(offset)
        return self

    def skip(self, count: int) -> 'BinaryReader':
        self._stream.seek(count, SEEK_CUR)
        return self

    def align(self, alignment: int):
        misalignment = self._stream.tell() % alignment
        if misalignment:
            self._stream.seek(alignment - misalignment, SEEK_CUR)

    def read(self, count: int) -> bytes:
        return self._stream.read(count)

    # read 1

    def read_str(self, length: int, encoding: str = 'utf-8') -> str:
        return self._stream.read(length).decode(encoding=encoding)

    def str_null(self) -> 'str':
        bytes_array = bytearray()
        while True:
            b = self.read(1)
            if b == b'\x00':
                break
            bytes_array += b
        try:
            value = bytes_array.decode()
        except UnicodeDecodeError:
            value = base64.b64encode(bytes(bytes_array)).decode()
        return value

    def read_char(self, encoding='utf-8') -> str:
        decoder = codecs.getincrementaldecoder(encoding)()
        char = ''
        while not char:
            byte = self._stream.read(1)
            if not byte:
                raise EOFError('End of stream reached before character could be decoded.')
            char = decoder.decode(byte)
        return char

    def read_varint(self) -> int:
        shift = 0
        result = 0
        while True:
            byte = self.read(1)[0]
            result |= (byte & 0x7F) << shift
            if (byte & 0x80) == 0:
                break
            shift += 7
        return result

    def compressed_uint32(self) -> int:
        read = self.read(1)[0]
        if (read & 0x80) == 0:
            return read
        elif (read & 0xC0) == 0x80:
            return ((read & ~0x80) << 8) | self.read(1)[0]
        elif (read & 0xE0) == 0xC0:
            r1 = self.read(1)[0]
            r2 = self.read(1)[0]
            r3 = self.read(1)[0]
            return ((read & ~0xC0) << 24) | (r1 << 16) | (r2 << 8) | r3
        elif read == 0xF0:
            return self.u32()
        elif read == 0xFE:
            return 0xFFFFFFFF - 1
        elif read == 0xFF:
            return 0xFFFFFFFF
        else:
            raise Exception('Invalid compressed integer format')

    def compressed_int32(self) -> int:
        encoded = self.compressed_uint32()
        if encoded == 0xFFFFFFFF:
            return -0x80000000
        is_negative = (encoded & 1) != 0
        encoded >>= 1

        if is_negative:
            return -(encoded + 1)
        return encoded

    def read_bool(self) -> bool:
        return bool(self._stream.read(1)[0])

    def byte(self) -> int:
        return self.read(1)[0]

    def i32(self) -> int:
        return self._i32.unpack(self._stream.read(4))[0]

    def u32(self) -> int:
        return self._u32.unpack(self._stream.read(4))[0]

    def i16(self) -> int:
        return self._i16.unpack(self._stream.read(2))[0]

    def u16(self) -> int:
        return self._u16.unpack(self._stream.read(2))[0]

    def i8(self) -> int:
        return self._i8.unpack(self._stream.read(1))[0]

    def u8(self) -> int:
        return self._u8.unpack(self._stream.read(1))[0]

    def i64(self) -> int:
        return self._i64.unpack(self._stream.read(8))[0]

    def u64(self) -> int:
        return self._u64.unpack(self._stream.read(8))[0]

    def f32(self) -> float:
        return self._f32.unpack(self._stream.read(4))[0]

    def f64(self) -> float:
        return self._f64.unpack(self._stream.read(8))[0]

    def read_rgba(self) -> tuple[float, float, float, float]:
        return self.i8() / 127, self.i8() / 127, self.i8() / 127, self.i8() / 127

    def read_struct(self, struct: Struct) -> tuple:
        return struct.unpack(self.read(struct.size))

    # read multiple
    def read_i32_multiple(self, number: int) -> tuple[int, ...]:
        return unpack(f'{self._format_head}{number}i', self._stream.read(4 * number))

    def read_u32_multiple(self, number: int) -> tuple[int, ...]:
        return unpack(f'{self._format_head}{number}I', self._stream.read(4 * number))

    def read_i16_multiple(self, number: int) -> tuple[int, ...]:
        return unpack(f'{self._format_head}{number}h', self._stream.read(2 * number))

    def read_u16_multiple(self, number: int) -> tuple[int, ...]:
        return unpack(f'{self._format_head}{number}H', self._stream.read(2 * number))

    def read_i8_multiple(self, number: int) -> tuple[int, ...]:
        return unpack(f'{self._format_head}{number}b', self._stream.read(number))

    def read_u8_multiple(self, number: int) -> tuple[int, ...]:
        return unpack(f'{self._format_head}{number}B', self._stream.read(number))

    def read_i64_multiple(self, number: int) -> tuple[int, ...]:
        return unpack(f'{self._format_head}{number}q', self._stream.read(8 * number))

    def read_u64_multiple(self, number: int) -> tuple[int, ...]:
        return unpack(f'{self._format_head}{number}Q', self._stream.read(8 * number))

    def read_f32_multiple(self, number: int) -> tuple[float, ...]:
        return unpack(f'{self._format_head}{number}f', self._stream.read(4 * number))

    def read_f64_multiple(self, number: int) -> tuple[float, ...]:
        return unpack(f'{self._format_head}{number}d', self._stream.read(8 * number))

    def read_bool_multiple(self, number: int) -> tuple['bool', ...]:
        return unpack(f'{self._format_head}{number}?', self._stream.read(number))

    # numpy

    def read_i32_array(self, number: int) -> npt.NDArray[np.int32]:
        return np.frombuffer(self._stream.read(4 * number), f'{self._format_head}i')

    def read_u32_array(self, number: int) -> npt.NDArray[np.uint32]:
        return np.frombuffer(self._stream.read(4 * number), f'{self._format_head}I')

    def read_i16_array(self, number: int) -> npt.NDArray[np.int16]:
        return np.frombuffer(self._stream.read(2 * number), f'{self._format_head}h')

    def read_u16_array(self, number: int) -> npt.NDArray[np.uint16]:
        return np.frombuffer(self._stream.read(2 * number), f'{self._format_head}H')

    def read_i8_array(self, number: int) -> npt.NDArray[np.int8]:
        return np.frombuffer(self._stream.read(number), f'{self._format_head}b')

    def read_u8_array(self, number: int) -> npt.NDArray[np.uint8]:
        return np.frombuffer(self._stream.read(number), f'{self._format_head}B')

    def read_i64_array(self, number: int) -> npt.NDArray[np.int64]:
        return np.frombuffer(self._stream.read(8 * number), f'{self._format_head}q')

    def read_u64_array(self, number: int) -> npt.NDArray[np.uint64]:
        return np.frombuffer(self._stream.read(8 * number), f'{self._format_head}Q')

    def read_f32_array(self, number: int) -> npt.NDArray[np.float32]:
        return np.frombuffer(self._stream.read(4 * number), f'{self._format_head}f')

    def read_f64_array(self, number: int) -> npt.NDArray[np.float64]:
        return np.frombuffer(self._stream.read(8 * number), f'{self._format_head}d')

    def read_bool_array(self, number: int) -> npt.NDArray[np.bool_]:
        return np.frombuffer(self._stream.read(number), f'{self._format_head}?')

    def read_dtype_array[T: np.generic](self, number: int, dtype: np.dtype[T]) -> npt.NDArray[T]:
        return np.frombuffer(self._stream.read(dtype.itemsize * number), dtype)

    def read_class[T:Readable](self, class_: type[T]) -> T:
        return class_.read(self)

    def read_class_multiple[T:Readable](self, class_: type[T], number: int) -> list[T]:
        return [class_.read(self) for _ in range(number)]

    def read_class_size[T:Readable](self, class_: type[T], offset:int, size: int, ) -> list[T]:
        result = []
        self.pos = offset
        end = offset + size
        while self.pos < end:
            result.append(class_.read(self))
        return result
