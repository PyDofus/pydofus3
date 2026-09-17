from enum import IntEnum
from enum import IntFlag

class BestiaryTabUI:
	class DetailsSection(IntFlag):
		Stats = 1
		Properties = 2
		Spells = 4
		Loots = 16

	class MonsterType(IntEnum):
		Monster = 0
		QuestMonster = 1
		MiniBoss = 2
		Boss = 3
		Bounty = 4

	class BestiarySortType(IntEnum):
		None_ = 0
		Name = 1
		Level = 2

class MonsterInfoWrapper:
	class MonsterProperties(IntFlag):
		CanPlay = 1
		CanMove = 2
		CanTackle = 4
		CanBePushed = 8
		CanSwitchPos = 16
		CanSwitchPosOnTarget = 32
		CanBeCarried = 64
		CanUsePortal = 128
		CanBeControlledByFightOwner = 256

