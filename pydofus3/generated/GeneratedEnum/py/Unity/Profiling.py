from enum import IntFlag

# Unity.Profiling.ProfilerCategoryColor
class ProfilerCategoryColor(IntFlag):
    Render = 0
    Scripts = 1
    BurstJobs = 2
    Other = 3
    Physics = 4
    Animation = 5
    Audio = 6
    AudioJob = 7
    AudioUpdateJob = 8
    Lighting = 9
    GC = 10
    VSync = 11
    Memory = 12
    Internal = 13
    UI = 14
    Build = 15
    Input = 16

# Unity.Profiling.ProfilerCounterOptions
class ProfilerCounterOptions(IntFlag):
    NONE = 0
    FlushOnEndOfFrame = 2
    ResetToZeroOnFlush = 4

# Unity.Profiling.ProfilerMarkerDataUnit
class ProfilerMarkerDataUnit(IntFlag):
    Undefined = 0
    TimeNanoseconds = 1
    Bytes = 2
    Count = 3
    Percent = 4
    FrequencyHz = 5

# Unity.Profiling.ProfilerRecorder
class ProfilerRecorder(IntFlag):
    Start = 0
    Stop = 1
    Reset = 2
    Release = 4
    SetFilterToCurrentThread = 5
    SetToCollectFromAllThreads = 6

# Unity.Profiling.ProfilerRecorder
class ProfilerRecorder(IntFlag):
    Count = 0
    MaxCount = 1

# Unity.Profiling.ProfilerRecorderOptions
class ProfilerRecorderOptions(IntFlag):
    NONE = 0
    StartImmediately = 1
    KeepAliveDuringDomainReload = 2
    CollectOnlyOnCurrentThread = 4
    WrapAroundWhenCapacityReached = 8
    SumAllSamplesInFrame = 16
    GpuRecorder = 64
    Default = 24

