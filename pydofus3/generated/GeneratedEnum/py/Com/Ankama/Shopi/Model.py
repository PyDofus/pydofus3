from enum import IntFlag

# Com.Ankama.Shopi.Model.Address
class Address(IntFlag):
    M = 1
    MME = 2
    MLLE = 3
    OTHER = 4

# Com.Ankama.Shopi.Model.Article
class Article(IntFlag):
    CLASSIC = 1
    UPDATEDOFUSCHARACTERACCOUNT = 2
    UPDATEACCOUNTNICKNAME = 3
    TRANSFERACCOUNTWAKFU = 4
    RENAMECHARACTERWAKFU = 5
    UPDATEDOFUSCHARACTERSERVER = 6
    UPDATEDOFUSCHARACTERTEMPORISSERVER = 7
    UPDATEDOFUSCHARACTERPIONEERSERVER = 8
    RESTOREDOFUSCHARACTER = 9

# Com.Ankama.Shopi.Model.ArticlePaymentModeOneOf
class ArticlePaymentModeOneOf(IntFlag):
    ArticleVirtualPaymentMode = 1
    ArticleNonVirtualPaymentMode = 2
    ArticleMobilePaymentMode = 3
    ArticleFreePaymentMode = 4

# Com.Ankama.Shopi.Model.CartDetailOneOf
class CartDetailOneOf(IntFlag):
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

# Com.Ankama.Shopi.Model.CartDetailRequestOneOf
class CartDetailRequestOneOf(IntFlag):
    CartDetailClassicRequest = 1
    CartDetailUpdateAccountNicknameRequest = 2
    CartDetailTransferAccountWakfuRequest = 3
    CartDetailRenameCharacterWakfuRequest = 4
    CartDetailUpdateDofusCharacterAccountRequest = 5
    CartDetailUpdateDofusCharacterServerRequest = 6
    CartDetailUpdateDofusCharacterTemporisServerRequest = 7
    CartDetailUpdateDofusCharacterPioneerServerRequest = 8
    CartDetailRestoreDofusCharacterRequest = 9

# Com.Ankama.Shopi.Model.CartEstimatedTotalOneOf
class CartEstimatedTotalOneOf(IntFlag):
    NonVirtualCartEstimatedTotal = 1
    VirtualCartEstimatedTotal = 2

# Com.Ankama.Shopi.Model.CartPaymentModeOneOf
class CartPaymentModeOneOf(IntFlag):
    CartVirtualPaymentMode = 1
    CartNonVirtualPaymentMode = 2
    CartMobilePaymentMode = 3
    CartFreePaymentMode = 4

# Com.Ankama.Shopi.Model.CartProblemOneOf
class CartProblemOneOf(IntFlag):
    CartDetailProblem = 1
    CartGlobalProblem = 2

# Com.Ankama.Shopi.Model.CartSecurityOneOf
class CartSecurityOneOf(IntFlag):
    CartSecurityAnkamaCode = 1

# Com.Ankama.Shopi.Model.ChosenReferenceContextOneOf
class ChosenReferenceContextOneOf(IntFlag):
    GameActionReferenceContext = 1

# Com.Ankama.Shopi.Model.Device
class Device(IntFlag):
    DESKTOP = 1
    TABLET = 2
    MOBILE = 3

# Com.Ankama.Shopi.Model.Language
class Language(IntFlag):
    En = 1
    Es = 2
    Fr = 3
    Pt = 4
    De = 5

# Com.Ankama.Shopi.Model.MediaOneOf
class MediaOneOf(IntFlag):
    MediaImage = 1
    MediaYoutubeVideo = 2

# Com.Ankama.Shopi.Model.MetadataOneOf
class MetadataOneOf(IntFlag):
    StringMetadata = 1

# Com.Ankama.Shopi.Model.MobilePaymentModeId
class MobilePaymentModeId(IntFlag):
    Z1 = 1
    Z4 = 2

# Com.Ankama.Shopi.Model.NonVirtualPaymentModeId
class NonVirtualPaymentModeId(IntFlag):
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

# Com.Ankama.Shopi.Model.OneClickPaymentModeOption
class OneClickPaymentModeOption(IntFlag):
    SMS = 1

# Com.Ankama.Shopi.Model.OrderType
class OrderType(IntFlag):
    CLI = 1
    ANK = 2
    UNKNOWN = 3

# Com.Ankama.Shopi.Model.Ordering
class Ordering(IntFlag):
    ASC = 1
    DESC = 2

# Com.Ankama.Shopi.Model.PaymentModeOptionOneOf
class PaymentModeOptionOneOf(IntFlag):
    LegalDocumentPaymentModeOption = 1
    SaveCardPaymentModeOption = 2
    OneClickPaymentModeOption = 3

# Com.Ankama.Shopi.Model.PaymentOneOf
class PaymentOneOf(IntFlag):
    VIRTUAL = 1
    NONVIRTUAL = 2
    FREE = 3
    MOBILE = 4

# Com.Ankama.Shopi.Model.PaymentOptionsRequestOneOf
class PaymentOptionsRequestOneOf(IntFlag):
    OneClickPaymentOptionRequest = 1
    SaveCardPaymentOptionRequest = 2
    LegalDocumentPaymentOptionRequest = 3

# Com.Ankama.Shopi.Model.PaymentRequestOneOf
class PaymentRequestOneOf(IntFlag):
    VIRTUAL = 1
    NONVIRTUAL = 2
    FREE = 3
    MOBILE = 4

# Com.Ankama.Shopi.Model.ProcessoutTransaction
class ProcessoutTransaction(IntFlag):
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

# Com.Ankama.Shopi.Model.PromoteSectionOneOf
class PromoteSectionOneOf(IntFlag):
    PromoteSectionArticle = 1
    PromoteSectionCarousel = 2
    PromoteSectionImage = 3

# Com.Ankama.Shopi.Model.PromoteTargetOneOf
class PromoteTargetOneOf(IntFlag):
    CATEGORY = 1
    ARTICLE = 2

# Com.Ankama.Shopi.Model.PromotionCodeOneOf
class PromotionCodeOneOf(IntFlag):
    ValidPromotionCode = 1
    InvalidValidPromotionCode = 2

# Com.Ankama.Shopi.Model.PromotionDiscountOneOf
class PromotionDiscountOneOf(IntFlag):
    PromotionDiscountOfferedArticles = 1
    PromotionDiscountPercent = 2
    PromotionDiscountAmount = 3

# Com.Ankama.Shopi.Model.ReferenceChoiceType
class ReferenceChoiceType(IntFlag):
    ITEM = 1

# Com.Ankama.Shopi.Model.ReferenceOneOf
class ReferenceOneOf(IntFlag):
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

# Com.Ankama.Shopi.Model.ShopKey
class ShopKey(IntFlag):
    ANKAMASTORE = 1
    DOFUSUNITYINGAME = 2
    DOFUSTOUCHINGAME = 3
    WAKFUINGAME = 4
    WAVENINGAME = 5
    WAVENMOBILE = 6
    ZAAP = 7
    ZAAPMOBILE = 8

# Com.Ankama.Shopi.Model.SortOneOf
class SortOneOf(IntFlag):
    RelevanceSort = 1
    NonVirtualPriceSort = 2
    VirtualPriceSort = 3

# Com.Ankama.Shopi.Model.VirtualPaymentModeId
class VirtualPaymentModeId(IntFlag):
    GO = 1
    OG = 2
    WV = 3
    SW = 4

