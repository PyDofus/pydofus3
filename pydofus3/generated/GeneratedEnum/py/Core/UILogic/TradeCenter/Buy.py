from enum import IntFlag

# Core.UILogic.TradeCenter.Buy.AuctionHouseItemsList
class AuctionHouseItemsList(IntFlag):
    Quantity = 0
    Price = 1

# Core.UILogic.TradeCenter.Buy.ObjectFamilyTypeEnum
class ObjectFamilyTypeEnum(IntFlag):
    NONE = 0
    EquipmentCategory = 1
    ConsumableCategory = 2
    ResourceCategory = 3
    RuneCategory = 4
    SoulCategory = 5
    CreatureCategory = 6
    CosmeticCategory = 7
    SkinCategory = 8

