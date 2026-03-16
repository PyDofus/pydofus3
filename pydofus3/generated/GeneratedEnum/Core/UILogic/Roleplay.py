from enum import IntEnum
from enum import IntFlag

class FightMapPreviewUi:
	class CellType(IntEnum):
		None_ = 0
		Mov = 1
		NoLos = 2
		Red = 3
		Blue = 4

class SpectatorUi:
	class CriteriaFight(IntEnum):
		NB_PLAYER = 0
		AVERAGE_LEVEL = 1
		DURATION = 2

	class CriteriaTeam(IntEnum):
		NAME = 0
		LEVEL = 1

class TreasureHunt:
	class TreasureHuntWidgetSettings(IntFlag):
		FontSmall = 1
		FontMedium = 2
		FontLarge = 4
		OpacityNone = 8
		OpacityLow = 16
		OpacityMedium = 32
		Default = 34
		OpacityHigh = 64

