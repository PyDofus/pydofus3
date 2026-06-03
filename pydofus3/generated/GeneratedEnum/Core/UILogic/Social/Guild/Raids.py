from enum import IntEnum

class GuildRaidPopup:
	class RaidPopupType(IntEnum):
		ClaimRewards = 0
		Finish = 1
		Restart = 2
		Leave = 3

class GuildRaids:
	class RaidMode(IntEnum):
		Guild = 0
		Player = 1

	class SortingCriteria(IntEnum):
		Name = 0
		MemberCount = 1
		Status = 2
		Level = 3
		Affiliation = 4

class RaidTrackingUI:
	class TabEnum(IntEnum):
		Team = 0
		Goal = 1

