from enum import IntFlag

# UnityEngine.InputForUI.CommandEvent
class CommandEvent(IntFlag):
    Validate = 1
    Execute = 2

# UnityEngine.InputForUI.CommandEvent
class CommandEvent(IntFlag):
    Invalid = 0
    Cut = 1
    Copy = 2
    Paste = 3
    SelectAll = 4
    DeselectAll = 5
    InvertSelection = 6
    Duplicate = 7
    Rename = 8
    Delete = 9
    SoftDelete = 10
    Find = 11
    SelectChildren = 12
    SelectPrefabRoot = 13
    UndoRedoPerformed = 14
    OnLostFocus = 15
    NewKeyboardFocus = 16
    ModifierKeysChanged = 17
    EyeDropperUpdate = 18
    EyeDropperClicked = 19
    EyeDropperCancelled = 20
    ColorPickerChanged = 21
    FrameSelected = 22
    FrameSelectedWithLock = 23

# UnityEngine.InputForUI.Event
class Event(IntFlag):
    Invalid = 0
    KeyEvent = 1
    PointerEvent = 2
    TextInputEvent = 3
    IMECompositionEvent = 4
    CommandEvent = 5
    NavigationEvent = 6

# UnityEngine.InputForUI.EventModifiers
class EventModifiers(IntFlag):
    LeftShift = 1
    RightShift = 2
    Shift = 3
    LeftCtrl = 4
    RightCtrl = 8
    Ctrl = 12
    LeftAlt = 16
    RightAlt = 32
    Alt = 48
    LeftMeta = 64
    RightMeta = 128
    Meta = 192
    CapsLock = 256
    Numlock = 512
    FunctionKey = 1024
    Numeric = 2048

# UnityEngine.InputForUI.EventSource
class EventSource(IntFlag):
    Unspecified = 0
    Keyboard = 1
    Gamepad = 2
    Mouse = 3
    Pen = 4
    Touch = 5

# UnityEngine.InputForUI.KeyEvent
class KeyEvent(IntFlag):
    KeyPressed = 1
    KeyRepeated = 2
    KeyReleased = 3
    State = 4

# UnityEngine.InputForUI.NavigationEvent
class NavigationEvent(IntFlag):
    Move = 1
    Submit = 2
    Cancel = 3

# UnityEngine.InputForUI.NavigationEvent
class NavigationEvent(IntFlag):
    NONE = 0
    Left = 1
    Up = 2
    Right = 3
    Down = 4
    Next = 5
    Previous = 6

# UnityEngine.InputForUI.PointerEvent
class PointerEvent(IntFlag):
    PointerMoved = 1
    Scroll = 2
    ButtonPressed = 3
    ButtonReleased = 4
    State = 5
    TouchCanceled = 6

# UnityEngine.InputForUI.PointerEvent
class PointerEvent(IntFlag):
    NONE = 0
    Primary = 1
    FingerInTouch = 1
    PenTipInTouch = 1
    PenEraserInTouch = 2
    PenBarrelButton = 4
    MouseLeft = 1
    MouseRight = 2
    MouseMiddle = 4
    MouseForward = 8
    MouseBack = 16

