from enum import IntFlag

# AleCore.Data.AleParticleSystemEmitFromBox
class AleParticleSystemEmitFromBox(IntFlag):
    Volume = 0
    Shell = 1
    Edge = 2

# AleCore.Data.AleParticleSystemEmitFromCone
class AleParticleSystemEmitFromCone(IntFlag):
    Base = 0
    Volume = 1

# AleCore.Data.AleParticleSystemSimulationSpace
class AleParticleSystemSimulationSpace(IntFlag):
    Local = 0
    World = 1
    Custom = 2

# AleCore.Data.AleParticleSystemSimulationSpaceRestricted
class AleParticleSystemSimulationSpaceRestricted(IntFlag):
    Local = 0
    World = 1
    Custom = 2

# AleCore.Data.AleParticleSystemSubEmitterProperties
class AleParticleSystemSubEmitterProperties(IntFlag):
    InheritNothing = 0
    InheritEverything = 31
    InheritColor = 1
    InheritSize = 2
    InheritRotation = 4
    InheritLifetime = 8
    InheritDuration = 16

# AleCore.Data.AleParticleSystemSubEmitterType
class AleParticleSystemSubEmitterType(IntFlag):
    Birth = 0
    Death = 1

# AleCore.Data.EffectShape
class EffectShape(IntFlag):
    Circle = 0
    Rectangle = 1

# AleCore.Data.EffectsSortingLayer
class EffectsSortingLayer(IntFlag):
    MapBackground = 0
    PaintBackground = 1
    BackEffect = 2
    IsometricBackground = 3
    BackgroundEffect = 4
    IsometricForeground = 5
    ForegroundEffect = 6
    PaintForeground = 7
    FrontEffect = 8
    Default = 9
    UI = 10

# AleCore.Data.ShaderAnimationCurveType
class ShaderAnimationCurveType(IntFlag):
    PingPong = 0
    Loop = 1
    Fixed = 2

# AleCore.Data.ShaderVariantBitfield
class ShaderVariantBitfield(IntFlag):
    NONE = 0
    CustomFramerate = 1
    AlphaClip = 2
    ColorAnimationFeature = 4
    ColorAnimationTypeFeatureFixed = 8
    ColorAnimationTypeFeaturePingPong = 16
    ColorAnimationTypeFeatureLoop = 32
    TranslationFeature = 64
    TranslationTypeFeatureFixed = 128
    TranslationTypeFeaturePingPong = 256
    TranslationTypeFeatureLoop = 512
    RotationFeature = 1024
    RotationTypeFeatureFixed = 2048
    RotationTypeFeaturePingPong = 4096
    RotationTypeFeatureLoop = 8192
    ScaleFeature = 16384
    ScaleTypeFeatureFixed = 32768
    ScaleTypeFeaturePingPong = 65536
    ScaleTypeFeatureLoop = 131072
    DistortionFeature = 262144
    DistortionUvModeFeatureScreenSpace = 524288
    DistortionUvModeFeatureWorldSpace = 1048576
    DistortionUvModeFeatureNormal = 2097152
    RefractionFeature = 8388608
    RefractionUvModeFeatureScreenSpace = 16777216
    RefractionUvModeFeatureWorldSpace = 33554432
    RefractionUvModeFeatureNormal = 67108864
    DissolveFeatureNo = 134217728
    DissolveFeatureNormal = 268435456
    DissolveFeatureParticle = 536870912
    DissolveAnimationTypeFixed = 1073741824
    DissolveAnimationTypePingPong = 2147483648
    DissolveAnimationTypeLoop = 4294967296
    EmissiveFeatureNo = 8589934592
    EmissiveFeatureNormal = 17179869184
    EmissiveFeatureParticle = 34359738368
    WindSensitiveFeature = 68719476736
    WindSensitiveFeatureManual = 137438953472
    WindSensitiveFeatureNoiseFixed = 274877906944
    WindSensitiveFeatureNoiseDynamic = 549755813888
    Animator2D = 1099511627776
    UseCustomisationColor = 2199023255552
    UseColorEffects = 4398046511104
    FlashBlendModeNone = 8796093022208
    FlashBlendModeMultiply = 17592186044416
    FlashBlendModeScreen = 35184372088832
    FlashBlendModeInvert = 70368744177664
    HighlightFeature = 140737488355328
    WindEnabled = 281474976710656
    EnableGlobalInline = 562949953421312
    EnableOverrideInline = 1125899906842624
    EnableGlobalOutline = 2251799813685248
    UseMapNoiseModifier = 4503599627370496
    WavesEnabled = 72057594037927936
    WaveSensitiveFeature = 144115188075855872

# AleCore.Data.UVModes
class UVModes(IntFlag):
    Normal = 0
    ScreenSpace = 1
    WorldSpace = 2

