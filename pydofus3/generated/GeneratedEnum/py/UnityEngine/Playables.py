from enum import IntFlag

# UnityEngine.Playables.DirectorWrapMode
class DirectorWrapMode(IntFlag):
    Hold = 0
    Loop = 1
    NONE = 2

# UnityEngine.Playables.FrameData
class FrameData(IntFlag):
    Evaluate = 1
    SeekOccured = 2
    Loop = 4
    Hold = 8
    EffectivePlayStateDelayed = 16
    EffectivePlayStatePlaying = 32

# UnityEngine.Playables.FrameData
class FrameData(IntFlag):
    Evaluate = 0
    Playback = 1

# UnityEngine.Playables.PlayState
class PlayState(IntFlag):
    Paused = 0
    Playing = 1
    Delayed = 2

# UnityEngine.Playables.PlayableSystems
class PlayableSystems(IntFlag):
    FixedUpdate = 0
    FixedUpdatePostPhysics = 1
    Update = 2
    AnimationBegin = 3
    AnimationEnd = 4
    LateUpdate = 5
    Render = 6

# UnityEngine.Playables.PlayableTraversalMode
class PlayableTraversalMode(IntFlag):
    Mix = 0
    Passthrough = 1

