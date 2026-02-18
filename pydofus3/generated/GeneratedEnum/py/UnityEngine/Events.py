from enum import IntFlag

# UnityEngine.Events.PersistentListenerMode
class PersistentListenerMode(IntFlag):
    EventDefined = 0
    Void = 1
    Object = 2
    Int = 3
    Float = 4
    String = 5
    Bool = 6

# UnityEngine.Events.UnityEventCallState
class UnityEventCallState(IntFlag):
    Off = 0
    EditorAndRuntime = 1
    RuntimeOnly = 2

