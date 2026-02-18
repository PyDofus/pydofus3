from enum import IntFlag

# DG.Tweening.Core.Enums.FilterType
class FilterType(IntFlag):
    All = 0
    TargetOrId = 1
    TargetAndId = 2
    AllExceptTargetsOrIds = 3
    DOGetter = 4

# DG.Tweening.Core.Enums.NestedTweenFailureBehaviour
class NestedTweenFailureBehaviour(IntFlag):
    TryToPreserveSequence = 0
    KillWholeSequence = 1

# DG.Tweening.Core.Enums.OperationType
class OperationType(IntFlag):
    Complete = 0
    Despawn = 1
    Flip = 2
    Goto = 3
    Pause = 4
    Play = 5
    PlayForward = 6
    PlayBackwards = 7
    Rewind = 8
    SmoothRewind = 9
    Restart = 10
    TogglePause = 11
    IsTweening = 12

# DG.Tweening.Core.Enums.RewindCallbackMode
class RewindCallbackMode(IntFlag):
    FireIfPositionChanged = 0
    FireAlwaysWithRewind = 1
    FireAlways = 2

# DG.Tweening.Core.Enums.SpecialStartupMode
class SpecialStartupMode(IntFlag):
    NONE = 0
    SetLookAt = 1
    SetShake = 2
    SetPunch = 3
    SetCameraShakePosition = 4

# DG.Tweening.Core.Enums.UpdateMode
class UpdateMode(IntFlag):
    Update = 0
    Goto = 1
    IgnoreOnUpdate = 2
    IgnoreOnComplete = 3

# DG.Tweening.Core.Enums.UpdateNotice
class UpdateNotice(IntFlag):
    NONE = 0
    RewindStep = 1

