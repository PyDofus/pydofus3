from enum import IntFlag

# Unity.IO.LowLevel.Unsafe.AssetLoadingSubsystem
class AssetLoadingSubsystem(IntFlag):
    Other = 0
    Texture = 1
    VirtualTexture = 2
    Mesh = 3
    Audio = 4
    Scripts = 5
    EntitiesScene = 6
    EntitiesStreamBinaryReader = 7
    FileInfo = 8
    ContentLoading = 9

# Unity.IO.LowLevel.Unsafe.FileReadType
class FileReadType(IntFlag):
    Sync = 0
    Async = 1

# Unity.IO.LowLevel.Unsafe.FileState
class FileState(IntFlag):
    Absent = 0
    Exists = 1

# Unity.IO.LowLevel.Unsafe.Priority
class Priority(IntFlag):
    PriorityLow = 0
    PriorityHigh = 1

# Unity.IO.LowLevel.Unsafe.ProcessingState
class ProcessingState(IntFlag):
    Unknown = 0
    InQueue = 1
    Reading = 2
    Completed = 3
    Failed = 4
    Canceled = 5

# Unity.IO.LowLevel.Unsafe.ReadStatus
class ReadStatus(IntFlag):
    Complete = 0
    InProgress = 1
    Failed = 2
    Truncated = 4
    Canceled = 5

