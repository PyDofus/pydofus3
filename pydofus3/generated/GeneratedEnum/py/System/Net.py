from enum import IntFlag

# System.Net.AuthenticationSchemes
class AuthenticationSchemes(IntFlag):
    NONE = 0
    Digest = 1
    Negotiate = 2
    Ntlm = 4
    Basic = 8
    Anonymous = 32768
    IntegratedWindowsAuthentication = 6

# System.Net.CloseExState
class CloseExState(IntFlag):
    Normal = 0
    Abort = 1
    Silent = 2

# System.Net.CommandStream
class CommandStream(IntFlag):
    Abort = 0
    Advance = 1
    Pause = 2
    Reread = 3
    GiveStream = 4

# System.Net.CommandStream
class CommandStream(IntFlag):
    UserCommand = 1
    GiveDataStream = 2
    CreateDataConnection = 4
    DontLogParameter = 8

# System.Net.ContentDecodeStream
class ContentDecodeStream(IntFlag):
    GZip = 0
    Deflate = 1

# System.Net.ContextAwareResult
class ContextAwareResult(IntFlag):
    NONE = 0
    CaptureIdentity = 1
    CaptureContext = 2
    ThreadSafeContextCopy = 4
    PostBlockStarted = 8
    PostBlockFinished = 16

# System.Net.CookieCollection
class CookieCollection(IntFlag):
    Check = 0
    Set = 1
    SetToUnused = 2
    SetToMaxUsed = 3

# System.Net.CookieToken
class CookieToken(IntFlag):
    Nothing = 0
    NameValuePair = 1
    Attribute = 2
    EndToken = 3
    EndCookie = 4
    End = 5
    Equals = 6
    Comment = 7
    CommentUrl = 8
    CookieName = 9
    Discard = 10
    Domain = 11
    Expires = 12
    MaxAge = 13
    Path = 14
    Port = 15
    Secure = 16
    HttpOnly = 17
    Unknown = 18
    Version = 19

# System.Net.CookieVariant
class CookieVariant(IntFlag):
    Unknown = 0
    Plain = 1
    Rfc2109 = 2
    Rfc2965 = 3
    Default = 2

# System.Net.DecompressionMethods
class DecompressionMethods(IntFlag):
    NONE = 0
    GZip = 1
    Deflate = 2

# System.Net.FtpControlStream
class FtpControlStream(IntFlag):
    Normal = 0
    AssumeFilename = 1
    AssumeNoFilename = 2

# System.Net.FtpLoginState
class FtpLoginState(IntFlag):
    NotLoggedIn = 0
    LoggedIn = 1
    LoggedInButNeedsRelogin = 2
    ReloginFailed = 3

# System.Net.FtpMethodFlags
class FtpMethodFlags(IntFlag):
    NONE = 0
    IsDownload = 1
    IsUpload = 2
    TakesParameter = 4
    MayTakeParameter = 8
    DoesNotTakeParameter = 16
    ParameterIsDirectory = 32
    ShouldParseForResponseUri = 64
    HasHttpCommand = 128
    MustChangeWorkingDirectoryToPath = 256

# System.Net.FtpOperation
class FtpOperation(IntFlag):
    DownloadFile = 0
    ListDirectory = 1
    ListDirectoryDetails = 2
    UploadFile = 3
    UploadFileUnique = 4
    AppendFile = 5
    DeleteFile = 6
    GetDateTimestamp = 7
    GetFileSize = 8
    Rename = 9
    MakeDirectory = 10
    RemoveDirectory = 11
    PrintWorkingDirectory = 12
    Other = 13

# System.Net.FtpStatusCode
class FtpStatusCode(IntFlag):
    Undefined = 0
    RestartMarker = 110
    ServiceTemporarilyNotAvailable = 120
    DataAlreadyOpen = 125
    OpeningData = 150
    CommandOK = 200
    CommandExtraneous = 202
    DirectoryStatus = 212
    FileStatus = 213
    SystemType = 215
    SendUserCommand = 220
    ClosingControl = 221
    ClosingData = 226
    EnteringPassive = 227
    LoggedInProceed = 230
    ServerWantsSecureSession = 234
    FileActionOK = 250
    PathnameCreated = 257
    SendPasswordCommand = 331
    NeedLoginAccount = 332
    FileCommandPending = 350
    ServiceNotAvailable = 421
    CantOpenData = 425
    ConnectionClosed = 426
    ActionNotTakenFileUnavailableOrBusy = 450
    ActionAbortedLocalProcessingError = 451
    ActionNotTakenInsufficientSpace = 452
    CommandSyntaxError = 500
    ArgumentSyntaxError = 501
    CommandNotImplemented = 502
    BadCommandSequence = 503
    NotLoggedIn = 530
    AccountNeeded = 532
    ActionNotTakenFileUnavailable = 550
    ActionAbortedUnknownPageType = 551
    FileActionAborted = 552
    ActionNotTakenFilenameNotAllowed = 553

# System.Net.FtpWebRequest
class FtpWebRequest(IntFlag):
    CheckForError = 0
    RequestStarted = 1
    WriteReady = 2
    ReadReady = 3
    ReleaseConnection = 4

# System.Net.HttpConnection
class HttpConnection(IntFlag):
    RequestLine = 0
    Headers = 1

# System.Net.HttpConnection
class HttpConnection(IntFlag):
    NONE = 0
    CR = 1
    LF = 2

# System.Net.HttpListenerRequestUriBuilder
class HttpListenerRequestUriBuilder(IntFlag):
    Success = 0
    InvalidString = 1
    EncodingError = 2

# System.Net.HttpListenerRequestUriBuilder
class HttpListenerRequestUriBuilder(IntFlag):
    Primary = 0
    Secondary = 1

# System.Net.HttpRequestHeader
class HttpRequestHeader(IntFlag):
    CacheControl = 0
    Connection = 1
    Date = 2
    KeepAlive = 3
    Pragma = 4
    Trailer = 5
    TransferEncoding = 6
    Upgrade = 7
    Via = 8
    Warning = 9
    Allow = 10
    ContentLength = 11
    ContentType = 12
    ContentEncoding = 13
    ContentLanguage = 14
    ContentLocation = 15
    ContentMd5 = 16
    ContentRange = 17
    Expires = 18
    LastModified = 19
    Accept = 20
    AcceptCharset = 21
    AcceptEncoding = 22
    AcceptLanguage = 23
    Authorization = 24
    Cookie = 25
    Expect = 26
    From = 27
    Host = 28
    IfMatch = 29
    IfModifiedSince = 30
    IfNoneMatch = 31
    IfRange = 32
    IfUnmodifiedSince = 33
    MaxForwards = 34
    ProxyAuthorization = 35
    Referer = 36
    Range = 37
    Te = 38
    Translate = 39
    UserAgent = 40

# System.Net.HttpStatusCode
class HttpStatusCode(IntFlag):
    Continue = 100
    SwitchingProtocols = 101
    Processing = 102
    EarlyHints = 103
    OK = 200
    Created = 201
    Accepted = 202
    NonAuthoritativeInformation = 203
    NoContent = 204
    ResetContent = 205
    PartialContent = 206
    MultiStatus = 207
    AlreadyReported = 208
    IMUsed = 226
    MultipleChoices = 300
    Ambiguous = 300
    MovedPermanently = 301
    Moved = 301
    Found = 302
    Redirect = 302
    SeeOther = 303
    RedirectMethod = 303
    NotModified = 304
    UseProxy = 305
    Unused = 306
    TemporaryRedirect = 307
    RedirectKeepVerb = 307
    PermanentRedirect = 308
    BadRequest = 400
    Unauthorized = 401
    PaymentRequired = 402
    Forbidden = 403
    NotFound = 404
    MethodNotAllowed = 405
    NotAcceptable = 406
    ProxyAuthenticationRequired = 407
    RequestTimeout = 408
    Conflict = 409
    Gone = 410
    LengthRequired = 411
    PreconditionFailed = 412
    RequestEntityTooLarge = 413
    RequestUriTooLong = 414
    UnsupportedMediaType = 415
    RequestedRangeNotSatisfiable = 416
    ExpectationFailed = 417
    MisdirectedRequest = 421
    UnprocessableEntity = 422
    Locked = 423
    FailedDependency = 424
    UpgradeRequired = 426
    PreconditionRequired = 428
    TooManyRequests = 429
    RequestHeaderFieldsTooLarge = 431
    UnavailableForLegalReasons = 451
    InternalServerError = 500
    NotImplemented = 501
    BadGateway = 502
    ServiceUnavailable = 503
    GatewayTimeout = 504
    HttpVersionNotSupported = 505
    VariantAlsoNegotiates = 506
    InsufficientStorage = 507
    LoopDetected = 508
    NotExtended = 510
    NetworkAuthenticationRequired = 511

# System.Net.HttpWebRequest
class HttpWebRequest(IntFlag):
    NONE = 0
    Challenge = 1
    Response = 2

# System.Net.MonoChunkParser
class MonoChunkParser(IntFlag):
    NONE = 0
    PartialSize = 1
    Body = 2
    BodyFinished = 3
    Trailer = 4

# System.Net.ReadState
class ReadState(IntFlag):
    NONE = 0
    Status = 1
    Headers = 2
    Content = 3
    Aborted = 4

# System.Net.SecurityProtocolType
class SecurityProtocolType(IntFlag):
    SystemDefault = 0
    Ssl3 = 48
    Tls = 192
    Tls11 = 768
    Tls12 = 3072
    Tls13 = 12288

# System.Net.TimerThread
class TimerThread(IntFlag):
    Ready = 0
    Fired = 1
    Cancelled = 2
    Sentinel = 3

# System.Net.TriState
class TriState(IntFlag):
    Unspecified = -1
    FALSE = 0
    TRUE = 1

# System.Net.WebCompletionSource
class WebCompletionSource(IntFlag):
    Running = 0
    Completed = 1
    Canceled = 2
    Faulted = 3

# System.Net.WebConnectionTunnel
class WebConnectionTunnel(IntFlag):
    NONE = 0
    Challenge = 1
    Response = 2

# System.Net.WebExceptionInternalStatus
class WebExceptionInternalStatus(IntFlag):
    RequestFatal = 0
    ServicePointFatal = 1
    Recoverable = 2
    Isolated = 3

# System.Net.WebExceptionStatus
class WebExceptionStatus(IntFlag):
    Success = 0
    NameResolutionFailure = 1
    ConnectFailure = 2
    ReceiveFailure = 3
    SendFailure = 4
    PipelineFailure = 5
    RequestCanceled = 6
    ProtocolError = 7
    ConnectionClosed = 8
    TrustFailure = 9
    SecureChannelFailure = 10
    ServerProtocolViolation = 11
    KeepAliveFailure = 12
    Pending = 13
    Timeout = 14
    ProxyNameResolutionFailure = 15
    UnknownError = 16
    MessageLengthLimitExceeded = 17
    CacheEntryNotFound = 18
    RequestProhibitedByCachePolicy = 19
    RequestProhibitedByProxy = 20

# System.Net.WebHeaderCollection
class WebHeaderCollection(IntFlag):
    High = 0
    Reg = 1
    Ctl = 2
    CR = 3
    LF = 4
    WS = 5
    Colon = 6
    Delim = 7

# System.Net.WebHeaderCollectionType
class WebHeaderCollectionType(IntFlag):
    Unknown = 0
    WebRequest = 1
    WebResponse = 2
    HttpWebRequest = 3
    HttpWebResponse = 4
    HttpListenerRequest = 5
    HttpListenerResponse = 6
    FtpWebRequest = 7
    FtpWebResponse = 8
    FileWebRequest = 9
    FileWebResponse = 10

