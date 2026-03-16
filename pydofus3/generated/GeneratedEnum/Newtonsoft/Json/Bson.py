from enum import IntEnum

class BsonBinaryType(IntEnum):
	Binary = 0
	Function = 1
	BinaryOld = 2
	UuidOld = 3
	Uuid = 4
	Md5 = 5
	UserDefined = 128

class BsonReader:
	class BsonReaderState(IntEnum):
		Normal = 0
		ReferenceStart = 1
		ReferenceRef = 2
		ReferenceId = 3
		CodeWScopeStart = 4
		CodeWScopeCode = 5
		CodeWScopeScope = 6
		CodeWScopeScopeObject = 7
		CodeWScopeScopeEnd = 8

class BsonType(IntEnum):
	Number = 1
	String = 2
	Object = 3
	Array = 4
	Binary = 5
	Undefined = 6
	Oid = 7
	Boolean = 8
	Date = 9
	Null = 10
	Regex = 11
	Reference = 12
	Code = 13
	Symbol = 14
	CodeWScope = 15
	Integer = 16
	TimeStamp = 17
	Long = 18
	MaxKey = 127
	MinKey = 255

