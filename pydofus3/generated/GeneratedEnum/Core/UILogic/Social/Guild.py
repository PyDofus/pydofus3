from enum import IntEnum

class GuildHouses:
	class GuildHousesSortEnum(IntEnum):
		SortByHouseName = 0
		SortByCoord = 1
		SortByOwner = 2

class GuildLogBook:
	class LogbookNewsEnum(IntEnum):
		GeneralNews = 0
		MissionNews = 1
		RaidNews = 2
		ChestNews = 3

class GuildMissions:
	class MissionSortType(IntEnum):
		Category = 0
		Rank = 1
		Subscribers = 2

class GuildMissionSubscribersUi:
	class SubscribersSortType(IntEnum):
		Name = 0
		Level = 1
		Status = 2
		Breed = 3

class GuildRightsAndRanksUI:
	class GuildRightsTab(IntEnum):
		General = 0
		Chest = 1

class GuildShopUi:
	class SortingCriteria(IntEnum):
		None_ = 0
		ArticleForSale = 1
		Price = 2
		ArticleAcquired = 3
		Delay = 4

	class TabEnum(IntEnum):
		Bonuses = 0
		Raids = 1

	class SubTabEnum(IntEnum):
		ForSale = 0
		Acquired = 1

class HouseGuildRight(IntEnum):
	GuildHouseEnabled = 1
	AccessGuildMatesHouse = 8
	AccessHouseDenyOthers = 16
	GuildMatesAccessSafes = 32
	ForbiddenSafes = 64
	AllowTeleport = 128
	AllowRespawn = 256

