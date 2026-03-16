from enum import IntEnum

class JsonContractType(IntEnum):
	None_ = 0
	Object = 1
	Array = 2
	Primitive = 3
	String = 4
	Dictionary = 5
	Dynamic = 6
	Serializable = 7
	Linq = 8

class JsonSerializerInternalReader:
	class PropertyPresence(IntEnum):
		None_ = 0
		Null = 1
		Value = 2

