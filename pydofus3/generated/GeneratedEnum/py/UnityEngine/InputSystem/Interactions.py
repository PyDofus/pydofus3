from enum import IntFlag

# UnityEngine.InputSystem.Interactions.MultiTapInteraction
class MultiTapInteraction(IntFlag):
    NONE = 0
    WaitingForNextRelease = 1
    WaitingForNextPress = 2

# UnityEngine.InputSystem.Interactions.PressBehavior
class PressBehavior(IntFlag):
    PressOnly = 0
    ReleaseOnly = 1
    PressAndRelease = 2

