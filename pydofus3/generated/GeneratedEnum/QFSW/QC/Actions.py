from enum import IntEnum

class Typewriter:
	class Config:
		class ChunkType(IntEnum):
			Character = 0
			Word = 1
			Line = 2

