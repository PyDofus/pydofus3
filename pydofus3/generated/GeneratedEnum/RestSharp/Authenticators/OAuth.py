from enum import IntEnum

class HttpPostParameterType(IntEnum):
	Field = 0
	File = 1

class OAuthParameterHandling(IntEnum):
	HttpAuthorizationHeader = 0
	UrlOrPostParameters = 1

class OAuthSignatureMethod(IntEnum):
	HmacSha1 = 0
	HmacSha256 = 1
	PlainText = 2
	RsaSha1 = 3

class OAuthSignatureTreatment(IntEnum):
	Escaped = 0
	Unescaped = 1

class OAuthType(IntEnum):
	RequestToken = 0
	AccessToken = 1
	ProtectedResource = 2
	ClientAuthentication = 3

