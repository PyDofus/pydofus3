from enum import IntEnum

class SpinCompressionSettings:
	class Mode(IntEnum):
		None_ = 0
		LZ4 = 1

class SpinConnection:
	class Status(IntEnum):
		Disconnected = 0
		Connecting = 1
		Connected = 2
		Disposed = 3

	class QueuedEvent:
		class Type(IntEnum):
			ApplicationMessageReceived = 0
			ConnectionOpened = 1
			ConnectionClosed = 2
			PingStatisticsReceived = 3
			TransportErrorOccurred = 4

class SpinProtocol:
	class AuthenticationError(IntEnum):
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

	class PartnerType(IntEnum):
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

	class ClientType(IntEnum):
		Other = 0
		Web = 1
		Standalone = 2

	class OsType(IntEnum):
		Other = 0
		Android = 1
		IOS = 2
		Windows = 3
		MacOS = 4
		Linux = 5

	class DeviceType(IntEnum):
		Other = 0
		Phone = 1
		Tablet = 2
		Computer = 3

class SpinRemoteCompressionSupport(IntEnum):
	Unknown = 0
	Supported = 1
	Unsupported = 2

class SpinTransportError(IntEnum):
	None_ = 0
	MessageProcessingError = 1
	MessageSizeIsTooSmall = 2
	MessageSizeLimitExceeded = 3
	AuthenticationWindowExpired = 4
	AuthenticationRequestTimeout = 5
	MalformedAuthenticationData = 6
	MalformedSpinMessageData = 7
	MalformedApplicationMessageData = 8
	UnsupportedCompressedApplicationMessageReceived = 9

