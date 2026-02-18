from enum import IntFlag

# System.Runtime.ConstrainedExecution.Cer
class Cer(IntFlag):
    NONE = 0
    MayFail = 1
    Success = 2

# System.Runtime.ConstrainedExecution.Consistency
class Consistency(IntFlag):
    MayCorruptProcess = 0
    MayCorruptAppDomain = 1
    MayCorruptInstance = 2
    WillNotCorruptState = 3

