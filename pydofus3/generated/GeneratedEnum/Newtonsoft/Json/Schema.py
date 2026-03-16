from enum import IntEnum
from enum import IntFlag

class JsonSchemaType(IntFlag):
	None_ = 0
	String = 1
	Float = 2
	Integer = 4
	Boolean = 8
	Object = 16
	Array = 32
	Null = 64
	Any = 127

class UndefinedSchemaIdHandling(IntEnum):
	None_ = 0
	UseTypeName = 1
	UseAssemblyQualifiedName = 2

