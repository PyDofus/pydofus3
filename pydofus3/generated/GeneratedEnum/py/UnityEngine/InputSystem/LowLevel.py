from enum import IntFlag

# UnityEngine.InputSystem.LowLevel.GamepadButton
class GamepadButton(IntFlag):
    DpadUp = 0
    DpadDown = 1
    DpadLeft = 2
    DpadRight = 3
    North = 4
    East = 5
    South = 6
    West = 7
    LeftStick = 8
    RightStick = 9
    LeftShoulder = 10
    RightShoulder = 11
    Start = 12
    Select = 13
    LeftTrigger = 32
    RightTrigger = 33
    X = 7
    Y = 4
    A = 6
    B = 5
    Cross = 6
    Square = 7
    Triangle = 4
    Circle = 5

# UnityEngine.InputSystem.LowLevel.InitiateUserAccountPairingCommand
class InitiateUserAccountPairingCommand(IntFlag):
    SuccessfullyInitiated = 1
    ErrorNotSupported = -1
    ErrorAlreadyInProgress = -2

# UnityEngine.InputSystem.LowLevel.InputEventTrace
class InputEventTrace(IntFlag):
    FixedUpdate = 1

# UnityEngine.InputSystem.LowLevel.InputUpdateType
class InputUpdateType(IntFlag):
    NONE = 0
    Dynamic = 1
    Fixed = 2
    BeforeRender = 4
    Editor = 8
    Manual = 16
    Default = 11

# UnityEngine.InputSystem.LowLevel.JoystickState
class JoystickState(IntFlag):
    HatSwitchUp = 0
    HatSwitchDown = 1
    HatSwitchLeft = 2
    HatSwitchRight = 3
    Trigger = 4

# UnityEngine.InputSystem.LowLevel.MouseButton
class MouseButton(IntFlag):
    Left = 0
    Right = 1
    Middle = 2
    Forward = 3
    Back = 4

# UnityEngine.InputSystem.LowLevel.QueryPairedUserAccountCommand
class QueryPairedUserAccountCommand(IntFlag):
    DevicePairedToUserAccount = 2
    UserAccountSelectionInProgress = 4
    UserAccountSelectionComplete = 8
    UserAccountSelectionCanceled = 16

# UnityEngine.InputSystem.LowLevel.TouchFlags
class TouchFlags(IntFlag):
    IndirectTouch = 1
    PrimaryTouch = 8
    TapPress = 16
    TapRelease = 32
    OrphanedPrimaryTouch = 64
    BeganInSameFrame = 128

