from enum import IntEnum

class TcpConnectionLayer:
	class Status(IntEnum):
		Disconnected = 0
		Connecting = 1
		Connected = 2
		Disposed = 3

