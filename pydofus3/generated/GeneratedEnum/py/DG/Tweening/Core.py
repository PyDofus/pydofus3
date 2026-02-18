from enum import IntFlag

# DG.Tweening.Core.DOTweenSettings
class DOTweenSettings(IntFlag):
    AssetsDirectory = 0
    DOTweenDirectory = 1
    DemigiantDirectory = 2

# DG.Tweening.Core.SafeModeReport
class SafeModeReport(IntFlag):
    Unset = 0
    TargetOrFieldMissing = 1
    Callback = 2
    StartupFailure = 3

# DG.Tweening.Core.TweenManager
class TweenManager(IntFlag):
    TweenersAndSequences = 0
    TweenersOnly = 1
    SequencesOnly = 2

