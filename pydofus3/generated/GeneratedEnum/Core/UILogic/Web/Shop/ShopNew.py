from enum import IntEnum

class ShopObjectType(IntEnum):
	Article = 0
	Category = 1

class ShopUi:
	class ShopViewEnum(IntEnum):
		Catalog = 0
		Search = 1
		Article = 2

class SortTypeEnum(IntEnum):
	Relevance = 0
	VirtualPrice = 1
	NonVirtualPrice = 2

