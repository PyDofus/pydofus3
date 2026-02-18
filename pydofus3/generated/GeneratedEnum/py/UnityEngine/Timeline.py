from enum import IntFlag

# UnityEngine.Timeline.ActivationControlPlayable
class ActivationControlPlayable(IntFlag):
    Active = 0
    Inactive = 1
    Revert = 2

# UnityEngine.Timeline.ActivationControlPlayable
class ActivationControlPlayable(IntFlag):
    Unset = 0
    Active = 1
    Inactive = 2

# UnityEngine.Timeline.ActivationTrack
class ActivationTrack(IntFlag):
    Active = 0
    Inactive = 1
    Revert = 2
    LeaveAsIs = 3

# UnityEngine.Timeline.AnimationPlayableAsset
class AnimationPlayableAsset(IntFlag):
    UseSourceAsset = 0
    On = 1
    Off = 2

# UnityEngine.Timeline.AnimationPlayableAsset
class AnimationPlayableAsset(IntFlag):
    Initial = 0
    RotationAsEuler = 1

# UnityEngine.Timeline.AppliedOffsetMode
class AppliedOffsetMode(IntFlag):
    NoRootTransform = 0
    TransformOffset = 1
    SceneOffset = 2
    TransformOffsetLegacy = 3
    SceneOffsetLegacy = 4
    SceneOffsetEditor = 5
    SceneOffsetLegacyEditor = 6

# UnityEngine.Timeline.ClipCaps
class ClipCaps(IntFlag):
    NONE = 0
    Looping = 1
    Extrapolation = 2
    ClipIn = 4
    SpeedMultiplier = 8
    Blending = 16
    AutoScale = 40
    All = -1

# UnityEngine.Timeline.DirectorControlPlayable
class DirectorControlPlayable(IntFlag):
    StopDirector = 0
    PauseDirector = 1

# UnityEngine.Timeline.MatchTargetFields
class MatchTargetFields(IntFlag):
    PositionX = 1
    PositionY = 2
    PositionZ = 4
    RotationX = 8
    RotationY = 16
    RotationZ = 32

# UnityEngine.Timeline.NotificationFlags
class NotificationFlags(IntFlag):
    TriggerInEditMode = 1
    Retroactive = 2
    TriggerOnce = 4

# UnityEngine.Timeline.StandardFrameRates
class StandardFrameRates(IntFlag):
    Fps24 = 0
    Fps23_97 = 1
    Fps25 = 2
    Fps30 = 3
    Fps29_97 = 4
    Fps50 = 5
    Fps60 = 6
    Fps59_94 = 7

# UnityEngine.Timeline.TimeFieldAttribute
class TimeFieldAttribute(IntFlag):
    NONE = 0
    ApplyEditMode = 1

# UnityEngine.Timeline.TimelineAsset
class TimelineAsset(IntFlag):
    Initial = 0

# UnityEngine.Timeline.TimelineAsset
class TimelineAsset(IntFlag):
    Animation = 0
    Audio = 1
    Texture = 2
    Video = 2
    Script = 3
    Hybrid = 4
    Group = 5

# UnityEngine.Timeline.TimelineAsset
class TimelineAsset(IntFlag):
    BasedOnClips = 0
    FixedLength = 1

# UnityEngine.Timeline.TimelineClip
class TimelineClip(IntFlag):
    Initial = 0
    ClipInFromGlobalToLocal = 1

# UnityEngine.Timeline.TimelineClip
class TimelineClip(IntFlag):
    NONE = 0
    Hold = 1
    Loop = 2
    PingPong = 3
    Continue = 4

# UnityEngine.Timeline.TimelineClip
class TimelineClip(IntFlag):
    Auto = 0
    Manual = 1

# UnityEngine.Timeline.TrackAsset
class TrackAsset(IntFlag):
    Initial = 0
    RotationAsEuler = 1
    RootMotionUpgrade = 2
    AnimatedTrackProperties = 3

# UnityEngine.Timeline.TrackBindingFlags
class TrackBindingFlags(IntFlag):
    NONE = 0
    AllowCreateComponent = 1
    All = 1

# UnityEngine.Timeline.TrackOffset
class TrackOffset(IntFlag):
    ApplyTransformOffsets = 0
    ApplySceneOffsets = 1
    Auto = 2

