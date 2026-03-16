from enum import IntEnum
from enum import IntFlag

class KisPopupWarningUi:
	class KisWarningTypeEnum(IntEnum):
		Inactivity = 0
		Prevent = 1
		Sanction = 2
		MissingEquipment = 3

class PartyDisplayUi:
	class PartyWidgetOptions(IntFlag):
		Horizontal = 1
		Vertical = 2
		OneLine = 4
		TwoLines = 8
		RestrictFightToParty = 16
		PartyLocked = 32
		ArenaPartyLocked = 64
		Small = 128
		Big = 256
		Default = 262

class PvpArenaBaseUi:
	class PvpArenaTab(IntEnum):
		Default = -1
		Fights = 0
		Rewards = 1
		Ladder = 2

