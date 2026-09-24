from enum import IntEnum

class DisconnectionSource(IntEnum):
	None_ = 0
	Client = 1
	Transport = 2
	Network = 3
	Runtime = 4

class PingStatisticsSettings:
	class Mode(IntEnum):
		Disabled = 0
		Enabled = 1

class TcpNetworkLayer:
	class Status(IntEnum):
		Disconnected = 0
		Connecting = 1
		Connected = 2
		Disposed = 3

