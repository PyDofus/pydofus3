from enum import IntEnum
from enum import IntFlag

class LobbyApplicantsUi:
	class Tab(IntEnum):
		Waiting = 0
		Accepted = 1
		Rejected = 2

	class SortingCriteria(IntEnum):
		Name = 0
		Level = 1
		Date = 2

class LobbyTab:
	class LobbyTabEnum(IntEnum):
		Join = 0
		Create = 1
		Applications = 2

	class LobbiesSearchCriterions(IntFlag):
		EventName = 1
		EventType = 2
		Description = 4
		Achievements = 8
		PlayerName = 16
		Tag = 32
		Level = 64
		All = 4294967295

	class LobbiesFilter(IntFlag):
		NoLevel = 1
		NotOwnedQuests = 2
		AlreadyAchievedSuccess = 4
		AnnounceFull = 8
		Paid = 16
		Accepted = 32
		Pending = 64
		Suspended = 128
		Rejected = 256
		All = 4294967295

	class SortingCriteria(IntEnum):
		Type = 0
		Description = 1
		Date = 2
		Group = 3

class LobbyType(IntEnum):
	None_ = 0
	Dungeon = 1
	Quest = 2
	Raid = 3
	WantedNotice = 4
	Archimonster = 5
	Kolizeum = 6
	InfiniteDream = 7

class State(IntEnum):
	None_ = 0
	Pending = 1
	Suspended = 2
	Accepted = 3
	Rejected = 4
	Full = 5
	Mine = 6

