from enum import IntFlag

# Google.Protobuf.JsonToken
class JsonToken(IntFlag):
    Null = 0
    FALSE = 1
    TRUE = 2
    StringValue = 3
    Number = 4
    Name = 5
    StartObject = 6
    EndObject = 7
    StartArray = 8
    EndArray = 9
    EndDocument = 10

# Google.Protobuf.JsonTokenizer
class JsonTokenizer(IntFlag):
    Document = 0
    Object = 1
    Array = 2

# Google.Protobuf.JsonTokenizer
class JsonTokenizer(IntFlag):
    StartOfDocument = 1
    ExpectedEndOfDocument = 2
    ReaderExhausted = 4
    ObjectStart = 8
    ObjectBeforeColon = 16
    ObjectAfterColon = 32
    ObjectAfterProperty = 64
    ObjectAfterComma = 128
    ArrayStart = 256
    ArrayAfterValue = 512
    ArrayAfterComma = 1024

# Google.Protobuf.WireFormat
class WireFormat(IntFlag):
    Varint = 0
    Fixed64 = 1
    LengthDelimited = 2
    StartGroup = 3
    EndGroup = 4
    Fixed32 = 5

