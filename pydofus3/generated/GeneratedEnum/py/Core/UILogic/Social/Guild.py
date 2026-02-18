from enum import IntFlag

# Core.UILogic.Social.Guild.GuildHouses
class GuildHouses(IntFlag):
    SortByHouseName = 0
    SortByCoord = 1
    SortByOwner = 2

# Core.UILogic.Social.Guild.GuildLogBook
class GuildLogBook(IntFlag):
    NONE = -1
    GeneralNews = 0
    ChestNews = 1

# Core.UILogic.Social.Guild.GuildMissionSubscribersUi
class GuildMissionSubscribersUi(IntFlag):
    Name = 0
    Level = 1
    Status = 2
    Breed = 3

# Core.UILogic.Social.Guild.GuildMissions
class GuildMissions(IntFlag):
    Category = 0
    Rank = 1
    Subscribers = 2

# Core.UILogic.Social.Guild.GuildPaddockInfoUi
class GuildPaddockInfoUi(IntFlag):
    SortByName = 0
    SortByType = 1
    SortByOwner = 2

# Core.UILogic.Social.Guild.GuildPaddockUI
class GuildPaddockUI(IntFlag):
    NONE = 0
    SortByCoord = 1
    SortBySize = 2
    SortByMount = 3

# Core.UILogic.Social.Guild.GuildRightsAndRanksUI
class GuildRightsAndRanksUI(IntFlag):
    General = 0
    Chest = 1

# Core.UILogic.Social.Guild.GuildShopUi
class GuildShopUi(IntFlag):
    NONE = 0
    ArticleForSale = 1
    Price = 2
    ArticleAcquired = 3
    Delay = 4

# Core.UILogic.Social.Guild.GuildShopUi
class GuildShopUi(IntFlag):
    ForSale = 0
    Acquired = 1

# Core.UILogic.Social.Guild.HouseGuildRight
class HouseGuildRight(IntFlag):
    GuildHouseEnabled = 1
    AccessGuildMatesHouse = 8
    AccessHouseDenyOthers = 16
    GuildMatesAccessSafes = 32
    ForbiddenSafes = 64
    AllowTeleport = 128
    AllowRespawn = 256

