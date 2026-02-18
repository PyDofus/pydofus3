from enum import IntFlag

# RestSharp.Authenticators.OAuth.HttpPostParameterType
class HttpPostParameterType(IntFlag):
    Field = 0
    File = 1

# RestSharp.Authenticators.OAuth.OAuthParameterHandling
class OAuthParameterHandling(IntFlag):
    HttpAuthorizationHeader = 0
    UrlOrPostParameters = 1

# RestSharp.Authenticators.OAuth.OAuthSignatureMethod
class OAuthSignatureMethod(IntFlag):
    HmacSha1 = 0
    HmacSha256 = 1
    PlainText = 2
    RsaSha1 = 3

# RestSharp.Authenticators.OAuth.OAuthSignatureTreatment
class OAuthSignatureTreatment(IntFlag):
    Escaped = 0
    Unescaped = 1

# RestSharp.Authenticators.OAuth.OAuthType
class OAuthType(IntFlag):
    RequestToken = 0
    AccessToken = 1
    ProtectedResource = 2
    ClientAuthentication = 3

