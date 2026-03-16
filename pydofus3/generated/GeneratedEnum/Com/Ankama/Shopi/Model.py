from enum import IntEnum

class Address:
	class CivilityEnum(IntEnum):
		M = 1
		MME = 2
		MLLE = 3
		OTHER = 4

class Article:
	class TypeEnum(IntEnum):
		CLASSIC = 1
		UPDATEDOFUSCHARACTERACCOUNT = 2
		UPDATEACCOUNTNICKNAME = 3
		TRANSFERACCOUNTWAKFU = 4
		RENAMECHARACTERWAKFU = 5
		UPDATEDOFUSCHARACTERSERVER = 6
		UPDATEDOFUSCHARACTERTEMPORISSERVER = 7
		UPDATEDOFUSCHARACTERPIONEERSERVER = 8
		RESTOREDOFUSCHARACTER = 9

class ArticlePaymentModeOneOf:
	class DiscriminatorEnum(IntEnum):
		ArticleVirtualPaymentMode = 1
		ArticleNonVirtualPaymentMode = 2
		ArticleMobilePaymentMode = 3
		ArticleFreePaymentMode = 4

class CartDetailOneOf:
	class DiscriminatorEnum(IntEnum):
		CartDetailClassic = 1
		CartDetailPlaceHolder = 2
		CartDetailUpdateAccountNickname = 3
		CartDetailWakfuAccountTransfer = 4
		CartDetailWakfuRenameCharacter = 5
		CartDetailUpdateDofusCharacterAccount = 6
		CartDetailUpdateDofusCharacterServer = 7
		CartDetailUpdateDofusCharacterTemporisServer = 8
		CartDetailUpdateDofusCharacterPioneerServer = 9
		CartDetailRestoreDofusCharacter = 10

class CartDetailRequestOneOf:
	class DiscriminatorEnum(IntEnum):
		CartDetailClassicRequest = 1
		CartDetailUpdateAccountNicknameRequest = 2
		CartDetailTransferAccountWakfuRequest = 3
		CartDetailRenameCharacterWakfuRequest = 4
		CartDetailUpdateDofusCharacterAccountRequest = 5
		CartDetailUpdateDofusCharacterServerRequest = 6
		CartDetailUpdateDofusCharacterTemporisServerRequest = 7
		CartDetailUpdateDofusCharacterPioneerServerRequest = 8
		CartDetailRestoreDofusCharacterRequest = 9

class CartEstimatedTotalOneOf:
	class DiscriminatorEnum(IntEnum):
		NonVirtualCartEstimatedTotal = 1
		VirtualCartEstimatedTotal = 2

class CartPaymentModeOneOf:
	class DiscriminatorEnum(IntEnum):
		CartVirtualPaymentMode = 1
		CartNonVirtualPaymentMode = 2
		CartMobilePaymentMode = 3
		CartFreePaymentMode = 4

class CartProblemOneOf:
	class DiscriminatorEnum(IntEnum):
		CartDetailProblem = 1
		CartGlobalProblem = 2

class CartSecurityOneOf:
	class DiscriminatorEnum(IntEnum):
		CartSecurityAnkamaCode = 1

class ChosenReferenceContextOneOf:
	class DiscriminatorEnum(IntEnum):
		GameActionReferenceContext = 1

class Device(IntEnum):
	DESKTOP = 1
	TABLET = 2
	MOBILE = 3

class Language(IntEnum):
	En = 1
	Es = 2
	Fr = 3
	Pt = 4
	De = 5

class MediaOneOf:
	class DiscriminatorEnum(IntEnum):
		MediaImage = 1
		MediaYoutubeVideo = 2

class MetadataOneOf:
	class DiscriminatorEnum(IntEnum):
		StringMetadata = 1

class MobilePaymentModeId(IntEnum):
	Z1 = 1
	Z4 = 2

class NonVirtualPaymentModeId(IntEnum):
	OC = 1
	OK = 2
	C1 = 3
	OY = 4
	YZ = 5
	A0 = 6
	A1 = 7
	A2 = 8
	OH = 9
	OM = 10
	OF = 11
	OU = 12
	OD = 13
	OT = 14
	BL = 15
	OA = 16
	OX = 17
	OR = 18
	BZ = 19
	O2 = 20
	CV = 21
	DG = 22
	BU = 23
	O3 = 24
	O5 = 25
	O6 = 26
	O7 = 27
	HC = 28
	HM = 29
	HF = 30
	MB = 31
	QY = 32
	QK = 33
	Q1 = 34
	QX = 35

class OneClickPaymentModeOption:
	class SecurityEnum(IntEnum):
		SMS = 1

class Ordering(IntEnum):
	ASC = 1
	DESC = 2

class OrderType(IntEnum):
	CLI = 1
	ANK = 2
	UNKNOWN = 3

class PaymentModeOptionOneOf:
	class DiscriminatorEnum(IntEnum):
		LegalDocumentPaymentModeOption = 1
		SaveCardPaymentModeOption = 2
		OneClickPaymentModeOption = 3

class PaymentOneOf:
	class DiscriminatorEnum(IntEnum):
		VIRTUAL = 1
		NONVIRTUAL = 2
		FREE = 3
		MOBILE = 4

class PaymentOptionsRequestOneOf:
	class DiscriminatorEnum(IntEnum):
		OneClickPaymentOptionRequest = 1
		SaveCardPaymentOptionRequest = 2
		LegalDocumentPaymentOptionRequest = 3

class PaymentRequestOneOf:
	class DiscriminatorEnum(IntEnum):
		VIRTUAL = 1
		NONVIRTUAL = 2
		FREE = 3
		MOBILE = 4

class ProcessoutTransaction:
	class StatusEnum(IntEnum):
		WAITING = 1
		PENDING = 2
		AUTHORIZED = 3
		COMPLETED = 4
		FAILED = 5
		VOIDED = 6
		DISPUTED = 7
		SOLVED = 8
		REVERSED = 9
		PARTIALLYREFUNDED = 10
		REFUNDED = 11
		INREVIEW = 12
		BLOCKED = 13
		CHARGEBACKINITIATED = 14

class PromoteSectionOneOf:
	class DiscriminatorEnum(IntEnum):
		PromoteSectionArticle = 1
		PromoteSectionCarousel = 2
		PromoteSectionImage = 3

class PromoteTargetOneOf:
	class DiscriminatorEnum(IntEnum):
		CATEGORY = 1
		ARTICLE = 2

class PromotionCodeOneOf:
	class DiscriminatorEnum(IntEnum):
		ValidPromotionCode = 1
		InvalidValidPromotionCode = 2

class PromotionDiscountOneOf:
	class DiscriminatorEnum(IntEnum):
		PromotionDiscountOfferedArticles = 1
		PromotionDiscountPercent = 2
		PromotionDiscountAmount = 3

class ReferenceChoiceType(IntEnum):
	ITEM = 1

class ReferenceOneOf:
	class DiscriminatorEnum(IntEnum):
		ClassicReference = 1
		ServerReference = 2
		KardReference = 3
		GameActionReference = 4
		VodReference = 5
		WebtoonReference = 6
		WavenItemReference = 7
		VirtualSubscriptionReference = 8
		AccountStatusReference = 9
		OgrineReference = 10
		OgrineTokenReference = 11
		GoultineReference = 12

class ShopKey(IntEnum):
	ANKAMASTORE = 1
	DOFUSUNITYINGAME = 2
	DOFUSTOUCHINGAME = 3
	WAKFUINGAME = 4
	WAVENINGAME = 5
	WAVENMOBILE = 6
	ZAAP = 7
	ZAAPMOBILE = 8

class SortOneOf:
	class DiscriminatorEnum(IntEnum):
		RelevanceSort = 1
		NonVirtualPriceSort = 2
		VirtualPriceSort = 3

class VirtualPaymentModeId(IntEnum):
	GO = 1
	OG = 2
	WV = 3
	SW = 4

