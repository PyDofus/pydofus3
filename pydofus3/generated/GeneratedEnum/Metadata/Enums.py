from enum import IntEnum

class AlmanaxCalendarCategory(IntEnum):
	Special = 2
	Floating = 3
	Javian = 4
	Flovor = 5
	Martalo = 6
	Aperirel = 7
	Maisial = 8
	Juinssidor = 9
	Joullier = 10
	Fraouctor = 11
	Septange = 12
	Octolliard = 13
	Novamaire = 14
	Descendre = 15

class CollectableCategory(IntEnum):
	Common = 0
	Rare = 1
	Evolution = 2
	Epic = 3
	Legendary = 4

class Collection(IntEnum):
	Mobedex = 1

class SkinSlotRuleType(IntEnum):
	Default = 0
	Breed = 1
	BreedAndSex = 2
	Face = 3

class SpellZoneShape(IntEnum):
	None_ = 0
	Empty = 32
	DiagonalCrossWithoutCenter = 35
	Star = 42
	DiagonalCross = 43
	DiagonalPerpendicularLine = 45
	DiagonalLine = 47
	Custom = 59
	WholeMapWithTheDead = 65
	Boomerang = 66
	Circle = 67
	Checkerboard = 68
	Fork = 70
	Square = 71
	OutsideCircle = 73
	Line = 76
	Regular = 78
	Ring = 79
	Point = 80
	CrossWithoutCenter = 81
	Rectangle = 82
	PerpendicularLine = 84
	HalfCircle = 85
	Cone = 86
	SquareWithoutDiagonals = 87
	Cross = 88
	OutsideComplexCircle = 90
	WholeMap = 97
	LineFromCaster = 108

class WorldEventDataType(IntEnum):
	WorldBoss = 1
	MonstersHunter = 2
	Dungeon = 3
	FarmingSimulator = 4

