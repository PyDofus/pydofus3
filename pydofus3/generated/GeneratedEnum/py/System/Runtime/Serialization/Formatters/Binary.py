from enum import IntFlag

# System.Runtime.Serialization.Formatters.Binary.BinaryArrayTypeEnum
class BinaryArrayTypeEnum(IntFlag):
    Single = 0
    Jagged = 1
    Rectangular = 2
    SingleOffset = 3
    JaggedOffset = 4
    RectangularOffset = 5

# System.Runtime.Serialization.Formatters.Binary.BinaryHeaderEnum
class BinaryHeaderEnum(IntFlag):
    SerializedStreamHeader = 0
    Object = 1
    ObjectWithMap = 2
    ObjectWithMapAssemId = 3
    ObjectWithMapTyped = 4
    ObjectWithMapTypedAssemId = 5
    ObjectString = 6
    Array = 7
    MemberPrimitiveTyped = 8
    MemberReference = 9
    ObjectNull = 10
    MessageEnd = 11
    Assembly = 12
    ObjectNullMultiple256 = 13
    ObjectNullMultiple = 14
    ArraySinglePrimitive = 15
    ArraySingleObject = 16
    ArraySingleString = 17
    CrossAppDomainMap = 18
    CrossAppDomainString = 19
    CrossAppDomainAssembly = 20
    MethodCall = 21
    MethodReturn = 22

# System.Runtime.Serialization.Formatters.Binary.BinaryTypeEnum
class BinaryTypeEnum(IntFlag):
    Primitive = 0
    String = 1
    Object = 2
    ObjectUrt = 3
    ObjectUser = 4
    ObjectArray = 5
    StringArray = 6
    PrimitiveArray = 7

# System.Runtime.Serialization.Formatters.Binary.InternalArrayTypeE
class InternalArrayTypeE(IntFlag):
    Empty = 0
    Single = 1
    Jagged = 2
    Rectangular = 3
    Base64 = 4

# System.Runtime.Serialization.Formatters.Binary.InternalMemberTypeE
class InternalMemberTypeE(IntFlag):
    Empty = 0
    Header = 1
    Field = 2
    Item = 3

# System.Runtime.Serialization.Formatters.Binary.InternalMemberValueE
class InternalMemberValueE(IntFlag):
    Empty = 0
    InlineValue = 1
    Nested = 2
    Reference = 3
    Null = 4

# System.Runtime.Serialization.Formatters.Binary.InternalObjectPositionE
class InternalObjectPositionE(IntFlag):
    Empty = 0
    Top = 1
    Child = 2
    Headers = 3

# System.Runtime.Serialization.Formatters.Binary.InternalObjectTypeE
class InternalObjectTypeE(IntFlag):
    Empty = 0
    Object = 1
    Array = 2

# System.Runtime.Serialization.Formatters.Binary.InternalParseTypeE
class InternalParseTypeE(IntFlag):
    Empty = 0
    SerializedStreamHeader = 1
    Object = 2
    Member = 3
    ObjectEnd = 4
    MemberEnd = 5
    Headers = 6
    HeadersEnd = 7
    SerializedStreamHeaderEnd = 8
    Envelope = 9
    EnvelopeEnd = 10
    Body = 11
    BodyEnd = 12

# System.Runtime.Serialization.Formatters.Binary.InternalPrimitiveTypeE
class InternalPrimitiveTypeE(IntFlag):
    Invalid = 0
    Boolean = 1
    Byte = 2
    Char = 3
    Currency = 4
    Decimal = 5
    Double = 6
    Int16 = 7
    Int32 = 8
    Int64 = 9
    SByte = 10
    Single = 11
    TimeSpan = 12
    DateTime = 13
    UInt16 = 14
    UInt32 = 15
    UInt64 = 16
    Null = 17
    String = 18

# System.Runtime.Serialization.Formatters.Binary.InternalSerializerTypeE
class InternalSerializerTypeE(IntFlag):
    Soap = 1
    Binary = 2

# System.Runtime.Serialization.Formatters.Binary.MessageEnum
class MessageEnum(IntFlag):
    NoArgs = 1
    ArgsInline = 2
    ArgsIsArray = 4
    ArgsInArray = 8
    NoContext = 16
    ContextInline = 32
    ContextInArray = 64
    MethodSignatureInArray = 128
    PropertyInArray = 256
    NoReturnValue = 512
    ReturnValueVoid = 1024
    ReturnValueInline = 2048
    ReturnValueInArray = 4096
    ExceptionInArray = 8192
    GenericMethod = 32768

# System.Runtime.Serialization.Formatters.Binary.ValueFixupEnum
class ValueFixupEnum(IntFlag):
    Empty = 0
    Array = 1
    Header = 2
    Member = 3

