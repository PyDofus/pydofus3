from enum import IntEnum
from enum import IntFlag

class CommentHandling(IntEnum):
	Ignore = 0
	Load = 1

class DuplicatePropertyNameHandling(IntEnum):
	Replace = 0
	Ignore = 1
	Error = 2

class JTokenType(IntEnum):
	None_ = 0
	Object = 1
	Array = 2
	Constructor = 3
	Property = 4
	Comment = 5
	Integer = 6
	Float = 7
	String = 8
	Boolean = 9
	Null = 10
	Undefined = 11
	Date = 12
	Raw = 13
	Bytes = 14
	Guid = 15
	Uri = 16
	TimeSpan = 17

class LineInfoHandling(IntEnum):
	Ignore = 0
	Load = 1

class MergeArrayHandling(IntEnum):
	Concat = 0
	Union = 1
	Replace = 2
	Merge = 3

class MergeNullValueHandling(IntFlag):
	Ignore = 0
	Merge = 1

