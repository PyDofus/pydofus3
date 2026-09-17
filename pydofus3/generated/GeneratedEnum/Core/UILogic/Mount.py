from enum import IntEnum

class BreedingLine:
	class SortType(IntEnum):
		Name = 0
		Level = 1
		Gender = 2
		Mood = 3
		Love = 4
		Stamina = 5
		Experience = 6
		Generation = 7
		Maturity = 8
		Colors = 9

class BreedingLineType(IntEnum):
	None_ = -1
	Stable = 0
	Paddock = 1

