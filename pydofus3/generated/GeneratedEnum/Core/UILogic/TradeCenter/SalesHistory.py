from enum import IntEnum
from enum import IntFlag

class SalesHistoryUI:
	class SortType(IntEnum):
		None_ = -1
		SaleDate = 0
		Name = 1
		Quantity = 2
		Kamas = 3
		Type = 4

	class StatusFilterEnum(IntFlag):
		Unsold = 1
		Sold = 2

