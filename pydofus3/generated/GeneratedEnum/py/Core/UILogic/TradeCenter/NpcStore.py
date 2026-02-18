from enum import IntFlag

# Core.UILogic.TradeCenter.NpcStore.ConfirmSellPopupUi
class ConfirmSellPopupUi(IntFlag):
    Name = 0
    Quantity = 1
    UnitPrice = 2
    TotalPrice = 3

# Core.UILogic.TradeCenter.NpcStore.NpcStoreUi
class NpcStoreUi(IntFlag):
    Buy = 0
    Sell = 1

