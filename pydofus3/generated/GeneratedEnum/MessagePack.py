from enum import IntEnum

class MessagePackCompression(IntEnum):
	None_ = 0
	Lz4Block = 1
	Lz4BlockArray = 2

class MessagePackCompression(IntEnum):
	None_ = 0
	Lz4Block = 1
	Lz4BlockArray = 2

class MessagePackType(IntEnum):
	Unknown = 0
	Integer = 1
	Nil = 2
	Boolean = 3
	Float = 4
	String = 5
	Binary = 6
	Array = 7
	Map = 8
	Extension = 9

class MessagePackType(IntEnum):
	Unknown = 0
	Integer = 1
	Nil = 2
	Boolean = 3
	Float = 4
	String = 5
	Binary = 6
	Array = 7
	Map = 8
	Extension = 9

class TinyJsonToken(IntEnum):
	None_ = 0
	StartObject = 1
	EndObject = 2
	StartArray = 3
	EndArray = 4
	Number = 5
	String = 6
	True = 7
	False = 8
	Null = 9

class TinyJsonToken(IntEnum):
	None_ = 0
	StartObject = 1
	EndObject = 2
	StartArray = 3
	EndArray = 4
	Number = 5
	String = 6
	True = 7
	False = 8
	Null = 9

class ValueType(IntEnum):
	Null = 0
	True = 1
	False = 2
	Double = 3
	Long = 4
	ULong = 5
	Decimal = 6
	String = 7

class ValueType(IntEnum):
	Null = 0
	True = 1
	False = 2
	Double = 3
	Long = 4
	ULong = 5
	Decimal = 6
	String = 7

