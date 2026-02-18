from enum import IntFlag

# UnityEngine.InputSystem.HID
class HID(IntFlag):
    Unknown = 0
    Input = 1
    Output = 2
    Feature = 3

# UnityEngine.InputSystem.HID
class HID(IntFlag):
    Physical = 0
    Application = 1
    Logical = 2
    Report = 3
    NamedArray = 4
    UsageSwitch = 5
    UsageModifier = 6

# UnityEngine.InputSystem.HID
class HID(IntFlag):
    Constant = 1
    Variable = 2
    Relative = 4
    Wrap = 8
    NonLinear = 16
    NoPreferred = 32
    NullState = 64
    Volatile = 128
    BufferedBytes = 256

# UnityEngine.InputSystem.HID
class HID(IntFlag):
    Undefined = 0
    GenericDesktop = 1
    Simulation = 2
    VRControls = 3
    SportControls = 4
    GameControls = 5
    GenericDeviceControls = 6
    Keyboard = 7
    LEDs = 8
    Button = 9
    Ordinal = 10
    Telephony = 11
    Consumer = 12
    Digitizer = 13
    PID = 15
    Unicode = 16
    AlphanumericDisplay = 20
    MedicalInstruments = 64
    Monitor = 128
    Power = 132
    BarCodeScanner = 140
    MagneticStripeReader = 142
    Camera = 144
    Arcade = 145
    VendorDefined = 65280

# UnityEngine.InputSystem.HID
class HID(IntFlag):
    Undefined = 0
    Pointer = 1
    Mouse = 2
    Joystick = 4
    Gamepad = 5
    Keyboard = 6
    Keypad = 7
    MultiAxisController = 8
    TabletPCControls = 9
    AssistiveControl = 10
    X = 48
    Y = 49
    Z = 50
    Rx = 51
    Ry = 52
    Rz = 53
    Slider = 54
    Dial = 55
    Wheel = 56
    HatSwitch = 57
    CountedBuffer = 58
    ByteCount = 59
    MotionWakeup = 60
    Start = 61
    Select = 62
    Vx = 64
    Vy = 65
    Vz = 66
    Vbrx = 67
    Vbry = 68
    Vbrz = 69
    Vno = 70
    FeatureNotification = 71
    ResolutionMultiplier = 72
    SystemControl = 128
    SystemPowerDown = 129
    SystemSleep = 130
    SystemWakeUp = 131
    SystemContextMenu = 132
    SystemMainMenu = 133
    SystemAppMenu = 134
    SystemMenuHelp = 135
    SystemMenuExit = 136
    SystemMenuSelect = 137
    SystemMenuRight = 138
    SystemMenuLeft = 139
    SystemMenuUp = 140
    SystemMenuDown = 141
    SystemColdRestart = 142
    SystemWarmRestart = 143
    DpadUp = 144
    DpadDown = 145
    DpadRight = 146
    DpadLeft = 147
    SystemDock = 160
    SystemUndock = 161
    SystemSetup = 162
    SystemBreak = 163
    SystemDebuggerBreak = 164
    ApplicationBreak = 165
    ApplicationDebuggerBreak = 166
    SystemSpeakerMute = 167
    SystemHibernate = 168
    SystemDisplayInvert = 176
    SystemDisplayInternal = 177
    SystemDisplayExternal = 178
    SystemDisplayBoth = 179
    SystemDisplayDual = 180
    SystemDisplayToggleIntExt = 181
    SystemDisplaySwapPrimarySecondary = 182
    SystemDisplayLCDAutoScale = 183

# UnityEngine.InputSystem.HID
class HID(IntFlag):
    Undefined = 0
    FlightSimulationDevice = 1
    AutomobileSimulationDevice = 2
    TankSimulationDevice = 3
    SpaceshipSimulationDevice = 4
    SubmarineSimulationDevice = 5
    SailingSimulationDevice = 6
    MotorcycleSimulationDevice = 7
    SportsSimulationDevice = 8
    AirplaneSimulationDevice = 9
    HelicopterSimulationDevice = 10
    MagicCarpetSimulationDevice = 11
    BicylcleSimulationDevice = 12
    FlightControlStick = 32
    FlightStick = 33
    CyclicControl = 34
    CyclicTrim = 35
    FlightYoke = 36
    TrackControl = 37
    Aileron = 176
    AileronTrim = 177
    AntiTorqueControl = 178
    AutopilotEnable = 179
    ChaffRelease = 180
    CollectiveControl = 181
    DiveBreak = 182
    ElectronicCountermeasures = 183
    Elevator = 184
    ElevatorTrim = 185
    Rudder = 186
    Throttle = 187
    FlightCommunications = 188
    FlareRelease = 189
    LandingGear = 190
    ToeBreak = 191
    Trigger = 192
    WeaponsArm = 193
    WeaponsSelect = 194
    WingFlaps = 195
    Accelerator = 196
    Brake = 197
    Clutch = 198
    Shifter = 199
    Steering = 200
    TurretDirection = 201
    BarrelElevation = 202
    DivePlane = 203
    Ballast = 204
    BicycleCrank = 205
    HandleBars = 206
    FrontBrake = 207
    RearBrake = 208

# UnityEngine.InputSystem.HID
class HID(IntFlag):
    Undefined = 0
    Primary = 1
    Secondary = 2
    Tertiary = 3

# UnityEngine.InputSystem.InputAction
class InputAction(IntFlag):
    WantsInitialStateCheck = 1

# UnityEngine.InputSystem.InputActionChange
class InputActionChange(IntFlag):
    ActionEnabled = 0
    ActionDisabled = 1
    ActionMapEnabled = 2
    ActionMapDisabled = 3
    ActionStarted = 4
    ActionPerformed = 5
    ActionCanceled = 6
    BoundControlsAboutToChange = 7
    BoundControlsChanged = 8

# UnityEngine.InputSystem.InputActionMap
class InputActionMap(IntFlag):
    NeedToResolveBindings = 1
    BindingResolutionNeedsFullReResolve = 2
    ControlsForEachActionInitialized = 4
    BindingsForEachActionInitialized = 8

# UnityEngine.InputSystem.InputActionPhase
class InputActionPhase(IntFlag):
    Disabled = 0
    Waiting = 1
    Started = 2
    Performed = 3
    Canceled = 4

# UnityEngine.InputSystem.InputActionRebindingExtensions
class InputActionRebindingExtensions(IntFlag):
    Started = 1
    Completed = 2
    Canceled = 4
    OnEventHooked = 8
    OnAfterUpdateHooked = 16
    DontIgnoreNoisyControls = 64
    DontGeneralizePathOfSelectedControl = 128
    AddNewBinding = 256
    SuppressMatchingEvents = 512

# UnityEngine.InputSystem.InputActionState
class InputActionState(IntFlag):
    TimerRunning = 1

# UnityEngine.InputSystem.InputActionState
class InputActionState(IntFlag):
    ChainsWithNext = 1
    EndOfChain = 2
    Composite = 4
    PartOfComposite = 8
    InitialStateCheckPending = 16
    WantsInitialStateCheck = 32

# UnityEngine.InputSystem.InputActionState
class InputActionState(IntFlag):
    HaveMagnitude = 1
    PassThrough = 2
    MayNeedConflictResolution = 4
    HasMultipleConcurrentActuations = 8
    InProcessing = 16
    Button = 32
    Pressed = 64

# UnityEngine.InputSystem.InputActionType
class InputActionType(IntFlag):
    Value = 0
    Button = 1
    PassThrough = 2

# UnityEngine.InputSystem.InputBinding
class InputBinding(IntFlag):
    DontUseShortDisplayNames = 1
    DontOmitDevice = 2
    DontIncludeInteractions = 4
    IgnoreBindingOverrides = 8

# UnityEngine.InputSystem.InputBinding
class InputBinding(IntFlag):
    EmptyGroupMatchesAny = 1

# UnityEngine.InputSystem.InputBinding
class InputBinding(IntFlag):
    NONE = 0
    Composite = 4
    PartOfComposite = 8

# UnityEngine.InputSystem.InputControl
class InputControl(IntFlag):
    ConfigUpToDate = 1
    IsNoisy = 2
    IsSynthetic = 4
    IsButton = 8
    DontReset = 16
    SetupFinished = 32
    UsesStateFromOtherControl = 64

# UnityEngine.InputSystem.InputControlExtensions
class InputControlExtensions(IntFlag):
    IgnoreControlsInDefaultState = 1
    IgnoreControlsInCurrentState = 2
    IncludeSyntheticControls = 4
    IncludeNoisyControls = 8
    IncludeNonLeafControls = 16

# UnityEngine.InputSystem.InputControlLayoutChange
class InputControlLayoutChange(IntFlag):
    Added = 0
    Removed = 1
    Replaced = 2

# UnityEngine.InputSystem.InputControlPath
class InputControlPath(IntFlag):
    NONE = 0
    OmitDevice = 2
    UseShortNames = 4

# UnityEngine.InputSystem.InputControlPath
class InputControlPath(IntFlag):
    Name = 0
    DisplayName = 1
    Usage = 2
    Layout = 3

# UnityEngine.InputSystem.InputControlScheme
class InputControlScheme(IntFlag):
    AllSatisfied = 0
    MissingRequired = 1
    MissingOptional = 2

# UnityEngine.InputSystem.InputControlScheme
class InputControlScheme(IntFlag):
    NONE = 0
    Optional = 1
    Or = 2

# UnityEngine.InputSystem.InputDevice
class InputDevice(IntFlag):
    UpdateBeforeRender = 1
    HasStateCallbacks = 2
    HasControlsWithDefaultState = 4
    HasDontResetControls = 1024
    HasEventMerger = 8192
    HasEventPreProcessor = 16384
    Remote = 8
    Native = 16
    DisabledInFrontend = 32
    DisabledInRuntime = 128
    DisabledWhileInBackground = 256
    DisabledStateHasBeenQueriedFromRuntime = 64
    CanRunInBackground = 2048
    CanRunInBackgroundHasBeenQueried = 4096

# UnityEngine.InputSystem.InputDeviceChange
class InputDeviceChange(IntFlag):
    Added = 0
    Removed = 1
    Disconnected = 2
    Reconnected = 3
    Enabled = 4
    Disabled = 5
    UsageChanged = 6
    ConfigurationChanged = 7
    SoftReset = 8
    HardReset = 9
    Destroyed = 10

# UnityEngine.InputSystem.InputInteractionContext
class InputInteractionContext(IntFlag):
    TimerHasExpired = 2

# UnityEngine.InputSystem.InputManager
class InputManager(IntFlag):
    Everywhere = 0
    InFrontendOnly = 1
    TemporaryWhilePlayerIsInBackground = 2

# UnityEngine.InputSystem.InputProcessor
class InputProcessor(IntFlag):
    CacheResult = 0
    EvaluateOnEveryRead = 1

# UnityEngine.InputSystem.InputRemoting
class InputRemoting(IntFlag):
    Connect = 0
    Disconnect = 1
    NewLayout = 2
    NewDevice = 3
    NewEvents = 4
    RemoveDevice = 5
    RemoveLayout = 6
    ChangeUsages = 7
    StartSending = 8
    StopSending = 9

# UnityEngine.InputSystem.InputRemoting
class InputRemoting(IntFlag):
    Sending = 1
    StartSendingOnConnect = 2

# UnityEngine.InputSystem.InputSettings
class InputSettings(IntFlag):
    ProcessEventsInDynamicUpdate = 1
    ProcessEventsInFixedUpdate = 2
    ProcessEventsManually = 3

# UnityEngine.InputSystem.InputSettings
class InputSettings(IntFlag):
    UniformAcrossAllPlatforms = 0
    KeepPlatformSpecificInputRange = 1

# UnityEngine.InputSystem.InputSettings
class InputSettings(IntFlag):
    ResetAndDisableNonBackgroundDevices = 0
    ResetAndDisableAllDevices = 1
    IgnoreFocus = 2

# UnityEngine.InputSystem.InputSettings
class InputSettings(IntFlag):
    PointersAndKeyboardsRespectGameViewFocus = 0
    AllDevicesRespectGameViewFocus = 1
    AllDeviceInputAlwaysGoesToGameView = 2

# UnityEngine.InputSystem.InputSettings
class InputSettings(IntFlag):
    Compact = 0
    MultilineEffective = 1
    MultilineBoth = 2

# UnityEngine.InputSystem.Key
class Key(IntFlag):
    NONE = 0
    Space = 1
    Enter = 2
    Tab = 3
    Backquote = 4
    Quote = 5
    Semicolon = 6
    Comma = 7
    Period = 8
    Slash = 9
    Backslash = 10
    LeftBracket = 11
    RightBracket = 12
    Minus = 13
    Equals = 14
    A = 15
    B = 16
    C = 17
    D = 18
    E = 19
    F = 20
    G = 21
    H = 22
    I = 23
    J = 24
    K = 25
    L = 26
    M = 27
    N = 28
    O = 29
    P = 30
    Q = 31
    R = 32
    S = 33
    T = 34
    U = 35
    V = 36
    W = 37
    X = 38
    Y = 39
    Z = 40
    Digit1 = 41
    Digit2 = 42
    Digit3 = 43
    Digit4 = 44
    Digit5 = 45
    Digit6 = 46
    Digit7 = 47
    Digit8 = 48
    Digit9 = 49
    Digit0 = 50
    LeftShift = 51
    RightShift = 52
    LeftAlt = 53
    RightAlt = 54
    AltGr = 54
    LeftCtrl = 55
    RightCtrl = 56
    LeftMeta = 57
    RightMeta = 58
    LeftWindows = 57
    RightWindows = 58
    LeftApple = 57
    RightApple = 58
    LeftCommand = 57
    RightCommand = 58
    ContextMenu = 59
    Escape = 60
    LeftArrow = 61
    RightArrow = 62
    UpArrow = 63
    DownArrow = 64
    Backspace = 65
    PageDown = 66
    PageUp = 67
    Home = 68
    End = 69
    Insert = 70
    Delete = 71
    CapsLock = 72
    NumLock = 73
    PrintScreen = 74
    ScrollLock = 75
    Pause = 76
    NumpadEnter = 77
    NumpadDivide = 78
    NumpadMultiply = 79
    NumpadPlus = 80
    NumpadMinus = 81
    NumpadPeriod = 82
    NumpadEquals = 83
    Numpad0 = 84
    Numpad1 = 85
    Numpad2 = 86
    Numpad3 = 87
    Numpad4 = 88
    Numpad5 = 89
    Numpad6 = 90
    Numpad7 = 91
    Numpad8 = 92
    Numpad9 = 93
    F1 = 94
    F2 = 95
    F3 = 96
    F4 = 97
    F5 = 98
    F6 = 99
    F7 = 100
    F8 = 101
    F9 = 102
    F10 = 103
    F11 = 104
    F12 = 105
    OEM1 = 106
    OEM2 = 107
    OEM3 = 108
    OEM4 = 109
    OEM5 = 110
    IMESelected = 111
    F13 = 112
    F14 = 113
    F15 = 114
    F16 = 115
    F17 = 116
    F18 = 117
    F19 = 118
    F20 = 119
    F21 = 120
    F22 = 121
    F23 = 122
    F24 = 123

# UnityEngine.InputSystem.PenButton
class PenButton(IntFlag):
    Tip = 0
    Eraser = 1
    BarrelFirst = 2
    BarrelSecond = 3
    InRange = 4
    BarrelThird = 5
    BarrelFourth = 6
    Barrel1 = 2
    Barrel2 = 3
    Barrel3 = 5
    Barrel4 = 6

# UnityEngine.InputSystem.PlayerJoinBehavior
class PlayerJoinBehavior(IntFlag):
    JoinPlayersWhenButtonIsPressed = 0
    JoinPlayersWhenJoinActionIsTriggered = 1
    JoinPlayersManually = 2

# UnityEngine.InputSystem.PlayerNotifications
class PlayerNotifications(IntFlag):
    SendMessages = 0
    BroadcastMessages = 1
    InvokeUnityEvents = 2
    InvokeCSharpEvents = 3

# UnityEngine.InputSystem.TouchPhase
class TouchPhase(IntFlag):
    NONE = 0
    Began = 1
    Moved = 2
    Ended = 3
    Canceled = 4
    Stationary = 5

