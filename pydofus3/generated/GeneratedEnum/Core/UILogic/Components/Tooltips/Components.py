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

