from enum import IntEnum
from enum import IntFlag

class QuestList:
	class QuestListWidgetOption(IntFlag):
		FollowFew = 1
		FollowNormal = 2
		FollowLot = 4
		AutoFollow = 8
		FontSmall = 16
		FontMedium = 32
		FontLarge = 64
		AutoResize = 128
		OpacityLow = 256
		OpacityMedium = 512
		OpacityHigh = 1024
		Default = 1196
		FontXLarge = 2048

class QuestsUI:
	class Tabs(IntEnum):
		InProgress = 0
		Done = 1
		Hidden = 2

