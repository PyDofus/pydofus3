from enum import IntEnum
from enum import IntFlag

class ConstructorHandling(IntEnum):
	Default = 0
	AllowNonPublicDefaultConstructor = 1

class DateFormatHandling(IntEnum):
	IsoDateFormat = 0
	MicrosoftDateFormat = 1

class DateParseHandling(IntEnum):
	None_ = 0
	DateTime = 1
	DateTimeOffset = 2

class DateTimeZoneHandling(IntEnum):
	Local = 0
	Utc = 1
	Unspecified = 2
	RoundtripKind = 3

class DefaultValueHandling(IntFlag):
	Include = 0
	Ignore = 1
	Populate = 2
	IgnoreAndPopulate = 3

class FloatFormatHandling(IntEnum):
	String = 0
	Symbol = 1
	DefaultValue = 2

class FloatParseHandling(IntEnum):
	Double = 0
	Decimal = 1

class Formatting(IntEnum):
	None_ = 0
	Indented = 1

class JsonContainerType(IntEnum):
	None_ = 0
	Object = 1
	Array = 2
	Constructor = 3

class JsonReader:
	class State(IntEnum):
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

class JsonToken(IntEnum):
	None_ = 0
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

class JsonWriter:
	class State(IntEnum):
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

class MemberSerialization(IntEnum):
	OptOut = 0
	OptIn = 1
	Fields = 2

class MetadataPropertyHandling(IntEnum):
	Default = 0
	ReadAhead = 1
	Ignore = 2

class MissingMemberHandling(IntEnum):
	Ignore = 0
	Error = 1

class NullValueHandling(IntEnum):
	Include = 0
	Ignore = 1

class ObjectCreationHandling(IntEnum):
	Auto = 0
	Reuse = 1
	Replace = 2

class PreserveReferencesHandling(IntFlag):
	None_ = 0
	Objects = 1
	Arrays = 2
	All = 3

class ReadType(IntEnum):
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

class ReferenceLoopHandling(IntEnum):
	Error = 0
	Ignore = 1
	Serialize = 2

class Required(IntEnum):
	Default = 0
	AllowNull = 1
	Always = 2
	DisallowNull = 3

class StringEscapeHandling(IntEnum):
	Default = 0
	EscapeNonAscii = 1
	EscapeHtml = 2

class TypeNameAssemblyFormatHandling(IntEnum):
	Simple = 0
	Full = 1

class TypeNameHandling(IntFlag):
	None_ = 0
	Objects = 1
	Arrays = 2
	All = 3
	Auto = 4

class WriteState(IntEnum):
	Error = 0
	Closed = 1
	Object = 2
	Array = 3
	Constructor = 4
	Property = 5
	Start = 6

