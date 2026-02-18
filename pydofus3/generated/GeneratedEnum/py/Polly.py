from enum import IntFlag

# Polly.ExceptionType
class ExceptionType(IntFlag):
    HandledByThisPolicy = 0
    Unhandled = 1

# Polly.FaultType
class FaultType(IntFlag):
    ExceptionHandledByThisPolicy = 0
    UnhandledException = 1
    ResultHandledByThisPolicy = 2

# Polly.OutcomeType
class OutcomeType(IntFlag):
    Successful = 0
    Failure = 1

