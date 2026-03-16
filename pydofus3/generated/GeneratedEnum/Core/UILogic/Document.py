from enum import IntEnum

class CascadingStyle:
	class ListStyleType(IntEnum):
		Null = 0
		None_ = 1
		Square = 2
		Circle = 3
		DecimalLeadingZero = 4

class CascadingStyleSheet:
	class ElementType(IntEnum):
		None_ = 0
		Body = 1
		Paragraph = 2
		Line = 3
		OrderedList = 4

class DocumentBase[T]:
	class IconType(IntEnum):
		Spell = 0
		State = 1
		Item = 2

