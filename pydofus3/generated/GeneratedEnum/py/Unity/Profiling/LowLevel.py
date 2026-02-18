from enum import IntFlag

# Unity.Profiling.LowLevel.MarkerFlags
class MarkerFlags(IntFlag):
    Default = 0
    Script = 2
    ScriptInvoke = 32
    ScriptDeepProfiler = 64
    AvailabilityEditor = 4
    AvailabilityNonDevelopment = 8
    Warning = 16
    Counter = 128
    SampleGPU = 256

# Unity.Profiling.LowLevel.ProfilerMarkerDataType
class ProfilerMarkerDataType(IntFlag):
    InstanceId = 1
    Int32 = 2
    UInt32 = 3
    Int64 = 4
    UInt64 = 5
    Float = 6
    Double = 7
    String16 = 9
    Blob8 = 11
    GfxResourceId = 12

