from enum import IntFlag

# UnityEngine.Networking.DownloadedTextureFlags
class DownloadedTextureFlags(IntFlag):
    NONE = 0
    Readable = 1
    MipmapChain = 2
    LinearColorSpace = 4

# UnityEngine.Networking.UnityWebRequest
class UnityWebRequest(IntFlag):
    Get = 0
    Post = 1
    Put = 2
    Head = 3
    Custom = 4

# UnityEngine.Networking.UnityWebRequest
class UnityWebRequest(IntFlag):
    OK = 0
    OKCached = 1
    Unknown = 2
    SDKError = 3
    UnsupportedProtocol = 4
    MalformattedUrl = 5
    CannotResolveProxy = 6
    CannotResolveHost = 7
    CannotConnectToHost = 8
    AccessDenied = 9
    GenericHttpError = 10
    WriteError = 11
    ReadError = 12
    OutOfMemory = 13
    Timeout = 14
    HTTPPostError = 15
    SSLCannotConnect = 16
    Aborted = 17
    TooManyRedirects = 18
    ReceivedNoData = 19
    SSLNotSupported = 20
    FailedToSendData = 21
    FailedToReceiveData = 22
    SSLCertificateError = 23
    SSLCipherNotAvailable = 24
    SSLCACertError = 25
    UnrecognizedContentEncoding = 26
    LoginFailed = 27
    SSLShutdownFailed = 28
    RedirectLimitInvalid = 29
    InvalidRedirect = 30
    CannotModifyRequest = 31
    HeaderNameContainsInvalidCharacters = 32
    HeaderValueContainsInvalidCharacters = 33
    CannotOverrideSystemHeaders = 34
    AlreadySent = 35
    InvalidMethod = 36
    NotImplemented = 37
    NoInternetConnection = 38
    DataProcessingError = 39
    InsecureConnectionNotAllowed = 40

# UnityEngine.Networking.UnityWebRequest
class UnityWebRequest(IntFlag):
    InProgress = 0
    Success = 1
    ConnectionError = 2
    ProtocolError = 3
    DataProcessingError = 4

