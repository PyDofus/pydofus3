from enum import IntEnum

class BreedingLine:
	class SortType(IntEnum):
		Name = 0
		LevelAsc = 1
		LevelDesc = 2
		Sex = 3
		MoodAsc = 4
		MoodDesc = 5

class BreedingLineType(IntEnum):
	None_ = -1
	Stable = 0
	Paddock = 1

