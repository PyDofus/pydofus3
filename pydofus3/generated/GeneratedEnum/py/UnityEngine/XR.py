from enum import IntFlag

# UnityEngine.XR.AvailableTrackingData
class AvailableTrackingData(IntFlag):
    NONE = 0
    PositionAvailable = 1
    RotationAvailable = 2
    VelocityAvailable = 4
    AngularVelocityAvailable = 8
    AccelerationAvailable = 16
    AngularAccelerationAvailable = 32

# UnityEngine.XR.ConnectionChangeType
class ConnectionChangeType(IntFlag):
    Connected = 0
    Disconnected = 1
    ConfigChange = 2

# UnityEngine.XR.InputDeviceCharacteristics
class InputDeviceCharacteristics(IntFlag):
    NONE = 0
    HeadMounted = 1
    Camera = 2
    HeldInHand = 4
    HandTracking = 8
    EyeTracking = 16
    TrackedDevice = 32
    Controller = 64
    TrackingReference = 128
    Left = 256
    Right = 512
    Simulated6DOF = 1024

# UnityEngine.XR.InputFeatureType
class InputFeatureType(IntFlag):
    Custom = 0
    Binary = 1
    DiscreteStates = 2
    Axis1D = 3
    Axis2D = 4
    Axis3D = 5
    Rotation = 6
    Hand = 7
    Bone = 8
    Eyes = 9
    kUnityXRInputFeatureTypeInvalid = 4294967295

# UnityEngine.XR.InputTracking
class InputTracking(IntFlag):
    NodeAdded = 0
    NodeRemoved = 1
    TrackingAcquired = 2
    TrackingLost = 3

# UnityEngine.XR.InputTrackingState
class InputTrackingState(IntFlag):
    NONE = 0
    Position = 1
    Rotation = 2
    Velocity = 4
    AngularVelocity = 8
    Acceleration = 16
    AngularAcceleration = 32
    All = 63

# UnityEngine.XR.MeshGenerationStatus
class MeshGenerationStatus(IntFlag):
    Success = 0
    InvalidMeshId = 1
    GenerationAlreadyInProgress = 2
    Canceled = 3
    UnknownError = 4

# UnityEngine.XR.MeshVertexAttributes
class MeshVertexAttributes(IntFlag):
    NONE = 0
    Normals = 1
    Tangents = 2
    UVs = 4
    Colors = 8

# UnityEngine.XR.XRDisplaySubsystem
class XRDisplaySubsystem(IntFlag):
    Texture2DArray = 1
    SingleTexture2D = 2
    SeparateTexture2Ds = 4

# UnityEngine.XR.XRNode
class XRNode(IntFlag):
    LeftEye = 0
    RightEye = 1
    CenterEye = 2
    Head = 3
    LeftHand = 4
    RightHand = 5
    GameController = 6
    TrackingReference = 7
    HardwareTracker = 8

