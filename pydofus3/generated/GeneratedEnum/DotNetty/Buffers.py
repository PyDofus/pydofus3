from enum import IntEnum

class ByteOrder(IntEnum):
	LittleEndian = 0
	BigEndian = 1

class SizeClass(IntEnum):
	Tiny = 0
	Small = 1
	Normal = 2

