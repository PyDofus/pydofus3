from enum import IntEnum
from enum import IntFlag

class EffectFormatFlags(IntFlag):
	None_ = 0
	SpellDetails = 1
	SpellZone = 2

class EffectStyle(IntEnum):
	BonusEffect = 0
	MalusEffect = 1
	NeutralEffect = 2
	OverEffect = 3
	ExoticEffect = 4
	TheoreticalEffect = 5

