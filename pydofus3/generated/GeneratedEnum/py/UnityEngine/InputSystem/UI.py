from enum import IntFlag

# UnityEngine.InputSystem.UI.InputSystemUIInputModule
class InputSystemUIInputModule(IntFlag):
    OutsideScreen = 0
    ScreenCenter = 1

# UnityEngine.InputSystem.UI.UIPointerBehavior
class UIPointerBehavior(IntFlag):
    SingleMouseOrPenButMultiTouchAndTrack = 0
    SingleUnifiedPointer = 1
    AllPointersAsIs = 2

# UnityEngine.InputSystem.UI.UIPointerType
class UIPointerType(IntFlag):
    NONE = 0
    MouseOrPen = 1
    Touch = 2
    Tracked = 3

# UnityEngine.InputSystem.UI.VirtualMouseInput
class VirtualMouseInput(IntFlag):
    SoftwareCursor = 0
    HardwareCursorIfAvailable = 1

