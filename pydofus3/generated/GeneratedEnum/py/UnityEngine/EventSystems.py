from enum import IntFlag

# UnityEngine.EventSystems.EventHandle
class EventHandle(IntFlag):
    Unused = 0
    Used = 1

# UnityEngine.EventSystems.EventTriggerType
class EventTriggerType(IntFlag):
    PointerEnter = 0
    PointerExit = 1
    PointerDown = 2
    PointerUp = 3
    PointerClick = 4
    Drag = 5
    Drop = 6
    Scroll = 7
    UpdateSelected = 8
    Select = 9
    Deselect = 10
    Move = 11
    InitializePotentialDrag = 12
    BeginDrag = 13
    EndDrag = 14
    Submit = 15
    Cancel = 16

# UnityEngine.EventSystems.MoveDirection
class MoveDirection(IntFlag):
    Left = 0
    Up = 1
    Right = 2
    Down = 3
    NONE = 4

# UnityEngine.EventSystems.NavigationDeviceType
class NavigationDeviceType(IntFlag):
    Unknown = 0
    Keyboard = 1
    NonKeyboard = 2

# UnityEngine.EventSystems.PointerEventData
class PointerEventData(IntFlag):
    Left = 0
    Right = 1
    Middle = 2

# UnityEngine.EventSystems.PointerEventData
class PointerEventData(IntFlag):
    Pressed = 0
    Released = 1
    PressedAndReleased = 2
    NotChanged = 3

# UnityEngine.EventSystems.StandaloneInputModule
class StandaloneInputModule(IntFlag):
    Mouse = 0
    Buttons = 1

