from enum import IntFlag

# UnityEngine.AdditionalCanvasShaderChannels
class AdditionalCanvasShaderChannels(IntFlag):
    NONE = 0
    TexCoord1 = 1
    TexCoord2 = 2
    TexCoord3 = 4
    Normal = 8
    Tangent = 16

# UnityEngine.AnimationEventSource
class AnimationEventSource(IntFlag):
    NoSource = 0
    Legacy = 1
    Animator = 2

# UnityEngine.AnimatorControllerParameterType
class AnimatorControllerParameterType(IntFlag):
    Float = 1
    Int = 3
    Bool = 4
    Trigger = 9

# UnityEngine.AnimatorCullingMode
class AnimatorCullingMode(IntFlag):
    AlwaysAnimate = 0
    CullUpdateTransforms = 1
    CullCompletely = 2

# UnityEngine.AnimatorRecorderMode
class AnimatorRecorderMode(IntFlag):
    Offline = 0
    Playback = 1
    Record = 2

# UnityEngine.AnimatorUpdateMode
class AnimatorUpdateMode(IntFlag):
    Normal = 0
    Fixed = 1
    UnscaledTime = 2

# UnityEngine.ApplicationInstallMode
class ApplicationInstallMode(IntFlag):
    Unknown = 0
    Store = 1
    DeveloperBuild = 2
    Adhoc = 3
    Enterprise = 4
    Editor = 5

# UnityEngine.ApplicationMemoryUsage
class ApplicationMemoryUsage(IntFlag):
    Unknown = 0
    Low = 1
    Medium = 2
    High = 3
    Critical = 4

# UnityEngine.AvatarIKGoal
class AvatarIKGoal(IntFlag):
    LeftFoot = 0
    RightFoot = 1
    LeftHand = 2
    RightHand = 3

# UnityEngine.AvatarIKHint
class AvatarIKHint(IntFlag):
    LeftKnee = 0
    RightKnee = 1
    LeftElbow = 2
    RightElbow = 3

# UnityEngine.AvatarMaskBodyPart
class AvatarMaskBodyPart(IntFlag):
    Root = 0
    Body = 1
    Head = 2
    LeftLeg = 3
    RightLeg = 4
    LeftArm = 5
    RightArm = 6
    LeftFingers = 7
    RightFingers = 8
    LeftFootIK = 9
    RightFootIK = 10
    LeftHandIK = 11
    RightHandIK = 12
    LastBodyPart = 13

# UnityEngine.AvatarTarget
class AvatarTarget(IntFlag):
    Root = 0
    Body = 1
    LeftFoot = 2
    RightFoot = 3
    LeftHand = 4
    RightHand = 5

# UnityEngine.Awaitable
class Awaitable(IntFlag):
    NONE = 0
    MainThread = 1
    BackgroundThread = 2

# UnityEngine.BatteryStatus
class BatteryStatus(IntFlag):
    Unknown = 0
    Charging = 1
    Discharging = 2
    NotCharging = 3
    Full = 4

# UnityEngine.Camera
class Camera(IntFlag):
    Explicit = 0
    Implicit = 1
    PhysicalPropertiesBased = 2

# UnityEngine.Camera
class Camera(IntFlag):
    Vertical = 1
    Horizontal = 2
    Fill = 3
    Overscan = 4
    NONE = 0

# UnityEngine.Camera
class Camera(IntFlag):
    Left = 0
    Right = 1

# UnityEngine.Camera
class Camera(IntFlag):
    Left = 0
    Right = 1
    Mono = 2

# UnityEngine.Camera
class Camera(IntFlag):
    Off = 0
    ShowFiltered = 1

# UnityEngine.CameraClearFlags
class CameraClearFlags(IntFlag):
    Skybox = 1
    Color = 2
    SolidColor = 2
    Depth = 3
    Nothing = 4

# UnityEngine.CameraType
class CameraType(IntFlag):
    Game = 1
    SceneView = 2
    Preview = 4
    VR = 8
    Reflection = 16

# UnityEngine.CollisionPairEventFlags
class CollisionPairEventFlags(IntFlag):
    SolveContacts = 1
    ModifyContacts = 2
    NotifyTouchFound = 4
    NotifyTouchPersists = 8
    NotifyTouchLost = 16
    NotifyTouchCCD = 32
    NotifyThresholdForceFound = 64
    NotifyThresholdForcePersists = 128
    NotifyThresholdForceLost = 256
    NotifyContactPoint = 512
    DetectDiscreteContact = 1024
    DetectCCDContact = 2048
    PreSolverVelocity = 4096
    PostSolverVelocity = 8192
    ContactEventPose = 16384
    NextFree = 32768
    ContactDefault = 1025
    TriggerDefault = 1044

# UnityEngine.CollisionPairFlags
class CollisionPairFlags(IntFlag):
    RemovedShape = 1
    RemovedOtherShape = 2
    ActorPairHasFirstTouch = 4
    ActorPairLostTouch = 8
    InternalHasImpulses = 16
    InternalContactsAreFlipped = 32

# UnityEngine.CollisionPairHeaderFlags
class CollisionPairHeaderFlags(IntFlag):
    RemovedActor = 1
    RemovedOtherActor = 2

# UnityEngine.ColorGamut
class ColorGamut(IntFlag):
    sRGB = 0
    Rec709 = 1
    Rec2020 = 2
    DisplayP3 = 3
    HDR10 = 4
    DolbyHDR = 5
    P3D65G22 = 6

# UnityEngine.ColorPrimaries
class ColorPrimaries(IntFlag):
    Unknown = -1
    Rec709 = 0
    Rec2020 = 1
    P3 = 2

# UnityEngine.ColorSpace
class ColorSpace(IntFlag):
    Uninitialized = -1
    Gamma = 0
    Linear = 1

# UnityEngine.ComputeBufferMode
class ComputeBufferMode(IntFlag):
    Immutable = 0
    Dynamic = 1
    Circular = 2
    StreamOut = 3
    SubUpdates = 4

# UnityEngine.ComputeBufferType
class ComputeBufferType(IntFlag):
    Default = 0
    Raw = 1
    Append = 2
    Counter = 4
    Constant = 8
    Structured = 16
    DrawIndirect = 256
    IndirectArguments = 256
    GPUMemory = 512

# UnityEngine.CubemapFace
class CubemapFace(IntFlag):
    Unknown = -1
    PositiveX = 0
    NegativeX = 1
    PositiveY = 2
    NegativeY = 3
    PositiveZ = 4
    NegativeZ = 5

# UnityEngine.CullingQueryOptions
class CullingQueryOptions(IntFlag):
    Normal = 0
    IgnoreVisibility = 1
    IgnoreDistance = 2

# UnityEngine.CursorLockMode
class CursorLockMode(IntFlag):
    NONE = 0
    Locked = 1
    Confined = 2

# UnityEngine.CursorMode
class CursorMode(IntFlag):
    Auto = 0
    ForceSoftware = 1

# UnityEngine.DepthTextureMode
class DepthTextureMode(IntFlag):
    NONE = 0
    Depth = 1
    DepthNormals = 2
    MotionVectors = 4

# UnityEngine.DeviceOrientation
class DeviceOrientation(IntFlag):
    Unknown = 0
    Portrait = 1
    PortraitUpsideDown = 2
    LandscapeLeft = 3
    LandscapeRight = 4
    FaceUp = 5
    FaceDown = 6

# UnityEngine.DeviceType
class DeviceType(IntFlag):
    Unknown = 0
    Handheld = 1
    Console = 2
    Desktop = 3

# UnityEngine.DisableBatchingType
class DisableBatchingType(IntFlag):
    FALSE = 0
    TRUE = 1
    WhenLODFading = 2

# UnityEngine.DrivenTransformProperties
class DrivenTransformProperties(IntFlag):
    NONE = 0
    All = -1
    AnchoredPositionX = 2
    AnchoredPositionY = 4
    AnchoredPositionZ = 8
    Rotation = 16
    ScaleX = 32
    ScaleY = 64
    ScaleZ = 128
    AnchorMinX = 256
    AnchorMinY = 512
    AnchorMaxX = 1024
    AnchorMaxY = 2048
    SizeDeltaX = 4096
    SizeDeltaY = 8192
    PivotX = 16384
    PivotY = 32768
    AnchoredPosition = 6
    AnchoredPosition3D = 14
    Scale = 224
    AnchorMin = 768
    AnchorMax = 3072
    Anchors = 3840
    SizeDelta = 12288
    Pivot = 49152

# UnityEngine.EnumDataUtility
class EnumDataUtility(IntFlag):
    ExcludeObsolete = 0
    IncludeObsoleteExceptErrors = 1
    IncludeAllObsolete = 2

# UnityEngine.EventModifiers
class EventModifiers(IntFlag):
    NONE = 0
    Shift = 1
    Control = 2
    Alt = 4
    Command = 8
    Numeric = 16
    CapsLock = 32
    FunctionKey = 64

# UnityEngine.EventType
class EventType(IntFlag):
    MouseDown = 0
    MouseUp = 1
    MouseMove = 2
    MouseDrag = 3
    KeyDown = 4
    KeyUp = 5
    ScrollWheel = 6
    Repaint = 7
    Layout = 8
    DragUpdated = 9
    DragPerform = 10
    DragExited = 15
    Ignore = 11
    Used = 12
    ValidateCommand = 13
    ExecuteCommand = 14
    ContextClick = 16
    MouseEnterWindow = 20
    MouseLeaveWindow = 21
    TouchDown = 30
    TouchUp = 31
    TouchMove = 32
    TouchEnter = 33
    TouchLeave = 34
    TouchStationary = 35
    mouseDown = 0
    mouseUp = 1
    mouseMove = 2
    mouseDrag = 3
    keyDown = 4
    keyUp = 5
    scrollWheel = 6
    repaint = 7
    layout = 8
    dragUpdated = 9
    dragPerform = 10
    ignore = 11
    used = 12

# UnityEngine.ExpressionEvaluator
class ExpressionEvaluator(IntFlag):
    Add = 0
    Sub = 1
    Mul = 2
    Div = 3
    Mod = 4
    Neg = 5
    Pow = 6
    Sqrt = 7
    Sin = 8
    Cos = 9
    Tan = 10
    Floor = 11
    Ceil = 12
    Round = 13
    Rand = 14
    Linear = 15

# UnityEngine.ExpressionEvaluator
class ExpressionEvaluator(IntFlag):
    Left = 0
    Right = 1

# UnityEngine.FilterMode
class FilterMode(IntFlag):
    Point = 0
    Bilinear = 1
    Trilinear = 2

# UnityEngine.FindObjectsInactive
class FindObjectsInactive(IntFlag):
    Exclude = 0
    Include = 1

# UnityEngine.FindObjectsSortMode
class FindObjectsSortMode(IntFlag):
    NONE = 0
    InstanceID = 1

# UnityEngine.FocusType
class FocusType(IntFlag):
    Native = 0
    Keyboard = 1
    Passive = 2

# UnityEngine.FontStyle
class FontStyle(IntFlag):
    Normal = 0
    Bold = 1
    Italic = 2
    BoldAndItalic = 3

# UnityEngine.ForceMode2D
class ForceMode2D(IntFlag):
    Force = 0
    Impulse = 1

# UnityEngine.FullScreenMode
class FullScreenMode(IntFlag):
    ExclusiveFullScreen = 0
    FullScreenWindow = 1
    MaximizedWindow = 2
    Windowed = 3

# UnityEngine.GUILayoutOption
class GUILayoutOption(IntFlag):
    fixedWidth = 0
    fixedHeight = 1
    minWidth = 2
    maxWidth = 3
    minHeight = 4
    maxHeight = 5
    stretchWidth = 6
    stretchHeight = 7
    alignStart = 8
    alignMiddle = 9
    alignEnd = 10
    alignJustify = 11
    equalSize = 12
    spacing = 13

# UnityEngine.GradientMode
class GradientMode(IntFlag):
    Blend = 0
    Fixed = 1
    PerceptualBlend = 2

# UnityEngine.GraphicsBuffer
class GraphicsBuffer(IntFlag):
    Vertex = 1
    Index = 2
    CopySource = 4
    CopyDestination = 8
    Structured = 16
    Raw = 32
    Append = 64
    Counter = 128
    IndirectArguments = 256
    Constant = 512

# UnityEngine.GraphicsBuffer
class GraphicsBuffer(IntFlag):
    NONE = 0
    LockBufferForWrite = 1

# UnityEngine.HDRDisplaySupportFlags
class HDRDisplaySupportFlags(IntFlag):
    NONE = 0
    Supported = 1
    RuntimeSwitchable = 2
    AutomaticTonemapping = 4

# UnityEngine.HideFlags
class HideFlags(IntFlag):
    NONE = 0
    HideInHierarchy = 1
    HideInInspector = 2
    DontSaveInEditor = 4
    NotEditable = 8
    DontSaveInBuild = 16
    DontUnloadUnusedAsset = 32
    DontSave = 52
    HideAndDontSave = 61

# UnityEngine.HorizontalWrapMode
class HorizontalWrapMode(IntFlag):
    Wrap = 0
    Overflow = 1

# UnityEngine.HumanBodyBones
class HumanBodyBones(IntFlag):
    Hips = 0
    LeftUpperLeg = 1
    RightUpperLeg = 2
    LeftLowerLeg = 3
    RightLowerLeg = 4
    LeftFoot = 5
    RightFoot = 6
    Spine = 7
    Chest = 8
    UpperChest = 54
    Neck = 9
    Head = 10
    LeftShoulder = 11
    RightShoulder = 12
    LeftUpperArm = 13
    RightUpperArm = 14
    LeftLowerArm = 15
    RightLowerArm = 16
    LeftHand = 17
    RightHand = 18
    LeftToes = 19
    RightToes = 20
    LeftEye = 21
    RightEye = 22
    Jaw = 23
    LeftThumbProximal = 24
    LeftThumbIntermediate = 25
    LeftThumbDistal = 26
    LeftIndexProximal = 27
    LeftIndexIntermediate = 28
    LeftIndexDistal = 29
    LeftMiddleProximal = 30
    LeftMiddleIntermediate = 31
    LeftMiddleDistal = 32
    LeftRingProximal = 33
    LeftRingIntermediate = 34
    LeftRingDistal = 35
    LeftLittleProximal = 36
    LeftLittleIntermediate = 37
    LeftLittleDistal = 38
    RightThumbProximal = 39
    RightThumbIntermediate = 40
    RightThumbDistal = 41
    RightIndexProximal = 42
    RightIndexIntermediate = 43
    RightIndexDistal = 44
    RightMiddleProximal = 45
    RightMiddleIntermediate = 46
    RightMiddleDistal = 47
    RightRingProximal = 48
    RightRingIntermediate = 49
    RightRingDistal = 50
    RightLittleProximal = 51
    RightLittleIntermediate = 52
    RightLittleDistal = 53
    LastBone = 55

# UnityEngine.IMECompositionMode
class IMECompositionMode(IntFlag):
    Auto = 0
    On = 1
    Off = 2

# UnityEngine.ImagePosition
class ImagePosition(IntFlag):
    ImageLeft = 0
    ImageAbove = 1
    ImageOnly = 2
    TextOnly = 3

# UnityEngine.InspectorSort
class InspectorSort(IntFlag):
    ByName = 0
    ByValue = 1

# UnityEngine.InspectorSortDirection
class InspectorSortDirection(IntFlag):
    Ascending = 0
    Descending = 1

# UnityEngine.KeyCode
class KeyCode(IntFlag):
    NONE = 0
    Backspace = 8
    Delete = 127
    Tab = 9
    Clear = 12
    Return = 13
    Pause = 19
    Escape = 27
    Space = 32
    Keypad0 = 256
    Keypad1 = 257
    Keypad2 = 258
    Keypad3 = 259
    Keypad4 = 260
    Keypad5 = 261
    Keypad6 = 262
    Keypad7 = 263
    Keypad8 = 264
    Keypad9 = 265
    KeypadPeriod = 266
    KeypadDivide = 267
    KeypadMultiply = 268
    KeypadMinus = 269
    KeypadPlus = 270
    KeypadEnter = 271
    KeypadEquals = 272
    UpArrow = 273
    DownArrow = 274
    RightArrow = 275
    LeftArrow = 276
    Insert = 277
    Home = 278
    End = 279
    PageUp = 280
    PageDown = 281
    F1 = 282
    F2 = 283
    F3 = 284
    F4 = 285
    F5 = 286
    F6 = 287
    F7 = 288
    F8 = 289
    F9 = 290
    F10 = 291
    F11 = 292
    F12 = 293
    F13 = 294
    F14 = 295
    F15 = 296
    Alpha0 = 48
    Alpha1 = 49
    Alpha2 = 50
    Alpha3 = 51
    Alpha4 = 52
    Alpha5 = 53
    Alpha6 = 54
    Alpha7 = 55
    Alpha8 = 56
    Alpha9 = 57
    Exclaim = 33
    DoubleQuote = 34
    Hash = 35
    Dollar = 36
    Percent = 37
    Ampersand = 38
    Quote = 39
    LeftParen = 40
    RightParen = 41
    Asterisk = 42
    Plus = 43
    Comma = 44
    Minus = 45
    Period = 46
    Slash = 47
    Colon = 58
    Semicolon = 59
    Less = 60
    Equals = 61
    Greater = 62
    Question = 63
    At = 64
    LeftBracket = 91
    Backslash = 92
    RightBracket = 93
    Caret = 94
    Underscore = 95
    BackQuote = 96
    A = 97
    B = 98
    C = 99
    D = 100
    E = 101
    F = 102
    G = 103
    H = 104
    I = 105
    J = 106
    K = 107
    L = 108
    M = 109
    N = 110
    O = 111
    P = 112
    Q = 113
    R = 114
    S = 115
    T = 116
    U = 117
    V = 118
    W = 119
    X = 120
    Y = 121
    Z = 122
    LeftCurlyBracket = 123
    Pipe = 124
    RightCurlyBracket = 125
    Tilde = 126
    Numlock = 300
    CapsLock = 301
    ScrollLock = 302
    RightShift = 303
    LeftShift = 304
    RightControl = 305
    LeftControl = 306
    RightAlt = 307
    LeftAlt = 308
    LeftMeta = 310
    LeftCommand = 310
    LeftApple = 310
    LeftWindows = 311
    RightMeta = 309
    RightCommand = 309
    RightApple = 309
    RightWindows = 312
    AltGr = 313
    Help = 315
    Print = 316
    SysReq = 317
    Break = 318
    Menu = 319
    WheelUp = 321
    WheelDown = 322
    F16 = 670
    F17 = 671
    F18 = 672
    F19 = 673
    F20 = 674
    F21 = 675
    F22 = 676
    F23 = 677
    F24 = 678
    Mouse0 = 323
    Mouse1 = 324
    Mouse2 = 325
    Mouse3 = 326
    Mouse4 = 327
    Mouse5 = 328
    Mouse6 = 329
    JoystickButton0 = 330
    JoystickButton1 = 331
    JoystickButton2 = 332
    JoystickButton3 = 333
    JoystickButton4 = 334
    JoystickButton5 = 335
    JoystickButton6 = 336
    JoystickButton7 = 337
    JoystickButton8 = 338
    JoystickButton9 = 339
    JoystickButton10 = 340
    JoystickButton11 = 341
    JoystickButton12 = 342
    JoystickButton13 = 343
    JoystickButton14 = 344
    JoystickButton15 = 345
    JoystickButton16 = 346
    JoystickButton17 = 347
    JoystickButton18 = 348
    JoystickButton19 = 349
    Joystick1Button0 = 350
    Joystick1Button1 = 351
    Joystick1Button2 = 352
    Joystick1Button3 = 353
    Joystick1Button4 = 354
    Joystick1Button5 = 355
    Joystick1Button6 = 356
    Joystick1Button7 = 357
    Joystick1Button8 = 358
    Joystick1Button9 = 359
    Joystick1Button10 = 360
    Joystick1Button11 = 361
    Joystick1Button12 = 362
    Joystick1Button13 = 363
    Joystick1Button14 = 364
    Joystick1Button15 = 365
    Joystick1Button16 = 366
    Joystick1Button17 = 367
    Joystick1Button18 = 368
    Joystick1Button19 = 369
    Joystick2Button0 = 370
    Joystick2Button1 = 371
    Joystick2Button2 = 372
    Joystick2Button3 = 373
    Joystick2Button4 = 374
    Joystick2Button5 = 375
    Joystick2Button6 = 376
    Joystick2Button7 = 377
    Joystick2Button8 = 378
    Joystick2Button9 = 379
    Joystick2Button10 = 380
    Joystick2Button11 = 381
    Joystick2Button12 = 382
    Joystick2Button13 = 383
    Joystick2Button14 = 384
    Joystick2Button15 = 385
    Joystick2Button16 = 386
    Joystick2Button17 = 387
    Joystick2Button18 = 388
    Joystick2Button19 = 389
    Joystick3Button0 = 390
    Joystick3Button1 = 391
    Joystick3Button2 = 392
    Joystick3Button3 = 393
    Joystick3Button4 = 394
    Joystick3Button5 = 395
    Joystick3Button6 = 396
    Joystick3Button7 = 397
    Joystick3Button8 = 398
    Joystick3Button9 = 399
    Joystick3Button10 = 400
    Joystick3Button11 = 401
    Joystick3Button12 = 402
    Joystick3Button13 = 403
    Joystick3Button14 = 404
    Joystick3Button15 = 405
    Joystick3Button16 = 406
    Joystick3Button17 = 407
    Joystick3Button18 = 408
    Joystick3Button19 = 409
    Joystick4Button0 = 410
    Joystick4Button1 = 411
    Joystick4Button2 = 412
    Joystick4Button3 = 413
    Joystick4Button4 = 414
    Joystick4Button5 = 415
    Joystick4Button6 = 416
    Joystick4Button7 = 417
    Joystick4Button8 = 418
    Joystick4Button9 = 419
    Joystick4Button10 = 420
    Joystick4Button11 = 421
    Joystick4Button12 = 422
    Joystick4Button13 = 423
    Joystick4Button14 = 424
    Joystick4Button15 = 425
    Joystick4Button16 = 426
    Joystick4Button17 = 427
    Joystick4Button18 = 428
    Joystick4Button19 = 429
    Joystick5Button0 = 430
    Joystick5Button1 = 431
    Joystick5Button2 = 432
    Joystick5Button3 = 433
    Joystick5Button4 = 434
    Joystick5Button5 = 435
    Joystick5Button6 = 436
    Joystick5Button7 = 437
    Joystick5Button8 = 438
    Joystick5Button9 = 439
    Joystick5Button10 = 440
    Joystick5Button11 = 441
    Joystick5Button12 = 442
    Joystick5Button13 = 443
    Joystick5Button14 = 444
    Joystick5Button15 = 445
    Joystick5Button16 = 446
    Joystick5Button17 = 447
    Joystick5Button18 = 448
    Joystick5Button19 = 449
    Joystick6Button0 = 450
    Joystick6Button1 = 451
    Joystick6Button2 = 452
    Joystick6Button3 = 453
    Joystick6Button4 = 454
    Joystick6Button5 = 455
    Joystick6Button6 = 456
    Joystick6Button7 = 457
    Joystick6Button8 = 458
    Joystick6Button9 = 459
    Joystick6Button10 = 460
    Joystick6Button11 = 461
    Joystick6Button12 = 462
    Joystick6Button13 = 463
    Joystick6Button14 = 464
    Joystick6Button15 = 465
    Joystick6Button16 = 466
    Joystick6Button17 = 467
    Joystick6Button18 = 468
    Joystick6Button19 = 469
    Joystick7Button0 = 470
    Joystick7Button1 = 471
    Joystick7Button2 = 472
    Joystick7Button3 = 473
    Joystick7Button4 = 474
    Joystick7Button5 = 475
    Joystick7Button6 = 476
    Joystick7Button7 = 477
    Joystick7Button8 = 478
    Joystick7Button9 = 479
    Joystick7Button10 = 480
    Joystick7Button11 = 481
    Joystick7Button12 = 482
    Joystick7Button13 = 483
    Joystick7Button14 = 484
    Joystick7Button15 = 485
    Joystick7Button16 = 486
    Joystick7Button17 = 487
    Joystick7Button18 = 488
    Joystick7Button19 = 489
    Joystick8Button0 = 490
    Joystick8Button1 = 491
    Joystick8Button2 = 492
    Joystick8Button3 = 493
    Joystick8Button4 = 494
    Joystick8Button5 = 495
    Joystick8Button6 = 496
    Joystick8Button7 = 497
    Joystick8Button8 = 498
    Joystick8Button9 = 499
    Joystick8Button10 = 500
    Joystick8Button11 = 501
    Joystick8Button12 = 502
    Joystick8Button13 = 503
    Joystick8Button14 = 504
    Joystick8Button15 = 505
    Joystick8Button16 = 506
    Joystick8Button17 = 507
    Joystick8Button18 = 508
    Joystick8Button19 = 509

# UnityEngine.LODFadeMode
class LODFadeMode(IntFlag):
    NONE = 0
    CrossFade = 1
    SpeedTree = 2

# UnityEngine.LightAnchor
class LightAnchor(IntFlag):
    World = 0
    Local = 1

# UnityEngine.LightShadows
class LightShadows(IntFlag):
    NONE = 0
    Hard = 1
    Soft = 2

# UnityEngine.LightShape
class LightShape(IntFlag):
    Cone = 0
    Pyramid = 1
    Box = 2

# UnityEngine.LightType
class LightType(IntFlag):
    Spot = 0
    Directional = 1
    Point = 2
    Area = 3
    Rectangle = 3
    Disc = 4
    Pyramid = 5
    Box = 6
    Tube = 7

# UnityEngine.LightmapBakeType
class LightmapBakeType(IntFlag):
    Realtime = 4
    Baked = 2
    Mixed = 1

# UnityEngine.LightmapsMode
class LightmapsMode(IntFlag):
    NonDirectional = 0
    CombinedDirectional = 1

# UnityEngine.LogOption
class LogOption(IntFlag):
    NONE = 0
    NoStacktrace = 1

# UnityEngine.LogType
class LogType(IntFlag):
    Error = 0
    Assert = 1
    Warning = 2
    Log = 3
    Exception = 4

# UnityEngine.MaterialGlobalIlluminationFlags
class MaterialGlobalIlluminationFlags(IntFlag):
    NONE = 0
    RealtimeEmissive = 1
    BakedEmissive = 2
    EmissiveIsBlack = 4
    AnyEmissive = 3

# UnityEngine.MaterialPropertyType
class MaterialPropertyType(IntFlag):
    Float = 0
    Int = 1
    Vector = 2
    Matrix = 3
    Texture = 4
    ConstantBuffer = 5
    ComputeBuffer = 6

# UnityEngine.MeshTopology
class MeshTopology(IntFlag):
    Triangles = 0
    Quads = 2
    Lines = 3
    LineStrip = 4
    Points = 5

# UnityEngine.MixedLightingMode
class MixedLightingMode(IntFlag):
    IndirectOnly = 0
    Shadowmask = 2
    Subtractive = 1

# UnityEngine.MotionVectorGenerationMode
class MotionVectorGenerationMode(IntFlag):
    Camera = 0
    Object = 1
    ForceNoMotion = 2

# UnityEngine.NPOTSupport
class NPOTSupport(IntFlag):
    NONE = 0
    Restricted = 1
    Full = 2

# UnityEngine.ObjectDispatcher
class ObjectDispatcher(IntFlag):
    GlobalTRS = 0
    LocalTRS = 1
    Hierarchy = 2

# UnityEngine.ObjectDispatcher
class ObjectDispatcher(IntFlag):
    SceneObjects = 1
    Assets = 2
    EditorOnlyObjects = 4
    Default = 3
    All = 7

# UnityEngine.OperatingSystemFamily
class OperatingSystemFamily(IntFlag):
    Other = 0
    MacOSX = 1
    Windows = 2
    Linux = 3

# UnityEngine.ParticleSystemBakeMeshOptions
class ParticleSystemBakeMeshOptions(IntFlag):
    BakeRotationAndScale = 1
    BakePosition = 2
    Default = 0

# UnityEngine.ParticleSystemBakeTextureOptions
class ParticleSystemBakeTextureOptions(IntFlag):
    BakeRotationAndScale = 1
    BakePosition = 2
    PerVertex = 4
    PerParticle = 8
    IncludeParticleIndices = 16
    Default = 4

# UnityEngine.ParticleSystemCurveMode
class ParticleSystemCurveMode(IntFlag):
    Constant = 0
    Curve = 1
    TwoCurves = 2
    TwoConstants = 3

# UnityEngine.ParticleSystemCustomData
class ParticleSystemCustomData(IntFlag):
    Custom1 = 0
    Custom2 = 1

# UnityEngine.ParticleSystemCustomDataMode
class ParticleSystemCustomDataMode(IntFlag):
    Disabled = 0
    Vector = 1
    Color = 2

# UnityEngine.ParticleSystemGradientMode
class ParticleSystemGradientMode(IntFlag):
    Color = 0
    Gradient = 1
    TwoColors = 2
    TwoGradients = 3
    RandomColor = 4

# UnityEngine.ParticleSystemMeshDistribution
class ParticleSystemMeshDistribution(IntFlag):
    UniformRandom = 0
    NonUniformRandom = 1

# UnityEngine.ParticleSystemNoiseQuality
class ParticleSystemNoiseQuality(IntFlag):
    Low = 0
    Medium = 1
    High = 2

# UnityEngine.ParticleSystemRenderMode
class ParticleSystemRenderMode(IntFlag):
    Billboard = 0
    Stretch = 1
    HorizontalBillboard = 2
    VerticalBillboard = 3
    Mesh = 4
    NONE = 5

# UnityEngine.ParticleSystemRenderSpace
class ParticleSystemRenderSpace(IntFlag):
    View = 0
    World = 1
    Local = 2
    Facing = 3
    Velocity = 4

# UnityEngine.ParticleSystemScalingMode
class ParticleSystemScalingMode(IntFlag):
    Hierarchy = 0
    Local = 1
    Shape = 2

# UnityEngine.ParticleSystemShapeMultiModeValue
class ParticleSystemShapeMultiModeValue(IntFlag):
    Random = 0
    Loop = 1
    PingPong = 2
    BurstSpread = 3

# UnityEngine.ParticleSystemShapeType
class ParticleSystemShapeType(IntFlag):
    Sphere = 0
    SphereShell = 1
    Hemisphere = 2
    HemisphereShell = 3
    Cone = 4
    Box = 5
    Mesh = 6
    ConeShell = 7
    ConeVolume = 8
    ConeVolumeShell = 9
    Circle = 10
    CircleEdge = 11
    SingleSidedEdge = 12
    MeshRenderer = 13
    SkinnedMeshRenderer = 14
    BoxShell = 15
    BoxEdge = 16
    Donut = 17
    Rectangle = 18
    Sprite = 19
    SpriteRenderer = 20

# UnityEngine.ParticleSystemSimulationSpace
class ParticleSystemSimulationSpace(IntFlag):
    Local = 0
    World = 1
    Custom = 2

# UnityEngine.ParticleSystemSortMode
class ParticleSystemSortMode(IntFlag):
    NONE = 0
    Distance = 1
    OldestInFront = 2
    YoungestInFront = 3
    Depth = 4
    DistanceReverse = 5
    DepthReverse = 6

# UnityEngine.ParticleSystemStopBehavior
class ParticleSystemStopBehavior(IntFlag):
    StopEmittingAndClear = 0
    StopEmitting = 1

# UnityEngine.ParticleSystemSubEmitterProperties
class ParticleSystemSubEmitterProperties(IntFlag):
    InheritNothing = 0
    InheritEverything = 31
    InheritColor = 1
    InheritSize = 2
    InheritRotation = 4
    InheritLifetime = 8
    InheritDuration = 16

# UnityEngine.ParticleSystemSubEmitterType
class ParticleSystemSubEmitterType(IntFlag):
    Birth = 0
    Collision = 1
    Death = 2
    Trigger = 3
    Manual = 4

# UnityEngine.ParticleSystemTrailTextureMode
class ParticleSystemTrailTextureMode(IntFlag):
    Stretch = 0
    Tile = 1
    DistributePerSegment = 2
    RepeatPerSegment = 3
    Static = 4

# UnityEngine.ParticleSystemVertexStream
class ParticleSystemVertexStream(IntFlag):
    Position = 0
    Normal = 1
    Tangent = 2
    Color = 3
    UV = 4
    UV2 = 5
    UV3 = 6
    UV4 = 7
    AnimBlend = 8
    AnimFrame = 9
    Center = 10
    VertexID = 11
    SizeX = 12
    SizeXY = 13
    SizeXYZ = 14
    Rotation = 15
    Rotation3D = 16
    RotationSpeed = 17
    RotationSpeed3D = 18
    Velocity = 19
    Speed = 20
    AgePercent = 21
    InvStartLifetime = 22
    StableRandomX = 23
    StableRandomXY = 24
    StableRandomXYZ = 25
    StableRandomXYZW = 26
    VaryingRandomX = 27
    VaryingRandomXY = 28
    VaryingRandomXYZ = 29
    VaryingRandomXYZW = 30
    Custom1X = 31
    Custom1XY = 32
    Custom1XYZ = 33
    Custom1XYZW = 34
    Custom2X = 35
    Custom2XY = 36
    Custom2XYZ = 37
    Custom2XYZW = 38
    NoiseSumX = 39
    NoiseSumXY = 40
    NoiseSumXYZ = 41
    NoiseImpulseX = 42
    NoiseImpulseXY = 43
    NoiseImpulseXYZ = 44
    MeshIndex = 45
    ParticleIndex = 46
    ColorPackedAsTwoFloats = 47
    MeshAxisOfRotation = 48
    NextTrailCenter = 49
    PreviousTrailCenter = 50
    PercentageAlongTrail = 51
    TrailWidth = 52

# UnityEngine.ParticleSystemVertexStreams
class ParticleSystemVertexStreams(IntFlag):
    Position = 1
    Normal = 2
    Tangent = 4
    Color = 8
    UV = 16
    UV2BlendAndFrame = 32
    CenterAndVertexID = 64
    Size = 128
    Rotation = 256
    Velocity = 512
    Lifetime = 1024
    Custom1 = 2048
    Custom2 = 4096
    Random = 8192
    NONE = 0
    All = 2147483647

# UnityEngine.PenEventType
class PenEventType(IntFlag):
    NoContact = 0
    PenDown = 1
    PenUp = 2

# UnityEngine.PenStatus
class PenStatus(IntFlag):
    NONE = 0
    Contact = 1
    Barrel = 2
    Inverted = 4
    Eraser = 8

# UnityEngine.PointerType
class PointerType(IntFlag):
    Mouse = 0
    Touch = 1
    Pen = 2

# UnityEngine.PrimitiveType
class PrimitiveType(IntFlag):
    Sphere = 0
    Capsule = 1
    Cylinder = 2
    Cube = 3
    Plane = 4
    Quad = 5

# UnityEngine.QueryTriggerInteraction
class QueryTriggerInteraction(IntFlag):
    UseGlobal = 0
    Ignore = 1
    Collide = 2

# UnityEngine.RectTransform
class RectTransform(IntFlag):
    Left = 0
    Right = 1
    Top = 2
    Bottom = 3

# UnityEngine.RectTransform
class RectTransform(IntFlag):
    Horizontal = 0
    Vertical = 1

# UnityEngine.ReflectionProbe
class ReflectionProbe(IntFlag):
    ReflectionProbeAdded = 0
    ReflectionProbeRemoved = 1

# UnityEngine.RemoteConfigSettingsHelper
class RemoteConfigSettingsHelper(IntFlag):
    kUnknown = 0
    kIntVal = 1
    kInt64Val = 2
    kUInt64Val = 3
    kDoubleVal = 4
    kBoolVal = 5
    kStringVal = 6
    kArrayVal = 7
    kMixedArrayVal = 8
    kMapVal = 9
    kMaxTags = 10

# UnityEngine.RenderMode
class RenderMode(IntFlag):
    ScreenSpaceOverlay = 0
    ScreenSpaceCamera = 1
    WorldSpace = 2

# UnityEngine.RenderTextureCreationFlags
class RenderTextureCreationFlags(IntFlag):
    MipMap = 1
    AutoGenerateMips = 2
    SRGB = 4
    EyeTexture = 8
    EnableRandomWrite = 16
    CreatedFromScript = 32
    AllowVerticalFlip = 128
    NoResolvedColorSurface = 256
    DynamicallyScalable = 1024
    BindMS = 2048
    ShadingRate = 16384
    DynamicallyScalableExplicit = 131072

# UnityEngine.RenderTextureFormat
class RenderTextureFormat(IntFlag):
    ARGB32 = 0
    Depth = 1
    ARGBHalf = 2
    Shadowmap = 3
    RGB565 = 4
    ARGB4444 = 5
    ARGB1555 = 6
    Default = 7
    ARGB2101010 = 8
    DefaultHDR = 9
    ARGB64 = 10
    ARGBFloat = 11
    RGFloat = 12
    RGHalf = 13
    RFloat = 14
    RHalf = 15
    R8 = 16
    ARGBInt = 17
    RGInt = 18
    RInt = 19
    BGRA32 = 20
    RGB111110Float = 22
    RG32 = 23
    RGBAUShort = 24
    RG16 = 25
    BGRA10101010_XR = 26
    BGR101010_XR = 27
    R16 = 28

# UnityEngine.RenderTextureMemoryless
class RenderTextureMemoryless(IntFlag):
    NONE = 0
    Color = 1
    Depth = 2
    MSAA = 4

# UnityEngine.RenderTextureReadWrite
class RenderTextureReadWrite(IntFlag):
    Default = 0
    Linear = 1
    sRGB = 2

# UnityEngine.RenderingPath
class RenderingPath(IntFlag):
    UsePlayerSettings = -1
    VertexLit = 0
    Forward = 1
    DeferredLighting = 2
    DeferredShading = 3

# UnityEngine.RotationOrder
class RotationOrder(IntFlag):
    OrderXYZ = 0
    OrderXZY = 1
    OrderYZX = 2
    OrderYXZ = 3
    OrderZXY = 4
    OrderZYX = 5

# UnityEngine.RuntimeInitializeLoadType
class RuntimeInitializeLoadType(IntFlag):
    AfterSceneLoad = 0
    BeforeSceneLoad = 1
    AfterAssembliesLoaded = 2
    BeforeSplashScreen = 3
    SubsystemRegistration = 4

# UnityEngine.RuntimePlatform
class RuntimePlatform(IntFlag):
    OSXEditor = 0
    OSXPlayer = 1
    WindowsPlayer = 2
    OSXWebPlayer = 3
    OSXDashboardPlayer = 4
    WindowsWebPlayer = 5
    WindowsEditor = 7
    IPhonePlayer = 8
    XBOX360 = 10
    PS3 = 9
    Android = 11
    NaCl = 12
    FlashPlayer = 15
    LinuxPlayer = 13
    LinuxEditor = 16
    WebGLPlayer = 17
    MetroPlayerX86 = 18
    WSAPlayerX86 = 18
    MetroPlayerX64 = 19
    WSAPlayerX64 = 19
    MetroPlayerARM = 20
    WSAPlayerARM = 20
    WP8Player = 21
    BlackBerryPlayer = 22
    TizenPlayer = 23
    PSP2 = 24
    PS4 = 25
    PSM = 26
    XboxOne = 27
    SamsungTVPlayer = 28
    WiiU = 30
    tvOS = 31
    Switch = 32
    Lumin = 33
    Stadia = 34
    CloudRendering = -1
    LinuxHeadlessSimulation = 35
    GameCoreScarlett = -1
    GameCoreXboxSeries = 36
    GameCoreXboxOne = 37
    PS5 = 38
    EmbeddedLinuxArm64 = 39
    EmbeddedLinuxArm32 = 40
    EmbeddedLinuxX64 = 41
    EmbeddedLinuxX86 = 42
    LinuxServer = 43
    WindowsServer = 44
    OSXServer = 45
    QNXArm32 = 46
    QNXArm64 = 47
    QNXX64 = 48
    QNXX86 = 49
    VisionOS = 50
    ReservedCFE = 51
    KeplerArm64 = 52
    KeplerX64 = 53

# UnityEngine.ScaleMode
class ScaleMode(IntFlag):
    StretchToFill = 0
    ScaleAndCrop = 1
    ScaleToFit = 2

# UnityEngine.ScreenCapture
class ScreenCapture(IntFlag):
    LeftEye = 1
    RightEye = 2
    BothEyes = 3
    MotionVectors = 4

# UnityEngine.ScreenOrientation
class ScreenOrientation(IntFlag):
    Portrait = 1
    PortraitUpsideDown = 2
    LandscapeLeft = 3
    LandscapeRight = 4
    AutoRotation = 5
    Unknown = 0
    Landscape = 3

# UnityEngine.SendMessageOptions
class SendMessageOptions(IntFlag):
    RequireReceiver = 0
    DontRequireReceiver = 1

# UnityEngine.ShadowObjectsFilter
class ShadowObjectsFilter(IntFlag):
    AllObjects = 0
    DynamicOnly = 1
    StaticOnly = 2

# UnityEngine.ShadowmaskMode
class ShadowmaskMode(IntFlag):
    Shadowmask = 0
    DistanceShadowmask = 1

# UnityEngine.Space
class Space(IntFlag):
    World = 0
    Self = 1

# UnityEngine.SpriteDrawMode
class SpriteDrawMode(IntFlag):
    Simple = 0
    Sliced = 1
    Tiled = 2

# UnityEngine.SpriteMask
class SpriteMask(IntFlag):
    Sprite = 0
    SupportedRenderers = 1

# UnityEngine.SpriteMaskInteraction
class SpriteMaskInteraction(IntFlag):
    NONE = 0
    VisibleInsideMask = 1
    VisibleOutsideMask = 2

# UnityEngine.SpriteMeshType
class SpriteMeshType(IntFlag):
    FullRect = 0
    Tight = 1

# UnityEngine.SpritePackingMode
class SpritePackingMode(IntFlag):
    Tight = 0
    Rectangle = 1

# UnityEngine.SpritePackingRotation
class SpritePackingRotation(IntFlag):
    NONE = 0
    FlipHorizontal = 1
    FlipVertical = 2
    Rotate180 = 3
    Any = 15

# UnityEngine.SpriteSortPoint
class SpriteSortPoint(IntFlag):
    Center = 0
    Pivot = 1

# UnityEngine.SpriteTileMode
class SpriteTileMode(IntFlag):
    Continuous = 0
    Adaptive = 1

# UnityEngine.StackTraceLogType
class StackTraceLogType(IntFlag):
    NONE = 0
    ScriptOnly = 1
    Full = 2

# UnityEngine.StandaloneRenderResize
class StandaloneRenderResize(IntFlag):
    Enabled = 0
    Disabled = 1

# UnityEngine.StateInfoIndex
class StateInfoIndex(IntFlag):
    CurrentState = 0
    NextState = 1
    ExitState = 2
    InterruptedState = 3

# UnityEngine.StereoTargetEyeMask
class StereoTargetEyeMask(IntFlag):
    NONE = 0
    Left = 1
    Right = 2
    Both = 3

# UnityEngine.SystemLanguage
class SystemLanguage(IntFlag):
    Afrikaans = 0
    Arabic = 1
    Basque = 2
    Belarusian = 3
    Bulgarian = 4
    Catalan = 5
    Chinese = 6
    Czech = 7
    Danish = 8
    Dutch = 9
    English = 10
    Estonian = 11
    Faroese = 12
    Finnish = 13
    French = 14
    German = 15
    Greek = 16
    Hebrew = 17
    Icelandic = 19
    Indonesian = 20
    Italian = 21
    Japanese = 22
    Korean = 23
    Latvian = 24
    Lithuanian = 25
    Norwegian = 26
    Polish = 27
    Portuguese = 28
    Romanian = 29
    Russian = 30
    SerboCroatian = 31
    Slovak = 32
    Slovenian = 33
    Spanish = 34
    Swedish = 35
    Thai = 36
    Turkish = 37
    Ukrainian = 38
    Vietnamese = 39
    ChineseSimplified = 40
    ChineseTraditional = 41
    Hindi = 42
    Unknown = 43
    Hungarian = 18

# UnityEngine.TerrainData
class TerrainData(IntFlag):
    MaxHeightmapRes = 0
    MinDetailResPerPatch = 1
    MaxDetailResPerPatch = 2
    MaxDetailPatchCount = 3
    MaxCoveragePerRes = 4
    MinAlphamapRes = 5
    MaxAlphamapRes = 6
    MinBaseMapRes = 7
    MaxBaseMapRes = 8

# UnityEngine.TextAlignment
class TextAlignment(IntFlag):
    Left = 0
    Center = 1
    Right = 2

# UnityEngine.TextAnchor
class TextAnchor(IntFlag):
    UpperLeft = 0
    UpperCenter = 1
    UpperRight = 2
    MiddleLeft = 3
    MiddleCenter = 4
    MiddleRight = 5
    LowerLeft = 6
    LowerCenter = 7
    LowerRight = 8

# UnityEngine.TextAsset
class TextAsset(IntFlag):
    NONE = 0
    CreateNativeObject = 1

# UnityEngine.TextClipping
class TextClipping(IntFlag):
    Overflow = 0
    Clip = 1
    Ellipsis = 2

# UnityEngine.TextEditOp
class TextEditOp(IntFlag):
    MoveLeft = 0
    MoveRight = 1
    MoveUp = 2
    MoveDown = 3
    MoveLineStart = 4
    MoveLineEnd = 5
    MoveTextStart = 6
    MoveTextEnd = 7
    MovePageUp = 8
    MovePageDown = 9
    MoveGraphicalLineStart = 10
    MoveGraphicalLineEnd = 11
    MoveWordLeft = 12
    MoveWordRight = 13
    MoveParagraphForward = 14
    MoveParagraphBackward = 15
    MoveToStartOfNextWord = 16
    MoveToEndOfPreviousWord = 17
    Delete = 18
    Backspace = 19
    DeleteWordBack = 20
    DeleteWordForward = 21
    DeleteLineBack = 22
    Cut = 23
    Paste = 24
    ScrollStart = 25
    ScrollEnd = 26
    ScrollPageUp = 27
    ScrollPageDown = 28

# UnityEngine.TextEditor
class TextEditor(IntFlag):
    WORDS = 0
    PARAGRAPHS = 1

# UnityEngine.TextGenerationError
class TextGenerationError(IntFlag):
    NONE = 0
    CustomSizeOnNonDynamicFont = 1
    CustomStyleOnNonDynamicFont = 2
    NoFont = 4

# UnityEngine.TextGeneratorType
class TextGeneratorType(IntFlag):
    Standard = 0
    Advanced = 1

# UnityEngine.TextSelectOp
class TextSelectOp(IntFlag):
    SelectLeft = 0
    SelectRight = 1
    SelectUp = 2
    SelectDown = 3
    SelectTextStart = 4
    SelectTextEnd = 5
    SelectPageUp = 6
    SelectPageDown = 7
    ExpandSelectGraphicalLineStart = 8
    ExpandSelectGraphicalLineEnd = 9
    SelectGraphicalLineStart = 10
    SelectGraphicalLineEnd = 11
    SelectWordLeft = 12
    SelectWordRight = 13
    SelectToEndOfPreviousWord = 14
    SelectToStartOfNextWord = 15
    SelectParagraphBackward = 16
    SelectParagraphForward = 17
    Copy = 18
    SelectAll = 19
    SelectNone = 20

# UnityEngine.TextSelectingUtilities
class TextSelectingUtilities(IntFlag):
    LetterLike = 0
    Symbol = 1
    Symbol2 = 2
    WhiteSpace = 3
    NewLine = 4

# UnityEngine.TextSelectingUtilities
class TextSelectingUtilities(IntFlag):
    Forward = 0
    Backward = 1

# UnityEngine.TextureColorSpace
class TextureColorSpace(IntFlag):
    Linear = 0
    sRGB = 1

# UnityEngine.TextureFormat
class TextureFormat(IntFlag):
    Alpha8 = 1
    ARGB4444 = 2
    RGB24 = 3
    RGBA32 = 4
    ARGB32 = 5
    RGB565 = 7
    R16 = 9
    DXT1 = 10
    DXT5 = 12
    RGBA4444 = 13
    BGRA32 = 14
    RHalf = 15
    RGHalf = 16
    RGBAHalf = 17
    RFloat = 18
    RGFloat = 19
    RGBAFloat = 20
    YUY2 = 21
    RGB9e5Float = 22
    BC4 = 26
    BC5 = 27
    BC6H = 24
    BC7 = 25
    DXT1Crunched = 28
    DXT5Crunched = 29
    PVRTC_RGB2 = 30
    PVRTC_RGBA2 = 31
    PVRTC_RGB4 = 32
    PVRTC_RGBA4 = 33
    ETC_RGB4 = 34
    EAC_R = 41
    EAC_R_SIGNED = 42
    EAC_RG = 43
    EAC_RG_SIGNED = 44
    ETC2_RGB = 45
    ETC2_RGBA1 = 46
    ETC2_RGBA8 = 47
    ASTC_4x4 = 48
    ASTC_5x5 = 49
    ASTC_6x6 = 50
    ASTC_8x8 = 51
    ASTC_10x10 = 52
    ASTC_12x12 = 53
    RG16 = 62
    R8 = 63
    ETC_RGB4Crunched = 64
    ETC2_RGBA8Crunched = 65
    ASTC_HDR_4x4 = 66
    ASTC_HDR_5x5 = 67
    ASTC_HDR_6x6 = 68
    ASTC_HDR_8x8 = 69
    ASTC_HDR_10x10 = 70
    ASTC_HDR_12x12 = 71
    RG32 = 72
    RGB48 = 73
    RGBA64 = 74
    R8_SIGNED = 75
    RG16_SIGNED = 76
    RGB24_SIGNED = 77
    RGBA32_SIGNED = 78
    R16_SIGNED = 79
    RG32_SIGNED = 80
    RGB48_SIGNED = 81
    RGBA64_SIGNED = 82

# UnityEngine.TextureWrapMode
class TextureWrapMode(IntFlag):
    Repeat = 0
    Clamp = 1
    Mirror = 2
    MirrorOnce = 3

# UnityEngine.TouchPhase
class TouchPhase(IntFlag):
    Began = 0
    Moved = 1
    Stationary = 2
    Ended = 3
    Canceled = 4

# UnityEngine.TouchScreenKeyboard
class TouchScreenKeyboard(IntFlag):
    Visible = 0
    Done = 1
    Canceled = 2
    LostFocus = 3

# UnityEngine.TouchScreenKeyboard
class TouchScreenKeyboard(IntFlag):
    Customizable = 0
    AlwaysVisible = 1
    AlwaysHidden = 2

# UnityEngine.TouchScreenKeyboardType
class TouchScreenKeyboardType(IntFlag):
    Default = 0
    ASCIICapable = 1
    NumbersAndPunctuation = 2
    URL = 3
    NumberPad = 4
    PhonePad = 5
    NamePhonePad = 6
    EmailAddress = 7
    NintendoNetworkAccount = 8
    Social = 9
    Search = 10
    DecimalPad = 11
    OneTimeCode = 12

# UnityEngine.TouchType
class TouchType(IntFlag):
    Direct = 0
    Indirect = 1
    Stylus = 2

# UnityEngine.TransferFunction
class TransferFunction(IntFlag):
    Unknown = -1
    sRGB = 0
    BT1886 = 1
    PQ = 2
    Linear = 3
    Gamma22 = 4

# UnityEngine.TransparencySortMode
class TransparencySortMode(IntFlag):
    Default = 0
    Perspective = 1
    Orthographic = 2
    CustomAxis = 3

# UnityEngine.UISystemProfilerApi
class UISystemProfilerApi(IntFlag):
    Layout = 0
    Render = 1

# UnityEngine.VRTextureUsage
class VRTextureUsage(IntFlag):
    NONE = 0
    OneEye = 1
    TwoEyes = 2
    DeviceSpecific = 3

# UnityEngine.VerticalWrapMode
class VerticalWrapMode(IntFlag):
    Truncate = 0
    Overflow = 1

# UnityEngine.WaitTimeoutMode
class WaitTimeoutMode(IntFlag):
    Realtime = 0
    InGameTime = 1

# UnityEngine.WeightedMode
class WeightedMode(IntFlag):
    NONE = 0
    In = 1
    Out = 2
    Both = 3

# UnityEngine.WhitePoint
class WhitePoint(IntFlag):
    Unknown = -1
    D65 = 0

# UnityEngine.WrapMode
class WrapMode(IntFlag):
    Once = 1
    Loop = 2
    PingPong = 4
    Default = 0
    ClampForever = 8
    Clamp = 1

