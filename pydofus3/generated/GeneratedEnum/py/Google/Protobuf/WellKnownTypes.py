from enum import IntFlag

# Google.Protobuf.WellKnownTypes.Field
class Field(IntFlag):
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

# Google.Protobuf.WellKnownTypes.Field
class Field(IntFlag):
    Unknown = 0
    Optional = 1
    Required = 2
    Repeated = 3

# Google.Protobuf.WellKnownTypes.NullValue
class NullValue(IntFlag):
    NullValue = 0

# Google.Protobuf.WellKnownTypes.Syntax
class Syntax(IntFlag):
    Proto2 = 0
    Proto3 = 1
    Editions = 2

# Google.Protobuf.WellKnownTypes.Value
class Value(IntFlag):
    NONE = 0
    NullValue = 1
    NumberValue = 2
    StringValue = 3
    BoolValue = 4
    StructValue = 5
    ListValue = 6

