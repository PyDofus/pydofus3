from enum import IntEnum
from enum import IntFlag

class DisplayConfiguration:
	class Flags(IntFlag):
		None_ = 0
		Fallback = 1

class DisplayConfigurationRequestParameters:
	class OptionalProperties(IntEnum):
		None_ = 0
		HdrSupport = 1

	class Windows:
		class DisplayModeEnumerationFlags(IntFlag):
			None_ = 0
			IncludeInterlaced = 1
			IncludeStretchedScaling = 2
			IncludeStereo = 4
			IncludeDisabledStereo = 8

class DisplayHdrSupport(IntEnum):
	None_ = 0
	Available = 1
	Enabled = 2
	ForceDisabled = 4

class DisplayInfo:
	class Flags(IntFlag):
		None_ = 0
		Set = 1
		Primary = 2

class DisplayInfoComparisonMask(IntFlag):
	None_ = 0
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

class DisplayRotation(IntEnum):
	Default = 0
	ClockWise90 = 1
	ClockWise180 = 2
	ClockWise270 = 3

class ScreenManagerError(IntEnum):
	None_ = 0
	Busy = 1
	SystemCallFailure = 2

class WindowPosition:
	class Type(IntEnum):
		Auto = 0
		Centered = 1
		Explicit = 2

class WindowSizeConstraints:
	class Flags(IntFlag):
		None_ = 0
		MinSize = 1
		MaxSize = 2

class WindowState(IntEnum):
	Unknown = 0
	Restored = 1
	Minimized = 2
	Maximized = 3

