from enum import IntEnum

class AbstractItemFilter:
	class ItemCategoryId(IntEnum):
		ItemComponent = 0
		ItemCraftable = 1
		ItemDropable = 2
		ItemHarvestable = 3
		ItemTemporis = 4

class BelongsToSet(IntEnum):
	InSet = 0
	NotInSet = 1

class CharacteristicEffect(IntEnum):
	BoostDealtDamageDistance = 120
	DecreaseDealtDamageDistance = 121
	BoostDealtDamageWeapon = 122
	BoostDealtDamageSpells = 123
	DecreaseDealtDamageMelee = 124
	BoostDealtDamageMelee = 125

class IsColorable(IntEnum):
	Colorable = 0
	NotColorable = 1

class ItemObtainingMethod(IntEnum):
	Component = 0
	Craft = 1
	Drop = 2
	Harvest = 3
	Temporis = 4

class Possession(IntEnum):
	Owned = 0
	Unowned = 1

class SubFilterCategory(IntEnum):
	None_ = 0
	SuperCategory = 1
	Category = 2
	Characteristic = 3
	WeaponEffect = 4
	ConsumableEffect = 5
	SkinTarget = 6
	BreedingItemEffectId = 7
	Obtaining = 8
	Set = 9
	Colorable = 10
	Possession = 11

