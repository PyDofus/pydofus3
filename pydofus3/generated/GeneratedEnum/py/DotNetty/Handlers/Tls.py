from enum import IntFlag

# DotNetty.Handlers.Tls.TlsHandlerState
class TlsHandlerState(IntFlag):
    Authenticating = 1
    Authenticated = 2
    FailedAuthentication = 4
    ReadRequestedBeforeAuthenticated = 8
    FlushedBeforeHandshake = 16
    AuthenticationStarted = 7
    AuthenticationCompleted = 6

