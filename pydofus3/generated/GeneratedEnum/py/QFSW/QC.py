from enum import IntFlag

# QFSW.QC.ActionState
class ActionState(IntFlag):
    Unknown = 0
    Running = 1
    Complete = 2

# QFSW.QC.AutoScrollOptions
class AutoScrollOptions(IntFlag):
    Never = 0
    OnInvoke = 1
    Always = 2

# QFSW.QC.LoggingLevel
class LoggingLevel(IntFlag):
    NONE = 0
    Errors = 1
    Warnings = 2
    Full = 3

# QFSW.QC.LoggingThreshold
class LoggingThreshold(IntFlag):
    Never = 0
    Exception = 1
    Error = 2
    Warning = 3
    Always = 4

# QFSW.QC.MonoTargetType
class MonoTargetType(IntFlag):
    Single = 0
    All = 1
    Registry = 2
    Singleton = 3
    SingleInactive = 4
    AllInactive = 5

# QFSW.QC.Platform
class Platform(IntFlag):
    OSXEditor = 1
    OSXPlayer = 2
    WindowsPlayer = 4
    OSXWebPlayer = 8
    OSXDashboardPlayer = 16
    WindowsWebPlayer = 32
    WindowsEditor = 128
    IPhonePlayer = 256
    PS3 = 512
    XBOX360 = 1024
    Android = 2048
    NaCl = 4096
    LinuxPlayer = 8192
    FlashPlayer = 32768
    LinuxEditor = 65536
    WebGLPlayer = 131072
    MetroPlayerX86 = 262144
    WSAPlayerX86 = 262144
    MetroPlayerX64 = 524288
    WSAPlayerX64 = 524288
    MetroPlayerARM = 1048576
    WSAPlayerARM = 1048576
    WP8Player = 2097152
    BlackBerryPlayer = 4194304
    TizenPlayer = 8388608
    PSP2 = 16777216
    PS4 = 33554432
    PSM = 67108864
    XboxOne = 134217728
    SamsungTVPlayer = 268435456
    WiiU = 1073741824
    tvOS = 2147483648
    Switch = 4294967296
    Lumin = 8589934592
    Stadia = 17179869184
    NONE = 0
    AllPlatforms = -1
    EditorPlatforms = 65665
    BuildPlatforms = -65666
    MobilePlatforms = 2099456

# QFSW.QC.ScanRuleResult
class ScanRuleResult(IntFlag):
    Accept = 0
    Reject = 1
    ForceAccept = 2

# QFSW.QC.SortOrder
class SortOrder(IntFlag):
    Ascending = 0
    Descending = 1

# QFSW.QC.SupportedState
class SupportedState(IntFlag):
    Always = 0
    Development = 1
    Editor = 2
    Never = 3

