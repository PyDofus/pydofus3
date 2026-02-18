from enum import IntFlag

# Ankama.AudioManagement.AudioManager
class AudioManager(IntFlag):
    NONE = 0
    Transform = 1
    Rigidbody = 2
    Rigidbody2D = 3
    Provider = 4

# Ankama.AudioManagement.AudioManagerStatus
class AudioManagerStatus(IntFlag):
    NONE = 0
    Initializing = 1
    Initialized = 2
    Error = 3

# Ankama.AudioManagement.AudioSystemConfigurationChangeFlag
class AudioSystemConfigurationChangeFlag(IntFlag):
    NONE = 0
    Output = 1
    Input = 2048

# Ankama.AudioManagement.BankFlags
class BankFlags(IntFlag):
    NONE = 0
    Localized = 1

# Ankama.AudioManagement.CodecType
class CodecType(IntFlag):
    FADPCM = 0
    Vorbis = 1
    AT9 = 2
    XMA = 3
    Opus = 4

# Ankama.AudioManagement.EventInfo
class EventInfo(IntFlag):
    NONE = 0
    Localized = 1
    Is3D = 2
    IsDopplerEnabled = 4
    IsOneShot = 8
    IsSnapshot = 16
    IsStream = 32

# Ankama.AudioManagement.GameCoreScarlettPlatformSettings
class GameCoreScarlettPlatformSettings(IntFlag):
    GDK241000 = 0

# Ankama.AudioManagement.MusicCreationFlags
class MusicCreationFlags(IntFlag):
    NONE = 0
    HasMarkers = 1
    LowPriority = 2
    StartAutomatically = 4
    PreventUnloadUntilReplaced = 8
    IgnoreUnloadBankDelay = 16
    IgnoreTransitionParameter = 32
    IgnoreRestartParameter = 64
    StopImmediately = 128

# Ankama.AudioManagement.MusicLoadingState
class MusicLoadingState(IntFlag):
    NONE = 0
    Loading = 1
    Loaded = 2
    Error = 3

# Ankama.AudioManagement.MusicState
class MusicState(IntFlag):
    NONE = 0
    BankLoading = 1
    BankLoaded = 2
    BankError = 4
    StartRequested = 8
    Started = 16
    Released = 32
    Replaced = 64
    Stopping = 128

# Ankama.AudioManagement.Playstation5PlatformSettings
class Playstation5PlatformSettings(IntFlag):
    SDK9 = 0
    SDK10 = 1
    SDK11 = 2

# Ankama.AudioManagement.SampleRate
class SampleRate(IntFlag):
    PlatformDefault = 0
    _22050Hz = 22050
    _24000Hz = 24000
    _32000Hz = 32000
    _44100Hz = 44100
    _48000Hz = 48000

# Ankama.AudioManagement.SettingsState
class SettingsState(IntFlag):
    Disabled = 0
    Enabled = 1
    DevelopmentBuildOnly = 2

# Ankama.AudioManagement.SpeakerMode
class SpeakerMode(IntFlag):
    Stereo = 3
    Surround51 = 6
    Surround71 = 7
    Surround714 = 8

# Ankama.AudioManagement.SwitchPlatformSettings
class SwitchPlatformSettings(IntFlag):
    SDK17 = 0
    SDK20 = 1

# Ankama.AudioManagement.ThreadAffinity
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

# Ankama.AudioManagement.ThreadType
class ThreadType(IntFlag):
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

# Ankama.AudioManagement.WebGLPlatformSettings
class WebGLPlatformSettings(IntFlag):
    V_3_1_8 = 0
    V_3_1_39 = 1

