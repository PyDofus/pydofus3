from enum import IntEnum

class ConfirmSellPopupUi:
	class ItemsSortingType(IntEnum):
		Name = 0
		Quantity = 1
		UnitPrice = 2
		TotalPrice = 3

class NpcStoreUi:
	class NpcStoreTab(IntEnum):
		Buy = 0
		Sell = 1

