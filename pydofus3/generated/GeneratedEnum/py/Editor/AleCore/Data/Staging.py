from enum import IntFlag

# Editor.AleCore.Data.Staging.StagingEffectTypeEnum
class StagingEffectTypeEnum(IntFlag):
    Distortion = 0
    Translation = 1
    Rotation = 2
    Scale = 3
    Dissolve = 4
    ColorAnimation = 5
    Emissive = 6
    ParticlesMain = 7
    ParticlesEmission = 8
    ParticlesPlay = 9
    ParticlesStop = 10
    PlayFmodEvent = 11
    StopLocalizedFmodEvents = 12
    ChangePlaylist = 13
    SetFmodParam = 14
    SequenceEvent = 15
    NoAnimColor = 16
    ShowMapAnimatedElement = 17

# Editor.AleCore.Data.Staging.StagingExclusivityResolveMethodEnum
class StagingExclusivityResolveMethodEnum(IntFlag):
    FastForward = 0
    Stop = 1
    Wait = 2
    Cancel = 3

# Editor.AleCore.Data.Staging.StagingTransitionType
class StagingTransitionType(IntFlag):
    Instant = 0
    Linear = 1

