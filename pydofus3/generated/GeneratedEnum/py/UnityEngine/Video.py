from enum import IntFlag

# UnityEngine.Video.Video3DLayout
class Video3DLayout(IntFlag):
    No3D = 0
    SideBySide3D = 1
    OverUnder3D = 2

# UnityEngine.Video.VideoAspectRatio
class VideoAspectRatio(IntFlag):
    NoScaling = 0
    FitVertically = 1
    FitHorizontally = 2
    FitInside = 3
    FitOutside = 4
    Stretch = 5

# UnityEngine.Video.VideoAudioOutputMode
class VideoAudioOutputMode(IntFlag):
    NONE = 0
    AudioSource = 1
    Direct = 2
    APIOnly = 3

# UnityEngine.Video.VideoRenderMode
class VideoRenderMode(IntFlag):
    CameraFarPlane = 0
    CameraNearPlane = 1
    RenderTexture = 2
    MaterialOverride = 3
    APIOnly = 4

# UnityEngine.Video.VideoSource
class VideoSource(IntFlag):
    VideoClip = 0
    Url = 1

# UnityEngine.Video.VideoTimeReference
class VideoTimeReference(IntFlag):
    Freerun = 0
    InternalTime = 1
    ExternalTime = 2

# UnityEngine.Video.VideoTimeSource
class VideoTimeSource(IntFlag):
    AudioDSPTimeSource = 0
    GameTimeSource = 1

# UnityEngine.Video.VideoTimeUpdateMode
class VideoTimeUpdateMode(IntFlag):
    DSPTime = 0
    GameTime = 1
    UnscaledGameTime = 2

