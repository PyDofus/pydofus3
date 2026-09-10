from enum import IntEnum

class EventType(IntEnum):
	None_ = 0
	StreamStart = 1
	StreamEnd = 2
	DocumentStart = 3
	DocumentEnd = 4
	Alias = 5
	Scalar = 6
	SequenceStart = 7
	SequenceEnd = 8
	MappingStart = 9
	MappingEnd = 10
	Comment = 11

class MappingStyle(IntEnum):
	Any = 0
	Block = 1
	Flow = 2

class SequenceStyle(IntEnum):
	Any = 0
	Block = 1
	Flow = 2

