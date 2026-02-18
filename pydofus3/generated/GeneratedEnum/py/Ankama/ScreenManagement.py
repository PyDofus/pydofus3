from enum import IntFlag

# Ankama.ScreenManagement.DisplayConfiguration
class DisplayConfiguration(IntFlag):
    NONE = 0
    Fallback = 1

# Ankama.ScreenManagement.DisplayConfigurationRequestParameters
class DisplayConfigurationRequestParameters(IntFlag):
    NONE = 0
    HdrSupport = 1

# Ankama.ScreenManagement.DisplayConfigurationRequestParameters
class DisplayConfigurationRequestParameters(IntFlag):
    NONE = 0
    IncludeInterlaced = 1
    IncludeStretchedScaling = 2
    IncludeStereo = 4
    IncludeDisabledStereo = 8

# Ankama.ScreenManagement.DisplayHdrSupport
class DisplayHdrSupport(IntFlag):
    NONE = 0
    Available = 1
    Enabled = 2
    ForceDisabled = 4

# Ankama.ScreenManagement.DisplayInfo
class DisplayInfo(IntFlag):
    NONE = 0
    Set = 1
    Primary = 2

# Ankama.ScreenManagement.DisplayInfoComparisonMask
class DisplayInfoComparisonMask(IntFlag):
    NONE = 0
    Name = 1
    AdapterName = 2
    Frame = 4
    WorkArea = 8
    CurrentResolution = 16
    Rotation = 32
    HDRSupport = 64
    PreferredResolution = 128
    IsPrimaryDisplay = 256
    Default = 511
    Everything = 511

# Ankama.ScreenManagement.DisplayRotation
class DisplayRotation(IntFlag):
    Default = 0
    ClockWise90 = 1
    ClockWise180 = 2
    ClockWise270 = 3

# Ankama.ScreenManagement.ScreenManagerError
class ScreenManagerError(IntFlag):
    NONE = 0
    Busy = 1
    SystemCallFailure = 2

# Ankama.ScreenManagement.WindowPosition
class WindowPosition(IntFlag):
    Auto = 0
    Centered = 1
    Explicit = 2

# Ankama.ScreenManagement.WindowSizeConstraints
class WindowSizeConstraints(IntFlag):
    NONE = 0
    MinSize = 1
    MaxSize = 2

# Ankama.ScreenManagement.WindowState
class WindowState(IntFlag):
    Unknown = 0
    Restored = 1
    Minimized = 2
    Maximized = 3

