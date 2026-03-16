from enum import IntEnum

class ExceptionType(IntEnum):
	HandledByThisPolicy = 0
	Unhandled = 1

class FaultType(IntEnum):
	ExceptionHandledByThisPolicy = 0
	UnhandledException = 1
	ResultHandledByThisPolicy = 2

class OutcomeType(IntEnum):
	Successful = 0
	Failure = 1

