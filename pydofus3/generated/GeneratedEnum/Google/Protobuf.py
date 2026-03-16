from enum import IntEnum
from enum import IntFlag

class JsonToken:
	class TokenType(IntEnum):
		Null = 0
		False = 1
		True = 2
		StringValue = 3
		Number = 4
		Name = 5
		StartObject = 6
		EndObject = 7
		StartArray = 8
		EndArray = 9
		EndDocument = 10

class JsonTokenizer:
	class JsonTextTokenizer:
		class ContainerType(IntEnum):
			Document = 0
			Object = 1
			Array = 2

		class State(IntFlag):
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

class WireFormat:
	class WireType(IntEnum):
		Varint = 0
		Fixed64 = 1
		LengthDelimited = 2
		StartGroup = 3
		EndGroup = 4
		Fixed32 = 5

