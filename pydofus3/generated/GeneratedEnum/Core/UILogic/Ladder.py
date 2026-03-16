from enum import IntEnum

class BaseLadderTabUI[T]:
	class LadderSortType(IntEnum):
		Rank = 0
		Name = 1
		Breed = 2
		Server = 3
		Level = 4
		Rating = 5
		WinRate = 6
		Xp = 7
		AchievementPoints = 8
		Intensity = 9
		Wave = 10
		GlobalTurn = 11

class LadderUI:
	class LadderTabs(IntEnum):
		Experience = 0
		Koli = 1
		Achievement = 2
		WorldEvents = 3
		InfiniteDream = 4

class WorldEventsLadderTabUI:
	class WorldEventLadderSortType(IntEnum):
		Rank = 0
		Name = 1
		Level = 2
		Score = 3

