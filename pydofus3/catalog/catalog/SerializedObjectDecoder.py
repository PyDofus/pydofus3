from enum import StrEnum
from typing import Callable, ClassVar

from pydofus3.binaryReader import BinaryReader
from pydofus3.catalog.binary.CatalogBinaryReader import CatalogBinaryReader
from pydofus3.catalog.classes import AssetBundleRequestOptions, AssetBundleRequestOptionsAdapter

from .ClassJsonObject import ClassJsonObject
from .SerializedType import SerializedType
from .WrappedSerializedObject import WrappedSerializedObject

type DecodedObject = str | int | WrappedSerializedObject | ClassJsonObject | None
type DecoderFunction = Callable[[BinaryReader], DecodedObject]
type DecoderFunctionV2 = Callable[[CatalogBinaryReader, int, SerializedType, bool], DecodedObject]


class MatchName(StrEnum):
    ABRO_MATCHNAME = 'Unity.ResourceManager; UnityEngine.ResourceManagement.ResourceProviders.AssetBundleRequestOptions'
    INT_MATCHNAME = 'mscorlib; System.Int32'
    LONG_MATCHNAME = 'mscorlib; System.Int64'
    BOOL_MATCHNAME = 'mscorlib; System.Boolean'
    STRING_MATCHNAME = 'mscorlib; System.String'
    HASH128_MATCHNAME = 'mscorlib; System.UnityEngine.Hash128'


class DecodeV1Method:
    @staticmethod
    def read_ascii_string_u32(reader: BinaryReader):
        return reader.read_str(reader.u32(), 'ascii')

    @staticmethod
    def read_unicode_string_u32(reader: BinaryReader):
        return reader.read_str(reader.u32(), 'utf-16')

    @staticmethod
    def read_u16(reader: BinaryReader):
        return reader.u16()

    @staticmethod
    def read_u32(reader: BinaryReader):
        return reader.u32()

    @staticmethod
    def read_i32(reader: BinaryReader):
        return reader.i32()

    @staticmethod
    def read_ascii_string_u8(reader: BinaryReader):
        return reader.read_str(reader.u8(), 'ascii')

    @staticmethod
    def read_json_object(reader: BinaryReader):
        json_obj = ClassJsonObject.read(reader)
        if json_obj.Type.get_match_name() == MatchName.ABRO_MATCHNAME:
            obj = AssetBundleRequestOptionsAdapter.validate_json(json_obj.JsonText)
            return WrappedSerializedObject(json_obj.Type, obj)
        return json_obj


class DecodeV2Method:
    @staticmethod
    def read_int(reader: CatalogBinaryReader, offset: int, _: SerializedType, is_default: bool):
        if is_default:
            return 0
        return reader.offset(offset).i32()

    @staticmethod
    def read_long(reader: CatalogBinaryReader, offset: int, _: SerializedType, is_default: bool):
        if is_default:
            return 0
        return reader.offset(offset).i64()

    @staticmethod
    def read_bool(reader: CatalogBinaryReader, offset: int, _: SerializedType, is_default: bool):
        if is_default:
            return False
        return reader.offset(offset).read_bool()

    @staticmethod
    def read_string(reader: CatalogBinaryReader, offset: int, _: SerializedType, is_default: bool):
        if is_default:
            return ''
        str_offset = reader.offset(offset).u32()
        separator = reader.read_char()
        return reader.read_encoded_string(str_offset, separator)

    @staticmethod
    def read_hash128(reader: CatalogBinaryReader, offset: int, _: SerializedType, is_default: bool):
        if is_default:
            return ''
        return reader.offset(offset).read(16).hex()

    @staticmethod
    def read_abro(reader: CatalogBinaryReader, offset: int, serialized_type: SerializedType, is_default: bool):
        if is_default:
            return None
        obj = AssetBundleRequestOptions.read(reader, offset)
        return WrappedSerializedObject(serialized_type, obj)


class SerializedObjectDecoder:
    dispatchV1: ClassVar[dict[int, DecoderFunction]] = {
        0: DecodeV1Method.read_ascii_string_u32,
        1: DecodeV1Method.read_unicode_string_u32,
        2: DecodeV1Method.read_u16,
        3: DecodeV1Method.read_u32,
        4: DecodeV1Method.read_i32,
        5: DecodeV1Method.read_ascii_string_u8,
        6: DecodeV1Method.read_ascii_string_u8,
        7: DecodeV1Method.read_json_object,
    }

    @classmethod
    def decode_v1(cls, reader: BinaryReader, offset: int) -> DecodedObject:
        obj_type = reader.offset(offset).u8()
        try:
            return cls.dispatchV1[obj_type](reader)
        except KeyError:
            raise RuntimeError(f'type {obj_type} not supported now.')

    dispatchV2: ClassVar[dict[str, DecoderFunctionV2]] = {
        MatchName.INT_MATCHNAME: DecodeV2Method.read_int,
        MatchName.LONG_MATCHNAME: DecodeV2Method.read_long,
        MatchName.BOOL_MATCHNAME: DecodeV2Method.read_bool,
        MatchName.STRING_MATCHNAME: DecodeV2Method.read_string,
        MatchName.HASH128_MATCHNAME: DecodeV2Method.read_hash128,
        MatchName.ABRO_MATCHNAME: DecodeV2Method.read_abro,
    }

    @classmethod
    def decode_v2(cls, reader: CatalogBinaryReader, offset: int) -> DecodedObject:
        if offset == 0xFFFFFFFF:
            return None

        type_name_offset, object_offset = reader.offset(offset).read_u32_multiple(2)

        is_default = object_offset == 0xFFFFFFFF
        serialized_type = SerializedType.read(reader, type_name_offset)
        match_name = serialized_type.get_match_name()

        try:
            result = cls.dispatchV2[match_name](reader, object_offset, serialized_type, is_default)
            return result
        except KeyError:
            raise RuntimeError(f'type {match_name} not supported now.')
