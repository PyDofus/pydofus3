from enum import IntEnum

class ConditionsTooltipElement:
	class ConditionStyle(IntEnum):
		BonusEffect = 0
		NeutralEffect = 1
		MalusEffect = 2

class EffectAndDamageTooltipBlock:
	class CategoryType(IntEnum):
		Effects = 0
		Damages = 1
		Status = 2

	class EffectStyle(IntEnum):
		BonusEffect = 0
		MalusEffect = 1
		NeutralEffect = 2
		OverEffect = 3
		ExoticEffect = 4
		TheoreticalEffect = 5

