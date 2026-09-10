from enum import IntEnum

class EmitterState(IntEnum):
	StreamStart = 0
	StreamEnd = 1
	FirstDocumentStart = 2
	DocumentStart = 3
	DocumentContent = 4
	DocumentEnd = 5
	FlowSequenceFirstItem = 6
	FlowSequenceItem = 7
	FlowMappingFirstKey = 8
	FlowMappingKey = 9
	FlowMappingSimpleValue = 10
	FlowMappingValue = 11
	BlockSequenceFirstItem = 12
	BlockSequenceItem = 13
	BlockMappingFirstKey = 14
	BlockMappingKey = 15
	BlockMappingSimpleValue = 16
	BlockMappingValue = 17

class ParserState(IntEnum):
	StreamStart = 0
	StreamEnd = 1
	ImplicitDocumentStart = 2
	DocumentStart = 3
	DocumentContent = 4
	DocumentEnd = 5
	BlockNode = 6
	BlockNodeOrIndentlessSequence = 7
	FlowNode = 8
	BlockSequenceFirstEntry = 9
	BlockSequenceEntry = 10
	IndentlessSequenceEntry = 11
	BlockMappingFirstKey = 12
	BlockMappingKey = 13
	BlockMappingValue = 14
	FlowSequenceFirstEntry = 15
	FlowSequenceEntry = 16
	FlowSequenceEntryMappingKey = 17
	FlowSequenceEntryMappingValue = 18
	FlowSequenceEntryMappingEnd = 19
	FlowMappingFirstKey = 20
	FlowMappingKey = 21
	FlowMappingValue = 22
	FlowMappingEmptyValue = 23

class ScalarStyle(IntEnum):
	Any = 0
	Plain = 1
	SingleQuoted = 2
	DoubleQuoted = 3
	Literal = 4
	Folded = 5
	ForcePlain = 6

