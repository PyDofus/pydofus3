from enum import IntEnum

class WebBakPopup:
	class BakPopupTypeEnum(IntEnum):
		BuyOgrines = 0
		BuyKamas = 1
		SubmitOfferKamas = 2
		SubmitOfferOgrines = 3
		BuyOgrinesValidated = 4
		BuyKamasValidated = 5
		ValidateOffer = 6
		CancelOfferKamas = 7
		CancelOfferOgrines = 8

class WebBakUi:
	class OffersSortEnum(IntEnum):
		None_ = 0
		SortByOgrines = 1
		SortByKamas = 2
		SortByRate = 3

	class BakTabEnum(IntEnum):
		BuyOgrines = 0
		BuyKamas = 1

