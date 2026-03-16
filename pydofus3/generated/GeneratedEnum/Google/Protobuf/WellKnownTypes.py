from enum import IntEnum

class Field:
	class Types:
		class Kind(IntEnum):
			TypeUnknown = 0
			TypeDouble = 1
			TypeFloat = 2
			TypeInt64 = 3
			TypeUint64 = 4
			TypeInt32 = 5
			TypeFixed64 = 6
			TypeFixed32 = 7
			TypeBool = 8
			TypeString = 9
			TypeGroup = 10
			TypeMessage = 11
			TypeBytes = 12
			TypeUint32 = 13
			TypeEnum = 14
			TypeSfixed32 = 15
			TypeSfixed64 = 16
			TypeSint32 = 17
			TypeSint64 = 18

		class Cardinality(IntEnum):
			Unknown = 0
			Optional = 1
			Required = 2
			Repeated = 3

class NullValue(IntEnum):
	NullValue = 0

class Syntax(IntEnum):
	Proto2 = 0
	Proto3 = 1
	Editions = 2

class Value:
	class KindOneofCase(IntEnum):
		None_ = 0
		NullValue = 1
		NumberValue = 2
		StringValue = 3
		BoolValue = 4
		StructValue = 5
		ListValue = 6

