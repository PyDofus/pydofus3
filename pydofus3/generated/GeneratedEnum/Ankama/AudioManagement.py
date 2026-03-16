from enum import IntEnum
from enum import IntFlag

class AudioManager:
	class EventInstanceAttachmentData:
		class TargetType(IntEnum):
			None_ = 0
			Transform = 1
			Rigidbody = 2
			Rigidbody2D = 3
			Provider = 4

class AudioManagerStatus(IntEnum):
	None_ = 0
	Initializing = 1
	Initialized = 2
	Error = 3

class AudioSystemConfigurationChangeFlag(IntFlag):
	None_ = 0
	Output = 1
	Input = 2048

class BankFlags(IntFlag):
	None_ = 0
	Localized = 1

class CodecType(IntEnum):
	FADPCM = 0
	Vorbis = 1
	AT9 = 2
	XMA = 3
	Opus = 4

class EventInfo:
	class Flags(IntFlag):
		None_ = 0
		Localized = 1
		Is3D = 2
		IsDopplerEnabled = 4
		IsOneShot = 8
		IsSnapshot = 16
		IsStream = 32

class GameCoreScarlettPlatformSettings:
	class GDKVersion(IntEnum):
		GDK250400 = 0

class MusicCreationFlags(IntFlag):
	None_ = 0
	HasMarkers = 1
	LowPriority = 2
	StartAutomatically = 4
	PreventUnloadUntilReplaced = 8
	IgnoreUnloadBankDelay = 16
	IgnoreTransitionParameter = 32
	IgnoreRestartParameter = 64
	StopImmediately = 128

class MusicLoadingState(IntEnum):
	None_ = 0
	Loading = 1
	Loaded = 2
	Error = 3

class MusicState(IntFlag):
	None_ = 0
	BankLoading = 1
	BankLoaded = 2
	BankError = 4
	StartRequested = 8
	Started = 16
	Released = 32
	Replaced = 64
	Stopping = 128

class Playstation5PlatformSettings:
	class SDKVersion(IntEnum):
		SDK11 = 0

class SampleRate(IntEnum):
	PlatformDefault = 0
	_22050Hz = 22050
	_24000Hz = 24000
	_32000Hz = 32000
	_44100Hz = 44100
	_48000Hz = 48000

class SettingsState(IntEnum):
	Disabled = 0
	Enabled = 1
	DevelopmentBuildOnly = 2

class SpeakerMode(IntEnum):
	Stereo = 3
	Surround51 = 6
	Surround71 = 7
	Surround714 = 8

class SwitchPlatformSettings:
	class SDKVersion(IntEnum):
		SDK20 = 0

class ThreadAffinity(IntFlag):
	Any = 0
	Core0 = 1
	Core1 = 2
	Core2 = 4
	Core3 = 8
	Core4 = 16
	Core5 = 32
	Core6 = 64
	Core7 = 128
	Core8 = 256
	Core9 = 512
	Core10 = 1024
	Core11 = 2048
	Core12 = 4096
	Core13 = 8192
	Core14 = 16384
	Core15 = 32768

class ThreadType(IntEnum):
	Mixer = 0
	Feeder = 1
	Stream = 2
	File = 3
	NonBlocking = 4
	Record = 5
	Geometry = 6
	Profiler = 7
	StudioUpdate = 8
	StudioLoadBank = 9
	StudioLoadSample = 10
	Convolution1 = 11
	Convolution2 = 12

class WebGLPlatformSettings:
	class LibraryVersion(IntEnum):
		V_3_1_8 = 0
		V_3_1_39 = 1

