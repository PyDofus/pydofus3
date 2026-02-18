from enum import IntFlag

# System.Text.Json.ConsumeNumberResult
class ConsumeNumberResult(IntFlag):
    Success = 0
    OperationIncomplete = 1
    NeedMoreData = 2

# System.Text.Json.ConsumeTokenResult
class ConsumeTokenResult(IntFlag):
    Success = 0
    NotEnoughDataRollBackState = 1
    IncompleteNoRollBackNecessary = 2

# System.Text.Json.ConverterStrategy
class ConverterStrategy(IntFlag):
    NONE = 0
    Object = 1
    Value = 2
    Enumerable = 8
    Dictionary = 16

# System.Text.Json.DataType
class DataType(IntFlag):
    Boolean = 0
    DateTime = 1
    DateTimeOffset = 2
    TimeSpan = 3
    Base64String = 4
    Guid = 5

# System.Text.Json.ExceptionResource
class ExceptionResource(IntFlag):
    ArrayDepthTooLarge = 0
    EndOfCommentNotFound = 1
    EndOfStringNotFound = 2
    RequiredDigitNotFoundAfterDecimal = 3
    RequiredDigitNotFoundAfterSign = 4
    RequiredDigitNotFoundEndOfData = 5
    ExpectedEndAfterSingleJson = 6
    ExpectedEndOfDigitNotFound = 7
    ExpectedFalse = 8
    ExpectedNextDigitEValueNotFound = 9
    ExpectedNull = 10
    ExpectedSeparatorAfterPropertyNameNotFound = 11
    ExpectedStartOfPropertyNotFound = 12
    ExpectedStartOfPropertyOrValueNotFound = 13
    ExpectedStartOfPropertyOrValueAfterComment = 14
    ExpectedStartOfValueNotFound = 15
    ExpectedTrue = 16
    ExpectedValueAfterPropertyNameNotFound = 17
    FoundInvalidCharacter = 18
    InvalidCharacterWithinString = 19
    InvalidCharacterAfterEscapeWithinString = 20
    InvalidHexCharacterWithinString = 21
    InvalidEndOfJsonNonPrimitive = 22
    MismatchedObjectArray = 23
    ObjectDepthTooLarge = 24
    ZeroDepthAtEnd = 25
    DepthTooLarge = 26
    CannotStartObjectArrayWithoutProperty = 27
    CannotStartObjectArrayAfterPrimitiveOrClose = 28
    CannotWriteValueWithinObject = 29
    CannotWriteValueAfterPrimitiveOrClose = 30
    CannotWritePropertyWithinArray = 31
    ExpectedJsonTokens = 32
    TrailingCommaNotAllowedBeforeArrayEnd = 33
    TrailingCommaNotAllowedBeforeObjectEnd = 34
    InvalidCharacterAtStartOfComment = 35
    UnexpectedEndOfDataWhileReadingComment = 36
    UnexpectedEndOfLineSeparator = 37
    ExpectedOneCompleteToken = 38
    NotEnoughData = 39
    InvalidLeadingZeroInNumber = 40

# System.Text.Json.JsonCommentHandling
class JsonCommentHandling(IntFlag):
    Disallow = 0
    Skip = 1
    Allow = 2

# System.Text.Json.JsonSerializerDefaults
class JsonSerializerDefaults(IntFlag):
    General = 0
    Web = 1

# System.Text.Json.JsonTokenType
class JsonTokenType(IntFlag):
    NONE = 0
    StartObject = 1
    EndObject = 2
    StartArray = 3
    EndArray = 4
    PropertyName = 5
    Comment = 6
    String = 7
    Number = 8
    TRUE = 9
    FALSE = 10
    Null = 11

# System.Text.Json.JsonValueKind
class JsonValueKind(IntFlag):
    Undefined = 0
    Object = 1
    Array = 2
    String = 3
    Number = 4
    TRUE = 5
    FALSE = 6
    Null = 7

# System.Text.Json.MetadataPropertyName
class MetadataPropertyName(IntFlag):
    NoMetadata = 0
    Values = 1
    Id = 2
    Ref = 3

# System.Text.Json.NumericType
class NumericType(IntFlag):
    Byte = 0
    SByte = 1
    Int16 = 2
    Int32 = 3
    Int64 = 4
    UInt16 = 5
    UInt32 = 6
    UInt64 = 7
    Single = 8
    Double = 9
    Decimal = 10

# System.Text.Json.StackFrameObjectState
class StackFrameObjectState(IntFlag):
    NONE = 0
    StartToken = 1
    ReadAheadNameOrEndObject = 2
    ReadNameOrEndObject = 3
    ReadAheadIdValue = 4
    ReadAheadRefValue = 5
    ReadIdValue = 6
    ReadRefValue = 7
    ReadAheadRefEndObject = 8
    ReadRefEndObject = 9
    ReadAheadValuesName = 10
    ReadValuesName = 11
    ReadAheadValuesStartArray = 12
    ReadValuesStartArray = 13
    PropertyValue = 14
    CreatedObject = 15
    ReadElements = 16
    EndToken = 17
    EndTokenValidation = 18

# System.Text.Json.StackFramePropertyState
class StackFramePropertyState(IntFlag):
    NONE = 0
    ReadName = 1
    Name = 2
    ReadValue = 3
    ReadValueIsEnd = 4
    TryRead = 5

