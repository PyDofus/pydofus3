from enum import IntFlag

# Core.UILogic.Web.Bak.WebBakPopup
class WebBakPopup(IntFlag):
    BuyOgrines = 0
    BuyKamas = 1
    SubmitOfferKamas = 2
    SubmitOfferOgrines = 3
    BuyOgrinesValidated = 4
    BuyKamasValidated = 5
    ValidateOffer = 6
    CancelOfferKamas = 7
    CancelOfferOgrines = 8

# Core.UILogic.Web.Bak.WebBakUi
class WebBakUi(IntFlag):
    NONE = 0
    SortByOgrines = 1
    SortByKamas = 2
    SortByRate = 3

# Core.UILogic.Web.Bak.WebBakUi
class WebBakUi(IntFlag):
    BuyOgrines = 0
    BuyKamas = 1

