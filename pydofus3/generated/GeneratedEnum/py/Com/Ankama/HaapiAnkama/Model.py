from enum import IntFlag

# Com.Ankama.HaapiAnkama.Model.Account
class Account(IntFlag):
    ANKAMA = 1
    EXTERNAL = 2
    GUEST = 3
    GHOST = 4

# Com.Ankama.HaapiAnkama.Model.Account
class Account(IntFlag):
    SHIELD = 1
    AUTHENTICATOR = 2

# Com.Ankama.HaapiAnkama.Model.Account
class Account(IntFlag):
    COMMUNITY0 = 1
    COMMUNITY1 = 2
    COMMUNITY2 = 3
    COMMUNITY3 = 4
    COMMUNITY4 = 5
    COMMUNITY5 = 6
    COMMUNITY6 = 7
    COMMUNITY7 = 8
    COMMUNITY8 = 9
    COMMUNITY9 = 10
    COMMUNITY10 = 11
    COMMUNITY11 = 12
    COMMUNITY12 = 13
    COMMUNITY13 = 14
    COMMUNITY14 = 15

# Com.Ankama.HaapiAnkama.Model.Account
class Account(IntFlag):
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2

# Com.Ankama.HaapiAnkama.Model.Account
class Account(IntFlag):
    ACCEPTED = 1
    REFUSED = 2
    PENDING = 3

# Com.Ankama.HaapiAnkama.Model.AccountOrigin
class AccountOrigin(IntFlag):
    Game = 1

# Com.Ankama.HaapiAnkama.Model.AccountSendCodeSmsFailure
class AccountSendCodeSmsFailure(IntFlag):
    PhoneUnlisted = 1
    LimitSmsWeek = 2
    LimitMonth = 3
    LimitWeek = 4
    LimitHour = 5
    LimitMinute = 6
    LimitPhoneMonth = 7
    GsmErrorNoDelivery = 8
    CountryNotActivate = 9

# Com.Ankama.HaapiAnkama.Model.CmsLauncherCarousel
class CmsLauncherCarousel(IntFlag):
    ANKAMA = 1
    ANKAMAEDITIONS = 2
    ANKAMAPRESSE = 3
    BOUFBOWL = 4
    DOFUS = 5
    WAKFU = 6
    DOFUSINGAME = 7
    DOFUSTOUCHINGAME = 8
    DOFUSPETSINGAME = 9
    WAKFUINGAME = 10
    KROSMASTER2D = 11
    KROSMAGAINGAME = 12
    KROSMAGA = 13
    KROSMASTER = 14
    KROSMASTERINGAME = 15
    TACTILEWARSINGAME = 16
    STEAMDOFUS = 17
    STEAMKROSMAGA = 18
    WAVEN = 19
    WAVENINGAME = 20
    ZAAP = 21

# Com.Ankama.HaapiAnkama.Model.CmsLauncherCarousel
class CmsLauncherCarousel(IntFlag):
    EXCLUKROSMOZ = 1
    EXCLUALLSKREEN = 2

# Com.Ankama.HaapiAnkama.Model.ErrorAccountLogin
class ErrorAccountLogin(IntFlag):
    BAN = 1
    BLACKLIST = 2
    LOCKED = 3
    DELETED = 4
    OTPTIMEFAILED = 5
    BRUTEFORCE = 6
    FAILED = 7
    MAILNOVALID = 8
    BETACLOSED = 9
    NOACCOUNT = 10
    ACCOUNTLINKED = 11
    ACCOUNTINVALID = 12
    ACCOUNTSHIELDED = 13
    ACCOUNTNOCERTIFY = 14
    RECAPTCHAINVALID = 15
    ANONYMOUSIPFORBIDDEN = 16
    GUESTFORBIDDEN = 17

# Com.Ankama.HaapiAnkama.Model.ErrorAddress
class ErrorAddress(IntFlag):
    ADDRESSCIVILITY = 1
    ADDRESSNAMEBADLEN = 2
    ADDRESSFIRSTNAME = 3
    ADDRESSLASTNAME = 4
    ADDRESSADDRESS = 5
    ADDRESSADDITIONALADDRESS = 6
    ADDRESSCITY = 7
    ADDRESSZIPCODE = 8
    ADDRESSCOUNTRY = 9
    ANKAMAADDEDIPBAD = 10
    FIRSTNAMETOOLONG = 11
    LASTNAMETOOLONG = 12
    ADDRESSTOOLONG = 13
    CITYTOOLONG = 14
    COUNTRYCODETOOLONG = 15
    ADDITIONALADDRESSTOOLONG = 16
    STATECODETOOLONG = 17

# Com.Ankama.HaapiAnkama.Model.ErrorCertification
class ErrorCertification(IntFlag):
    ACCOUNTALREADYCERTIFIED = 1
    CANTEDITCERTIFICATIONFIRSTNAME = 2
    CANTEDITCERTIFICATIONLASTNAME = 3
    CANTEDITCERTIFICATIONBIRTHDATE = 4
    PARENTALEMAILNEEDED = 5
    INVALIDPARENTALEMAIL = 6
    INVALIDSECRETQUESTIONID = 7
    ADDRESSNEEDED = 8
    CITYNEEDED = 9
    ZIPCODENEEDED = 10
    COUNTRYCODENEEDED = 11
    ACCOUNTNOTFOUND = 12
    BIRTHDATEBADFORMAT = 13
    MINIMUMAGEEXCEEDED = 14
    SECRETANSWERTOOSHORT = 15
    SECRETANSWERTOOWEAK = 16
    SECRETANSWERALREADYUSED = 17
    UPDATEFAILED = 18
    UNKNOWNCIVILITYTYPE = 19
    ADDRESSWRONGFORMAT = 20
    ADDITIONALADDRESSWRONGFORMAT = 21
    CITYWRONGFORMAT = 22
    ZIPCODEWRONGFORMAT = 23
    COUNTRYCODEWRONGFORMAT = 24
    STATECODEWRONGFORMAT = 25
    FIRSTNAMETOOLONG = 26
    LASTNAMETOOLONG = 27
    ADDRESSTOOLONG = 28
    CITYTOOLONG = 29
    ZIPCODETOOLONG = 30
    COUNTRYCODETOOLONG = 31
    ADDITIONALADDRESSTOOLONG = 32
    STATECODETOOLONG = 33

# Com.Ankama.HaapiAnkama.Model.ErrorEmailing
class ErrorEmailing(IntFlag):
    INVALIDADDRESSEMAIL = 1
    INVALIDSENDINGTYPE = 2
    INVALIDEMAILINGKEY = 3
    ALREADYSUBSCRIBED = 4

# Com.Ankama.HaapiAnkama.Model.ErrorGameSession
class ErrorGameSession(IntFlag):
    SERVICEDENIEDFORCURRENTAPIKEY = 1
    SERVICEDENIEDFORGAMEID = 2
    GAMEBUYERSONLY = 3
    CONNECTPLAYERFAILED = 4

# Com.Ankama.HaapiAnkama.Model.ErrorPassculture
class ErrorPassculture(IntFlag):
    TOKENALREADYCONSUMED = 1
    TOKENNOTFOUND = 2
    ARTICLENOTFOUND = 3
    ACCOUNTNOTFOUND = 4
    PAYMENTFAILED = 5
    APIKEYINVALIDMISSINGSHOP = 6

# Com.Ankama.HaapiAnkama.Model.ErrorRelation
class ErrorRelation(IntFlag):
    ALREADYEXISTS = 1
    BLACKLISTED = 2
    NOTEXISTS = 3
    NOTREQUESTED = 4
    SAMEACCOUNT = 5
    UNKNOWNACCOUNT = 6
    BADGROUP = 7
    MAXIMUM = 8
    MAXIMUMBLOCKED = 9
    INVALIDNOTE = 10

# Com.Ankama.HaapiAnkama.Model.ErrorTwitch
class ErrorTwitch(IntFlag):
    NOTWITCHACCOUNTLINKED = 1
    TWITCHAPIERROR = 2

# Com.Ankama.HaapiAnkama.Model.GameServer
class GameServer(IntFlag):
    DOFUS = 1
    DOFUSRETRO = 2
    DOFUSTOUCH = 3
    WAKFU = 4

# Com.Ankama.HaapiAnkama.Model.GameServerName
class GameServerName(IntFlag):
    En = 1
    Fr = 2
    Es = 3
    Pt = 4

# Com.Ankama.HaapiAnkama.Model.Meta
class Meta(IntFlag):
    SERVICEDENIEDFORCURRENTAPIKEY = 1
    SERVICEDENIEDFORGAMEID = 2
    GAMEBUYERSONLY = 3
    CONNECTPLAYERFAILED = 4

# Com.Ankama.HaapiAnkama.Model.MoneyBalance
class MoneyBalance(IntFlag):
    OGR = 1
    KRZ = 2
    FRG = 3
    GOU = 4

# Com.Ankama.HaapiAnkama.Model.PaymentProcessoutTransaction
class PaymentProcessoutTransaction(IntFlag):
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

# Com.Ankama.HaapiAnkama.Model.ShopArticle
class ShopArticle(IntFlag):
    NORMAL = 1
    PREORDER = 2
    SOONAVAILABLE = 3

# Com.Ankama.HaapiAnkama.Model.ShopBuyError
class ShopBuyError(IntFlag):
    NOPRICE = 1
    STOCKMISSING = 2
    PAIDFAILED = 3
    CANCELFAILED = 4
    CREATEFAILED = 5
    MISSINGMONEY = 6
    PARTNERERROR = 7
    PARTNERMISSING = 8
    PARTNERNOORDER = 9
    RECEIPTALREADYVALIDATED = 10
    TRANSACTIONALREADYVALIDATED = 11
    STEAMUSERSTATUSNOTAUTHORIZED = 12
    PAYMENTCODENOTSENT = 13
    ACCOUNTALREADYHASCHALLENGEDORDER = 14
    CONDITIONFAILED = 15
    INVALIDAMOUNT = 16
    BADTOKEN = 17
    DELETEDTOKEN = 18
    BADTOKENACCOUNT = 19
    BADTOKENCODE = 20
    BADORDER = 21
    INVALIDARTICLEID = 22
    SHOPNOTFOUND = 23
    ARTICLECONDITIONNOTMET = 24
    FAILADDARTICLETOORDER = 25
    FRAUDDETECTED = 26
    WRONGSHOPKEY = 27

# Com.Ankama.HaapiAnkama.Model.ShopBuyResult
class ShopBuyResult(IntFlag):
    PENDING = 1
    CANCELED = 2
    TOPREPARE = 3
    INPROGRESS = 4
    PROCESSED = 5

# Com.Ankama.HaapiAnkama.Model.ShopCharacterUnavailableRestoreReason
class ShopCharacterUnavailableRestoreReason(IntFlag):
    NOREMAININGSLOT = 1

# Com.Ankama.HaapiAnkama.Model.ShopCharacterUnavailableTransferReason
class ShopCharacterUnavailableTransferReason(IntFlag):
    PENDINGACCOUNTTRANSFER = 1
    PENDINGSERVERTRANSFER = 2
    LEVELTOOWEAK = 3
    ACCOUNTGAMEBANNED = 4
    HASDOFUSKAMASDEBT = 5

# Com.Ankama.HaapiAnkama.Model.ShopTargetServerUnavailableReason
class ShopTargetServerUnavailableReason(IntFlag):
    NOSLOTAVAILABLE = 1
    EMPTYSTOCK = 2
    SAMESERVERTRANSFER = 3
    MONOACCOUNTTARGET = 4
    TEMPORISTARGET = 5
    TEMPORISSOURCE = 6
    UNKNOWNSERVER = 7
    BADACCOUNT = 8
    PENDINGSERVERTRANSFER = 9
    PENDINGACCOUNTTRANSFER = 10
    LEVELTOOWEAK = 11
    HASDOFUSKAMASDEBT = 12
    UNAUTHORIZEDSERVER = 13
    UNKNOWNERROR = 14

# Com.Ankama.HaapiAnkama.Model.ShopTransferAccountError
class ShopTransferAccountError(IntFlag):
    BAN = 1
    BLACKLIST = 2
    LOCKED = 3
    DELETED = 4
    OTPTIMEFAILED = 5
    BRUTEFORCE = 6
    FAILED = 7
    MAILNOVALID = 8
    BETACLOSED = 9
    NOACCOUNT = 10
    ACCOUNTLINKED = 11
    ACCOUNTINVALID = 12
    ACCOUNTSHIELDED = 13
    ACCOUNTNOCERTIFY = 14
    RECAPTCHAINVALID = 15
    ANONYMOUSIPFORBIDDEN = 16
    BADOWNER = 17
    ACCOUNTTOOYOUNG = 18
    COPYDATAFAILED = 19
    ACCOUNTNOIDENTITY = 20

# Com.Ankama.HaapiAnkama.Model.ShopTransferValidation
class ShopTransferValidation(IntFlag):
    BAN = 1
    BLACKLIST = 2
    LOCKED = 3
    DELETED = 4
    OTPTIMEFAILED = 5
    BRUTEFORCE = 6
    FAILED = 7
    MAILNOVALID = 8
    BETACLOSED = 9
    NOACCOUNT = 10
    ACCOUNTLINKED = 11
    ACCOUNTINVALID = 12
    ACCOUNTSHIELDED = 13
    ACCOUNTNOCERTIFY = 14
    RECAPTCHAINVALID = 15
    ANONYMOUSIPFORBIDDEN = 16
    BADOWNER = 17
    ACCOUNTTOOYOUNG = 18
    COPYDATAFAILED = 19
    BADACCOUNT = 20
    NOTENOUGHSLOT = 21

