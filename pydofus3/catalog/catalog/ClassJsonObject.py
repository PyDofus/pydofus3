from dataclasses import dataclass

from pydofus3.binaryReader import BinaryReader

from .SerializedType import SerializedType


@dataclass
class ClassJsonObject:
    Type: SerializedType
    JsonText: str

    @staticmethod
    def read(reader: BinaryReader) -> "ClassJsonObject":
        return ClassJsonObject(SerializedType.read(reader), reader.read_str(reader.i32(), "utf-16"))
