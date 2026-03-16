from enum import IntFlag

class TlsHandlerState(IntFlag):
	Authenticating = 1
	Authenticated = 2
	FailedAuthentication = 4
	AuthenticationCompleted = 6
	AuthenticationStarted = 7
	ReadRequestedBeforeAuthenticated = 8
	FlushedBeforeHandshake = 16

