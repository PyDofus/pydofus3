from enum import IntEnum

class SmithMagicDraconicPopup:
	class DraconicRuneType(IntEnum):
		Offensive = 0
		Defensive = 1
		Power = 2

class SmithMagicDraconicUtils:
	class DraconicRuneError(IntEnum):
		None_ = 0
		NoElementToTransform = 1
		ElementAlreadyOnItem = 2
		HasDraconicMark = 3

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

