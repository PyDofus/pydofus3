from enum import IntEnum

class DragDropStep(IntEnum):
	START = 0
	DRAG = 1
	END = 2
	INACTIVE = 3

class KeyGroupType(IntEnum):
	KEY = 0
	STRING = 1
	ARRAY = 2

