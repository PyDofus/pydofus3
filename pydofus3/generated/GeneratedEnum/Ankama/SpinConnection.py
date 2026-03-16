from enum import IntEnum

class SpinConnection[TCommand, TEvent]:
	class Status(IntEnum):
		Disconnected = 0
		Connecting = 1
		Connected = 2
		Disposed = 3

class SpinProtocol:
	class ConnectionErrors(IntEnum):
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

	class Partner(IntEnum):
		None_ = 0
		BigPoint = 1
		LikeVN = 2
		Steam = 3

	class MessageType(IntEnum):
		Application = 0
		Ping = 1
		Pong = 2
		Heartbeat = 3
		ApplicationCompressed = 4
		Capabilities = 5

	class Capabilities(IntEnum):
		Compression = 0

