from enum import IntFlag

# Core.UILogic.Components.Filters.AbstractItemFilter
class AbstractItemFilter(IntFlag):
    ItemComponent = 0
    ItemCraftable = 1
    ItemDropable = 2
    ItemHarvestable = 3
    ItemTemporis = 4

# Core.UILogic.Components.Filters.BelongsToSet
class BelongsToSet(IntFlag):
    InSet = 0
    NotInSet = 1

# Core.UILogic.Components.Filters.CharacteristicEffect
class CharacteristicEffect(IntFlag):
    BoostDealtDamageDistance = 120
    DecreaseDealtDamageDistance = 121
    BoostDealtDamageWeapon = 122
    BoostDealtDamageSpells = 123
    DecreaseDealtDamageMelee = 124
    BoostDealtDamageMelee = 125

# Core.UILogic.Components.Filters.ExcludedCharacteristic
class ExcludedCharacteristic(IntFlag):
    WeaponSkill = 31
    ErosionInFight = 75
    ErosionDamage = 147

# Core.UILogic.Components.Filters.IsColorable
class IsColorable(IntFlag):
    Colorable = 0
    NotColorable = 1

# Core.UILogic.Components.Filters.ItemObtainingMethod
class ItemObtainingMethod(IntFlag):
    Component = 0
    Craft = 1
    Drop = 2
    Harvest = 3
    Temporis = 4

# Core.UILogic.Components.Filters.SubFilterCategory
class SubFilterCategory(IntFlag):
    NONE = 0
    SuperCategory = 1
    Category = 2
    Characteristic = 3
    WeaponEffect = 4
    ConsumableEffect = 5
    SkinTarget = 6
    BreedingItemEffectId = 7
    Obtaining = 8
    FullSoulStone = 9
    Set = 10
    Colorable = 11

