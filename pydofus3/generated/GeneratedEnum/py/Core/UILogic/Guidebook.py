from enum import IntFlag

# Core.UILogic.Guidebook.GameCollectionTabUI
class GameCollectionTabUI(IntFlag):
    All = 0
    Discovered = 1

# Core.UILogic.Guidebook.GameCollectionTabUI
class GameCollectionTabUI(IntFlag):
    Order = 0
    Name = 1

# Core.UILogic.Guidebook.GameGuideUi
class GameGuideUi(IntFlag):
    CtrCat = 0
    CtrSubCat = 1
    CtrSubSubCat = 2
    Unknown = 3

# Core.UILogic.Guidebook.GuideBookArticleEnum
class GuideBookArticleEnum(IntFlag):
    Almanax = 17
    Event = 20
    TreasureHunt = 65
    Chat = 66
    DivineDimension = 120
    Kolossium = 140
    Smithmagic = 147
    KolossiumChart = 226
    KolossiumSurrender = 229
    InfiniteDream = 180

# Core.UILogic.Guidebook.GuideBookArticleImageEnum
class GuideBookArticleImageEnum(IntFlag):
    Object = 0
    Challenge = 1
    Emote = 2
    GuildEmblemBackground = 3
    GuildEmblemSymbol = 4
    GuildRank = 5
    Achievement = 7
    OrnamentIcon = 8
    Ornament = 9
    CharacterCosmetics = 10
    Spell = 11
    SpellState = 12
    Smiley = 13
    BreedRole = 15
    KoliLeague = 18
    KoliLeagueIllustration = 19
    TextIcon = 20
    Monster = 21
    Companion = 22
    Choices = 23
    GuideBook = 24

# Core.UILogic.Guidebook.GuideBookImageHorizontalAlignEnum
class GuideBookImageHorizontalAlignEnum(IntFlag):
    Left = 0
    Center = 1
    Right = 2

# Core.UILogic.Guidebook.GuideBookImageVerticalAlignEnum
class GuideBookImageVerticalAlignEnum(IntFlag):
    Top = 0
    Bottom = 1

# Core.UILogic.Guidebook.GuidebookSubTab
class GuidebookSubTab(IntFlag):
    Collection = 0
    TemporisTab = 1
    Suggestions = 2
    GameGuide = 3
    NONE = -1

