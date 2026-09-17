from enum import IntEnum
from enum import IntFlag

class CoordinateConversion(IntEnum):
	None_ = 0
	Local = 1
	WorldToScreenPoint = 2
	WorldToViewportPoint = 3
	ScreenToWorldPoint = 4
	ScreenToViewportPoint = 5
	ViewportToWorldPoint = 6
	ViewportToScreenPoint = 7

class LogFilter(IntFlag):
	None_ = 0
	Input = 1
	Input_Mouse = 2
	Input_Keyboard = 4
	Input_Touch = 8
	Input_Gamepad = 16
	Input_XR = 32
	Input_UIToolkit = 64
	MessageHandler = 128
	MessageHandler_ObjectValue = 256

class RuntimePlatform(IntEnum):
	OSXEditor = 0
	OSXPlayer = 1
	WindowsPlayer = 2
	OSXWebPlayer = 3
	OSXDashboardPlayer = 4
	WindowsWebPlayer = 5
	WindowsEditor = 7
	IPhonePlayer = 8
	PS3 = 9
	XBOX360 = 10
	Android = 11
	NaCl = 12
	LinuxPlayer = 13
	FlashPlayer = 15
	LinuxEditor = 16
	WebGLPlayer = 17
	MetroPlayerX86 = 18
	WSAPlayerX86 = 18
	MetroPlayerX64 = 19
	WSAPlayerX64 = 19
	MetroPlayerARM = 20
	WSAPlayerARM = 20
	WP8Player = 21
	BB10Player = 22
	BlackBerryPlayer = 22
	TizenPlayer = 23
	PSP2 = 24
	PS4 = 25
	PSM = 26
	XboxOne = 27
	SamsungTVPlayer = 28
	WiiU = 30
	tvOS = 31
	Switch = 32
	Lumin = 33
	Stadia = 34
	CloudRendering = 35

class UIToolkitHelper:
	class UIToolkitHPathType(IntFlag):
		DocGObjName = 2
		DocGObjTag = 4
		VElemName = 8
		VElemClass = 16

class UnixMemMgt:
	class OpenFlags(IntEnum):
		O_RDONLY = 0
		O_WRONLY = 1
		O_RDWR = 2
		O_ACCMODE = 3

	class ProtectionFlags(IntEnum):
		PROT_NONE = 0
		PROT_READ = 1
		PROT_WRITE = 2
		PROT_EXEC = 4

	class MMapFlags(IntEnum):
		MAP_FILE = 0
		MAP_SHARED = 1
		MAP_PRIVATE = 2
		MAP_TYPE = 15
		MAP_FIXED = 16
		MAP_ANONYMOUS_LINUX = 32
		MAP_ANON = 32
		MAP_ANONYMOUS_MACOS = 4096

class Win32MemMgt:
	class AllocationType(IntFlag):
		Commit = 4096
		Reserve = 8192
		Decommit = 16384
		Release = 32768
		Reset = 524288
		TopDown = 1048576
		WriteWatch = 2097152
		Physical = 4194304
		LargePages = 536870912

	class MemoryProtection(IntFlag):
		NoAccess = 1
		ReadOnly = 2
		ReadWrite = 4
		WriteCopy = 8
		Execute = 16
		ExecuteRead = 32
		ExecuteReadWrite = 64
		ExecuteWriteCopy = 128
		GuardModifierflag = 256
		NoCacheModifierflag = 512
		WriteCombineModifierflag = 1024

	class ProcessorArchitecture(IntEnum):
		Arm = -1
		X86 = 0
		Itanium = 6
		X64 = 9
		Unknown = 65535

