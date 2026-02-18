from enum import IntFlag

# UnityEngine.ResourceManagement.Profiling.BundleOptions
class BundleOptions(IntFlag):
    NONE = 0
    CachingEnabled = 1
    CheckSumEnabled = 2

# UnityEngine.ResourceManagement.Profiling.ContentStatus
class ContentStatus(IntFlag):
    NONE = 0
    Queue = 2
    Downloading = 4
    Released = 16
    Loading = 64
    Active = 256

