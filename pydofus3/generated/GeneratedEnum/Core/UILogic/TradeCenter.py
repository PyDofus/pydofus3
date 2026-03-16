from enum import IntEnum

class AuctionHouseUI:
	class WindowID(IntEnum):
		AuctionHouse = 0
		Inventory = 1

class FilterCategoryType(IntEnum):
	None_ = -1
	Search = 1
	Level = 2
	EquipmentSuperType = 3
	EffectFilter = 4
	ItemType = 5
	Characteristic = 6
	BreedingItem = 7
	TargetItem = 8
	ObtainingMethod = 9
	Set = 10
	Colorable = 11
	Possession = 12

class FilterComponentType(IntEnum):
	None_ = -1
	SearchField = 1
	Toggle = 2
	EquipmentItem = 3
	Level = 4

class SortingCriteria(IntEnum):
	None_ = -1
	Name = 0
	Type = 1
	Level = 2
	Price = 3
	Stack = 4
	UnsoldDelay = 5

