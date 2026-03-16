from enum import IntEnum

class SmithMagicItemEffectLine:
	class EffectStateStyle(IntEnum):
		neutral = 0
		bonus = 1
		malus = 2
		exo = 3
		over = 4
		missing = 5
		malusEffect = 6
		bonusEffect = 7

class SmithMagicUi:
	class SortType(IntEnum):
		Effect = 0
		Min = 1
		Max = 2
		Value = 3

