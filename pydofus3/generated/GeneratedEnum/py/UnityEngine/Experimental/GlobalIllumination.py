from enum import IntFlag

# UnityEngine.Experimental.GlobalIllumination.AngularFalloffType
class AngularFalloffType(IntFlag):
    LUT = 0
    AnalyticAndInnerAngle = 1

# UnityEngine.Experimental.GlobalIllumination.FalloffType
class FalloffType(IntFlag):
    InverseSquared = 0
    InverseSquaredNoRangeAttenuation = 1
    Linear = 2
    Legacy = 3
    Undefined = 4

# UnityEngine.Experimental.GlobalIllumination.LightMode
class LightMode(IntFlag):
    Realtime = 0
    Mixed = 1
    Baked = 2
    Unknown = 3

# UnityEngine.Experimental.GlobalIllumination.LightType
class LightType(IntFlag):
    Directional = 0
    Point = 1
    Spot = 2
    Rectangle = 3
    Disc = 4
    SpotPyramidShape = 5
    SpotBoxShape = 6

