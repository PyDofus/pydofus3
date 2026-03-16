from enum import IntEnum
from enum import IntFlag

class ActionState(IntEnum):
	Unknown = 0
	Running = 1
	Complete = 2

class AutoScrollOptions(IntEnum):
	Never = 0
	OnInvoke = 1
	Always = 2

class LoggingLevel(IntEnum):
	None_ = 0
	Errors = 1
	Warnings = 2
	Full = 3

class LoggingThreshold(IntEnum):
	Never = 0
	Exception = 1
	Error = 2
	Warning = 3
	Always = 4

class MonoTargetType(IntEnum):
	Single = 0
	All = 1
	Registry = 2
	Singleton = 3
	SingleInactive = 4
	AllInactive = 5

class Platform(IntFlag):
	BuildPlatforms = -65666
	AllPlatforms = -1
	None_ = 0
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
	EditorPlatforms = 65665
	WebGLPlayer = 131072
	MetroPlayerX86 = 262144
	WSAPlayerX86 = 262144
	MetroPlayerX64 = 524288
	WSAPlayerX64 = 524288
	MetroPlayerARM = 1048576
	WSAPlayerARM = 1048576
	WP8Player = 2097152
	MobilePlatforms = 2099456
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

class ScanRuleResult(IntEnum):
	Accept = 0
	Reject = 1
	ForceAccept = 2

class SortOrder(IntEnum):
	Ascending = 0
	Descending = 1

class SupportedState(IntEnum):
	Always = 0
	Development = 1
	Editor = 2
	Never = 3

