from enum import IntEnum

class BestiaryTabUI:
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

