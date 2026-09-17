from enum import IntEnum

class GDIOBlittableArrayWrapper:
	class UpdateFlags(IntEnum):
		NoUpdateNeeded = 0
		SizeChanged = 1
		DataIsNativePointer = 2
		DataIsNativeOwnedMemory = 3
		DataIsEmpty = 4
		DataIsNull = 5

