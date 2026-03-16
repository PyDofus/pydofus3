from enum import IntEnum

class AnkamaErrorBakBuy:
	class ReasonEnum(IntEnum):
		InvalidRate = 1
		InvalidExchangeType = 2
		InvalidKamasOrOgrinesQuatities = 3
		InvalidArticleKey = 4
		ServerMaintenance = 5
		KamaUploadFail = 6
		NotEnoughKamas = 7
		NotEnoughOgrines = 8
		InvalidServerId = 9
		InvalidAccountId = 10
		HeadingNotFound = 11
		OfferCanBuyOwn = 12
		OfferNotAvailable = 13
		ErrorTryAgain = 14
		AccountIndebtedOnThisServer = 15
		ServerDown = 16
		SomeLinkedOgrines = 17
		NotEligibleAccount = 18

class AnkamaErrorBakCancelBid:
	class ReasonEnum(IntEnum):
		InvalidBidType = 1
		InvalidBidId = 2
		InvalidAccountId = 3
		BidAlreadyCanceled = 4

class AnkamaErrorBakConsumeBufferKamas:
	class ReasonEnum(IntEnum):
		InvalidId = 1
		AmountLessRemainingAmount = 2

class AnkamaErrorBakCreateBid:
	class ReasonEnum(IntEnum):
		InvalidRate = 1
		InvalidRateAverage = 2
		NotEnoughOgrines = 3
		NotEnoughKamas = 4
		AddMissingOgrines = 5
		AddMissingKamas = 6
		BidAlreadyExists = 7
		AccountIndebtedOnThisServer = 8
		NotEligibleAccount = 9

class BakRate:
	class TypeEnum(IntEnum):
		OGRINESFORKAMAS = 1
		KAMASFOROGRINES = 2

