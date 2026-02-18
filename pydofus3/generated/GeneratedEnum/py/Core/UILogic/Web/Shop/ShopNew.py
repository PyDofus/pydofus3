from enum import IntFlag

# Core.UILogic.Web.Shop.ShopNew.ShopObjectType
class ShopObjectType(IntFlag):
    Article = 0
    Category = 1

# Core.UILogic.Web.Shop.ShopNew.ShopUi
class ShopUi(IntFlag):
    Catalog = 0
    Search = 1
    Article = 2

# Core.UILogic.Web.Shop.ShopNew.SortTypeEnum
class SortTypeEnum(IntFlag):
    Relevance = 0
    VirtualPrice = 1
    NonVirtualPrice = 2

