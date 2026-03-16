from enum import IntEnum

class BonusCriterionType(IntEnum):
	Area = 1
	SubArea = 2
	Monster = 3
	MonsterFamily = 4
	Job = 5
	Ride = 6
	EquippedItem = 7
	QuestCategory = 8
	Item = 9
	JobSkill = 10
	ItemType = 11
	Server = 12
	Anomaly = 13

class BonusType(IntEnum):
	MonsterXp = 1
	JobXp = 2
	MonsterRespawnRate = 3
	MonsterStarRate = 4
	MonsterExtraChallenge = 5
	MonsterTaxCollectorDrop = 6
	Gather = 7
	GatherRespawnRate = 8
	GatherFightRate = 9
	CraftSpareComponent = 10
	CraftBetterQuality = 11
	MountNatality = 12
	MountXp = 13
	QuestXp = 14
	QuestKamas = 15
	MonsterDropChance = 16
	ChallengeReward = 17
	ArchmonsterRespawnRate = 18
	Craft = 19
	HealthRegen = 20
	HealItem = 21
	Tax = 22
	PetBonus = 23
	MountBonus = 24
	ArenaToken = 25
	MonsterDropQuality = 26
	ResourceStarRate = 27
	ArenaXp = 28
	TreasureHuntDrop = 29

