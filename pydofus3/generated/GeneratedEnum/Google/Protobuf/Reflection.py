from enum import IntEnum

class Edition(IntEnum):
	Unknown = 0
	_1TestOnly = 1
	_2TestOnly = 2
	Legacy = 900
	Proto2 = 998
	Proto3 = 999
	_2023 = 1000
	_2024 = 1001
	_99997TestOnly = 99997
	_99998TestOnly = 99998
	_99999TestOnly = 99999
	Max = 2147483647

class ExtensionRangeOptions:
	class Types:
		class VerificationState(IntEnum):
			Declaration = 0
			Unverified = 1

class FeatureSet:
	class Types:
		class FieldPresence(IntEnum):
			Unknown = 0
			Explicit = 1
			Implicit = 2
			LegacyRequired = 3

		class EnumType(IntEnum):
			Unknown = 0
			Open = 1
			Closed = 2

		class RepeatedFieldEncoding(IntEnum):
			Unknown = 0
			Packed = 1
			Expanded = 2

		class Utf8Validation(IntEnum):
			Unknown = 0
			Verify = 2
			None_ = 3

		class MessageEncoding(IntEnum):
			Unknown = 0
			LengthPrefixed = 1
			Delimited = 2

		class JsonFormat(IntEnum):
			Unknown = 0
			Allow = 1
			LegacyBestEffort = 2

class FieldDescriptorProto:
	class Types:
		class Type(IntEnum):
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

		class Label(IntEnum):
			Optional = 1
			Required = 2
			Repeated = 3

class FieldOptions:
	class Types:
		class CType(IntEnum):
			String = 0
			Cord = 1
			StringPiece = 2

		class JSType(IntEnum):
			JsNormal = 0
			JsString = 1
			JsNumber = 2

		class OptionRetention(IntEnum):
			RetentionUnknown = 0
			RetentionRuntime = 1
			RetentionSource = 2

		class OptionTargetType(IntEnum):
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

class FieldType(IntEnum):
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

class FileOptions:
	class Types:
		class OptimizeMode(IntEnum):
			Speed = 1
			CodeSize = 2
			LiteRuntime = 3

class GeneratedCodeInfo:
	class Types:
		class Annotation:
			class Types:
				class Semantic(IntEnum):
					None_ = 0
					Set = 1
					Alias = 2

class MethodOptions:
	class Types:
		class IdempotencyLevel(IntEnum):
			IdempotencyUnknown = 0
			NoSideEffects = 1
			Idempotent = 2

class ReflectionUtil:
	class SampleEnum(IntEnum):
		X = 0

class Syntax(IntEnum):
	Proto2 = 0
	Proto3 = 1
	Editions = 2
	Unknown = 3

