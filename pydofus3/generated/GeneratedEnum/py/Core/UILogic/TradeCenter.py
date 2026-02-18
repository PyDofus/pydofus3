from enum import IntFlag

# Core.UILogic.TradeCenter.AuctionHouseUI
class AuctionHouseUI(IntFlag):
    AuctionHouse = 0
    Inventory = 1

# Core.UILogic.TradeCenter.FilterCategoryType
class FilterCategoryType(IntFlag):
    NONE = -1
    Search = 1
    Level = 2
    EquipmentSuperType = 3
    EffectFilter = 4
    ItemType = 5
    Characteristic = 6
    BreedingItem = 7
    SoulStone = 8
    TargetItem = 9
    ObtainingMethod = 10
    Set = 11
    Colorable = 12

# Core.UILogic.TradeCenter.FilterComponentType
class FilterComponentType(IntFlag):
    NONE = -1
    SearchField = 1
    Toggle = 2
    EquipmentItem = 3
    Level = 4
    ItemToggle = 5
    SoulStoneSearchField = 6

# Core.UILogic.TradeCenter.ItemNpcStore
class ItemNpcStore(IntFlag):
    Buy = 0
    Sell = 1

# Core.UILogic.TradeCenter.SortingCriteria
class SortingCriteria(IntFlag):
    NONE = -1
    Name = 0
    Type = 1
    Level = 2
    Price = 3
    Stack = 4
    UnsoldDelay = 5

