from enum import IntFlag

# Newtonsoft.Json.ConstructorHandling
class ConstructorHandling(IntFlag):
    Default = 0
    AllowNonPublicDefaultConstructor = 1

# Newtonsoft.Json.DateFormatHandling
class DateFormatHandling(IntFlag):
    IsoDateFormat = 0
    MicrosoftDateFormat = 1

# Newtonsoft.Json.DateParseHandling
class DateParseHandling(IntFlag):
    NONE = 0
    DateTime = 1
    DateTimeOffset = 2

# Newtonsoft.Json.DateTimeZoneHandling
class DateTimeZoneHandling(IntFlag):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

# Newtonsoft.Json.DefaultValueHandling
class DefaultValueHandling(IntFlag):
    Include = 0
    Ignore = 1
    Populate = 2
    IgnoreAndPopulate = 3

# Newtonsoft.Json.FloatFormatHandling
class FloatFormatHandling(IntFlag):
    String = 0
    Symbol = 1
    DefaultValue = 2

# Newtonsoft.Json.FloatParseHandling
class FloatParseHandling(IntFlag):
    Double = 0
    Decimal = 1

# Newtonsoft.Json.Formatting
class Formatting(IntFlag):
    NONE = 0
    Indented = 1

# Newtonsoft.Json.JsonContainerType
class JsonContainerType(IntFlag):
    NONE = 0
    Object = 1
    Array = 2
    Constructor = 3

# Newtonsoft.Json.JsonReader
class JsonReader(IntFlag):
    Start = 0
    Complete = 1
    Property = 2
    ObjectStart = 3
    Object = 4
    ArrayStart = 5
    Array = 6
    Closed = 7
    PostValue = 8
    ConstructorStart = 9
    Constructor = 10
    Error = 11
    Finished = 12

# Newtonsoft.Json.JsonToken
class JsonToken(IntFlag):
    NONE = 0
    StartObject = 1
    StartArray = 2
    StartConstructor = 3
    PropertyName = 4
    Comment = 5
    Raw = 6
    Integer = 7
    Float = 8
    String = 9
    Boolean = 10
    Null = 11
    Undefined = 12
    EndObject = 13
    EndArray = 14
    EndConstructor = 15
    Date = 16
    Bytes = 17

# Newtonsoft.Json.JsonWriter
class JsonWriter(IntFlag):
    Start = 0
    Property = 1
    ObjectStart = 2
    Object = 3
    ArrayStart = 4
    Array = 5
    ConstructorStart = 6
    Constructor = 7
    Closed = 8
    Error = 9

# Newtonsoft.Json.MemberSerialization
class MemberSerialization(IntFlag):
    OptOut = 0
    OptIn = 1
    Fields = 2

# Newtonsoft.Json.MetadataPropertyHandling
class MetadataPropertyHandling(IntFlag):
    Default = 0
    ReadAhead = 1
    Ignore = 2

# Newtonsoft.Json.MissingMemberHandling
class MissingMemberHandling(IntFlag):
    Ignore = 0
    Error = 1

# Newtonsoft.Json.NullValueHandling
class NullValueHandling(IntFlag):
    Include = 0
    Ignore = 1

# Newtonsoft.Json.ObjectCreationHandling
class ObjectCreationHandling(IntFlag):
    Auto = 0
    Reuse = 1
    Replace = 2

# Newtonsoft.Json.PreserveReferencesHandling
class PreserveReferencesHandling(IntFlag):
    NONE = 0
    Objects = 1
    Arrays = 2
    All = 3

# Newtonsoft.Json.ReadType
class ReadType(IntFlag):
    Read = 0
    ReadAsInt32 = 1
    ReadAsInt64 = 2
    ReadAsBytes = 3
    ReadAsString = 4
    ReadAsDecimal = 5
    ReadAsDateTime = 6
    ReadAsDateTimeOffset = 7
    ReadAsDouble = 8
    ReadAsBoolean = 9

# Newtonsoft.Json.ReferenceLoopHandling
class ReferenceLoopHandling(IntFlag):
    Error = 0
    Ignore = 1
    Serialize = 2

# Newtonsoft.Json.Required
class Required(IntFlag):
    Default = 0
    AllowNull = 1
    Always = 2
    DisallowNull = 3

# Newtonsoft.Json.StringEscapeHandling
class StringEscapeHandling(IntFlag):
    Default = 0
    EscapeNonAscii = 1
    EscapeHtml = 2

# Newtonsoft.Json.TypeNameAssemblyFormatHandling
class TypeNameAssemblyFormatHandling(IntFlag):
    Simple = 0
    Full = 1

# Newtonsoft.Json.TypeNameHandling
class TypeNameHandling(IntFlag):
    NONE = 0
    Objects = 1
    Arrays = 2
    All = 3
    Auto = 4

# Newtonsoft.Json.WriteState
class WriteState(IntFlag):
    Error = 0
    Closed = 1
    Object = 2
    Array = 3
    Constructor = 4
    Property = 5
    Start = 6

