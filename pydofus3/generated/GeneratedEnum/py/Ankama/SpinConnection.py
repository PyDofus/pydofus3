from enum import IntFlag

# Ankama.SpinConnection.SpinProtocol
class SpinProtocol(IntFlag):
    NoneOrOtherOrUnknown = 0
    BadCredentials = 1
    InvalidAuthenticationInfo = 2
    SubscriptionRequired = 3
    AdminRightsRequired = 4
    AccountKnownButBanned = 5
    AccountKnownButBlocked = 6
    IpAddressRefused = 7
    BetaAccessRequired = 8
    ServerTimeout = 9
    ServerError = 10
    AccountsBackendError = 11
    NickNameRequired = 12
    EmailNeedsValidation = 13
    ReCaptchaInvalid = 14
    BadClientVersion = 15
    ServerNotYetReady = 16

# Ankama.SpinConnection.SpinProtocol
class SpinProtocol(IntFlag):
    NONE = 0
    BigPoint = 1
    LikeVN = 2
    Steam = 3

# Ankama.SpinConnection.SpinProtocol
class SpinProtocol(IntFlag):
    Application = 0
    Ping = 1
    Pong = 2
    Heartbeat = 3
    ApplicationCompressed = 4
    Capabilities = 5

# Ankama.SpinConnection.SpinProtocol
class SpinProtocol(IntFlag):
    Compression = 0

