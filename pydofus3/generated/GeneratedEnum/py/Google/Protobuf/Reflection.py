from enum import IntFlag

# Google.Protobuf.Reflection.Edition
class Edition(IntFlag):
    Unknown = 0
    Legacy = 900
    Proto2 = 998
    Proto3 = 999
    _2023 = 1000
    _2024 = 1001
    _1TestOnly = 1
    _2TestOnly = 2
    _99997TestOnly = 99997
    _99998TestOnly = 99998
    _99999TestOnly = 99999
    Max = 2147483647

# Google.Protobuf.Reflection.ExtensionRangeOptions
class ExtensionRangeOptions(IntFlag):
    Declaration = 0
    Unverified = 1

# Google.Protobuf.Reflection.FeatureSet
class FeatureSet(IntFlag):
    Unknown = 0
    Explicit = 1
    Implicit = 2
    LegacyRequired = 3

# Google.Protobuf.Reflection.FeatureSet
class FeatureSet(IntFlag):
    Unknown = 0
    Open = 1
    Closed = 2

# Google.Protobuf.Reflection.FeatureSet
class FeatureSet(IntFlag):
    Unknown = 0
    Packed = 1
    Expanded = 2

# Google.Protobuf.Reflection.FeatureSet
class FeatureSet(IntFlag):
    Unknown = 0
    Verify = 2
    NONE = 3

# Google.Protobuf.Reflection.FeatureSet
class FeatureSet(IntFlag):
    Unknown = 0
    LengthPrefixed = 1
    Delimited = 2

# Google.Protobuf.Reflection.FeatureSet
class FeatureSet(IntFlag):
    Unknown = 0
    Allow = 1
    LegacyBestEffort = 2

# Google.Protobuf.Reflection.FieldDescriptorProto
class FieldDescriptorProto(IntFlag):
    Double = 1
    Float = 2
    Int64 = 3
    Uint64 = 4
    Int32 = 5
    Fixed64 = 6
    Fixed32 = 7
    Bool = 8
    String = 9
    Group = 10
    Message = 11
    Bytes = 12
    Uint32 = 13
    Enum = 14
    Sfixed32 = 15
    Sfixed64 = 16
    Sint32 = 17
    Sint64 = 18

# Google.Protobuf.Reflection.FieldDescriptorProto
class FieldDescriptorProto(IntFlag):
    Optional = 1
    Repeated = 3
    Required = 2

# Google.Protobuf.Reflection.FieldOptions
class FieldOptions(IntFlag):
    String = 0
    Cord = 1
    StringPiece = 2

# Google.Protobuf.Reflection.FieldOptions
class FieldOptions(IntFlag):
    JsNormal = 0
    JsString = 1
    JsNumber = 2

# Google.Protobuf.Reflection.FieldOptions
class FieldOptions(IntFlag):
    RetentionUnknown = 0
    RetentionRuntime = 1
    RetentionSource = 2

# Google.Protobuf.Reflection.FieldOptions
class FieldOptions(IntFlag):
    TargetTypeUnknown = 0
    TargetTypeFile = 1
    TargetTypeExtensionRange = 2
    TargetTypeMessage = 3
    TargetTypeField = 4
    TargetTypeOneof = 5
    TargetTypeEnum = 6
    TargetTypeEnumEntry = 7
    TargetTypeService = 8
    TargetTypeMethod = 9

# Google.Protobuf.Reflection.FieldType
class FieldType(IntFlag):
    Double = 0
    Float = 1
    Int64 = 2
    UInt64 = 3
    Int32 = 4
    Fixed64 = 5
    Fixed32 = 6
    Bool = 7
    String = 8
    Group = 9
    Message = 10
    Bytes = 11
    UInt32 = 12
    SFixed32 = 13
    SFixed64 = 14
    SInt32 = 15
    SInt64 = 16
    Enum = 17

# Google.Protobuf.Reflection.FileOptions
class FileOptions(IntFlag):
    Speed = 1
    CodeSize = 2
    LiteRuntime = 3

# Google.Protobuf.Reflection.GeneratedCodeInfo
class GeneratedCodeInfo(IntFlag):
    NONE = 0
    Set = 1
    Alias = 2

# Google.Protobuf.Reflection.MethodOptions
class MethodOptions(IntFlag):
    IdempotencyUnknown = 0
    NoSideEffects = 1
    Idempotent = 2

# Google.Protobuf.Reflection.ReflectionUtil
class ReflectionUtil(IntFlag):
    X = 0

# Google.Protobuf.Reflection.Syntax
class Syntax(IntFlag):
    Proto2 = 0
    Proto3 = 1
    Editions = 2
    Unknown = 3

