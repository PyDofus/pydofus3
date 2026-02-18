from enum import IntFlag

# UnityEngine.Rendering.Universal.Internal.DeferredLights
class DeferredLights(IntFlag):
    StencilVolume = 0
    PunctualLit = 1
    PunctualSimpleLit = 2
    DirectionalLit = 3
    DirectionalSimpleLit = 4
    Fog = 5
    SSAOOnly = 6

# UnityEngine.Rendering.Universal.Internal.DeferredLights
class DeferredLights(IntFlag):
    ClusteredLightsLit = 0
    ClusteredLightsSimpleLit = 1
    Fog = 2

# UnityEngine.Rendering.Universal.Internal.FinalBlitPass
class FinalBlitPass(IntFlag):
    Core = 0
    HDR = 1
    Count = 2

# UnityEngine.Rendering.Universal.Internal.LightFlag
class LightFlag(IntFlag):
    SubtractiveMixedLighting = 4

# UnityEngine.Rendering.Universal.Internal.StencilUsage
class StencilUsage(IntFlag):
    UserMask = 15
    StencilLight = 16
    MaterialMask = 96
    MaterialUnlit = 0
    MaterialLit = 32
    MaterialSimpleLit = 64

