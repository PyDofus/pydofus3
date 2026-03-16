from enum import IntEnum

class TTransportException:
	class ExceptionType(IntEnum):
		Unknown = 0
		NotOpen = 1
		AlreadyOpen = 2
		TimedOut = 3
		EndOfFile = 4
		Interrupted = 5

