from enum import IntFlag

# Ankama.Utilities.Device
class Device(IntFlag):
    PC = 0
    Mobile = 1
    Tablet = 2

# Ankama.Utilities.StreamingAssetRequest
class StreamingAssetRequest(IntFlag):
    InProgress = 0
    Success = 1
    Error = 2
    FileNotFoundError = 3
    AccessDeniedError = 4

