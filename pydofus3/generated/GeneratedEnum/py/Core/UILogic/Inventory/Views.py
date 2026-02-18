from enum import IntFlag

# Core.UILogic.Inventory.Views.SortFields
class SortFields(IntFlag):
    NONE = -1
    Name = 1
    Weight = 2
    Quantity = 3
    LotWeight = 4
    AveragePrice = 5
    LotAveragePrice = 6
    Level = 7
    ItemType = 8
    Obtention = 9

# Core.UILogic.Inventory.Views.ViewsNames
class ViewsNames(IntFlag):
    NONE = 0
    Equipment = 1
    Real = 2
    RolePlayBuff = 3
    Certificate = 4
    BankEquipment = 5
    BankConsumables = 6
    BankResources = 7
    BankQuest = 8
    Bank = 9
    BankFiltered = 10
    BankAssociatedRunes = 21
    BankCosmetics = 22
    Storage = 11
    StorageQuest = 12
    StorageEquipment = 13
    StorageConsumables = 14
    StorageResources = 15
    StorageCosmetics = 23
    StorageBidHouseFiltered = 16
    StorageSmithMagicFiltered = 17
    StorageCraftFiltered = 18
    StorageFiltered = 20
    StorageFavoriteView = 28
    StorageTaxCollectorEquipmentFiltered = 44
    StorageCustomView1 = 29
    StorageCustomView2 = 30
    StorageCustomView3 = 31
    StorageCustomView4 = 32
    StorageCustomView5 = 33
    StorageCustomView6 = 34
    StorageCustomView7 = 35
    StorageCustomView8 = 36
    ForgettableSpellsFiltered = 19
    CosmeticView = 37
    CosmeticViewFiltered = 38
    CosmeticOrnamentView = 39
    CosmeticTitlesView = 40
    CosmeticAurasView = 41
    CosmeticOutfitsView = 42
    Paddock = 43

