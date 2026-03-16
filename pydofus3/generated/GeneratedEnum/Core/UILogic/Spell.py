from enum import IntEnum

class CommonSpellsList:
	class CommonSpellsSortEnum(IntEnum):
		Name = 0
		Equipped = 1

class ForgettableListBase[TBinding]:
	class SpellFilter(IntEnum):
		All = 0
		LearnedSpells = 1
		UnlearnedSpells = 2

class ModstersList:
	class ForgettableModstersSortEnum(IntEnum):
		Name = 0
		ActiveSpell = 1
		PassiveSpell = 2
		Equipped = 3

class ObtainingSpell(IntEnum):
	Droppable = 0
	Craftable = 1
	InQuest = 2
	Unkown = 3

class SpellList:
	class ActionFilterId(IntEnum):
		Damages = 3
		Air = 4
		Fire = 5
		Water = 6
		Earth = 7
		Neutral = 8
		MultiElement = 9
		Protection = 10
		Heal = 11
		Malus = 12
		Bonus = 13
		Placement = 14
		Summons = 15
		Special = 16

