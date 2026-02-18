from enum import IntFlag

# Core.UILogic.Common.AdministrablePopupButtonTypeEnum
class AdministrablePopupButtonTypeEnum(IntFlag):
    MainButton = 0
    SecondaryButton = 1

# Core.UILogic.Common.FeedUI
class FeedUI(IntFlag):
    Mount = 0
    Pet = 1

# Core.UILogic.Common.FeedUI
class FeedUI(IntFlag):
    SingleItem = 0
    SingleItemSingleQuantity = 1
    MultipleItems = 2

# Core.UILogic.Common.WidgetManager
class WidgetManager(IntFlag):
    BannerMenu = 0
    Buffs = 1
    TreasureHunt = 2
    Timeline = 3
    MiniMap = 4
    QuestList = 5
    ActionBar = 6
    Party = 7
    Challenges = 8
    Chat = 9
    Breach = 10
    CharacterInformations = 11
    Summons = 12
    Smiley = 13
    EndTurn = 14

