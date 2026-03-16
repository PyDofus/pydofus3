from enum import IntEnum

class AuctionHouseItemsList:
	class ItemsSortingType(IntEnum):
		Quantity = 0
		Price = 1
		Loot = 2

class ObjectFamilyTypeEnum(IntEnum):
	None_ = 0
	EquipmentCategory = 1
	ConsumableCategory = 2
	ResourceCategory = 3
	RuneCategory = 4
	SoulCategory = 5
	CreatureCategory = 6
	CosmeticCategory = 7
	SkinCategory = 8

