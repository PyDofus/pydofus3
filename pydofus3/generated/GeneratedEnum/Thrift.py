from enum import IntEnum

class TApplicationException:
	class ExceptionType(IntEnum):
		Unknown = 0
		UnknownMethod = 1
		InvalidMessageType = 2
		WrongMethodName = 3
		BadSequenceID = 4
		MissingResult = 5
		InternalError = 6
		ProtocolError = 7
		InvalidTransform = 8
		InvalidProtocol = 9
		UnsupportedClientType = 10

