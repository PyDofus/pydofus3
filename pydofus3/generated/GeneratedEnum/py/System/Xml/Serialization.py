from enum import IntFlag

# System.Xml.Serialization.SchemaTypes
class SchemaTypes(IntFlag):
    NotSet = 0
    Primitive = 1
    Enum = 2
    Array = 3
    Class = 4
    XmlSerializable = 5
    XmlNode = 6
    Void = 7

# System.Xml.Serialization.SerializationFormat
class SerializationFormat(IntFlag):
    Encoded = 0
    Literal = 1

