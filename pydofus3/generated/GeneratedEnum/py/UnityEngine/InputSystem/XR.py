from enum import IntFlag

# UnityEngine.InputSystem.XR.FeatureType
class FeatureType(IntFlag):
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

# UnityEngine.InputSystem.XR.TrackedPoseDriver
class TrackedPoseDriver(IntFlag):
    RotationAndPosition = 0
    RotationOnly = 1
    PositionOnly = 2

# UnityEngine.InputSystem.XR.TrackedPoseDriver
class TrackedPoseDriver(IntFlag):
    NONE = 0
    Position = 1
    Rotation = 2

# UnityEngine.InputSystem.XR.TrackedPoseDriver
class TrackedPoseDriver(IntFlag):
    UpdateAndBeforeRender = 0
    Update = 1
    BeforeRender = 2

