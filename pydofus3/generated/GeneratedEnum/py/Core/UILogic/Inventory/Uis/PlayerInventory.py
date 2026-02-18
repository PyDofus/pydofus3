from enum import IntFlag

# Core.UILogic.Inventory.Uis.PlayerInventory.AppearanceType
class AppearanceType(IntFlag):
    NONE = 0
    Body = 1
    Color = 2
    Face = 3

# Core.UILogic.Inventory.Uis.PlayerInventory.MountFamilyEnum
class MountFamilyEnum(IntFlag):
    Semyool = 1
    Rhineetle = 6
    Dragoturkey = 5

# Core.UILogic.Inventory.Uis.PlayerInventory.PresetListUi
class PresetListUi(IntFlag):
    Name = 0
    ModificationDate = 1

