from enum import IntFlag

# Ankama.Logging.LogLevel
class LogLevel(IntFlag):
    NONE = 0
    Exception = 1
    Assert = 2
    Error = 3
    Warning = 4
    Info = 5
    Debug = 6

