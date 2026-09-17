from enum import IntEnum
from enum import IntFlag

class AuthenticationSchemes(IntEnum):
	None_ = 0
	Digest = 1
	Basic = 8
	Anonymous = 32768

class HttpHeaderType(IntFlag):
	Unspecified = 0
	Request = 1
	Response = 2
	Restricted = 4
	MultiValue = 8
	MultiValueInRequest = 16
	MultiValueInResponse = 32

class HttpRequestHeader(IntEnum):
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
	SecWebSocketKey = 41
	SecWebSocketExtensions = 42
	SecWebSocketProtocol = 43
	SecWebSocketVersion = 44

class HttpResponseHeader(IntEnum):
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
	AcceptRanges = 20
	Age = 21
	ETag = 22
	Location = 23
	ProxyAuthenticate = 24
	RetryAfter = 25
	Server = 26
	SetCookie = 27
	Vary = 28
	WwwAuthenticate = 29
	SecWebSocketExtensions = 30
	SecWebSocketAccept = 31
	SecWebSocketProtocol = 32
	SecWebSocketVersion = 33

class HttpStatusCode(IntEnum):
	Continue = 100
	SwitchingProtocols = 101
	OK = 200
	Created = 201
	Accepted = 202
	NonAuthoritativeInformation = 203
	NoContent = 204
	ResetContent = 205
	PartialContent = 206
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
	InternalServerError = 500
	NotImplemented = 501
	BadGateway = 502
	ServiceUnavailable = 503
	GatewayTimeout = 504
	HttpVersionNotSupported = 505

class InputChunkState(IntEnum):
	None_ = 0
	Data = 1
	DataEnded = 2
	Trailer = 3
	End = 4

class InputState(IntEnum):
	RequestLine = 0
	Headers = 1

class LineState(IntEnum):
	None_ = 0
	Cr = 1
	Lf = 2

