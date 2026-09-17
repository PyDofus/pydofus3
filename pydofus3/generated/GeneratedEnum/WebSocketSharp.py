from enum import IntEnum

class ByteOrder(IntEnum):
	Little = 0
	Big = 1

class CloseStatusCode(IntEnum):
	Normal = 1000
	Away = 1001
	ProtocolError = 1002
	UnsupportedData = 1003
	Undefined = 1004
	NoStatus = 1005
	Abnormal = 1006
	InvalidData = 1007
	PolicyViolation = 1008
	TooBig = 1009
	MandatoryExtension = 1010
	ServerError = 1011
	TlsHandshakeFailure = 1015

class CompressionMethod(IntEnum):
	None_ = 0
	Deflate = 1

class Fin(IntEnum):
	More = 0
	Final = 1

class LogLevel(IntEnum):
	Trace = 0
	Debug = 1
	Info = 2
	Warn = 3
	Error = 4
	Fatal = 5

class Mask(IntEnum):
	Off = 0
	On = 1

class Opcode(IntEnum):
	Cont = 0
	Text = 1
	Binary = 2
	Close = 8
	Ping = 9
	Pong = 10

class Rsv(IntEnum):
	Off = 0
	On = 1

class WebSocketState(IntEnum):
	Connecting = 0
	Open = 1
	Closing = 2
	Closed = 3

