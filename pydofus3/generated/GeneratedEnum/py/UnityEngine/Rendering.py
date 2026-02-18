from enum import IntFlag

# UnityEngine.Rendering.APVConstantBufferRegister
class APVConstantBufferRegister(IntFlag):
    GlobalRegister = 6

# UnityEngine.Rendering.APVLeakReductionMode
class APVLeakReductionMode(IntFlag):
    NONE = 0
    Performance = 1
    Quality = 2
    ValidityBased = 1
    ValidityAndNormalBased = 2

# UnityEngine.Rendering.AdvancedUpscalers
class AdvancedUpscalers(IntFlag):
    DLSS = 0
    FSR2 = 1
    STP = 2

# UnityEngine.Rendering.BatchBufferTarget
class BatchBufferTarget(IntFlag):
    Unknown = 0
    UnsupportedByUnderlyingGraphicsApi = -1
    RawBuffer = 1
    ConstantBuffer = 2

# UnityEngine.Rendering.BatchCullingFlags
class BatchCullingFlags(IntFlag):
    NONE = 0
    CullLightmappedShadowCasters = 1

# UnityEngine.Rendering.BatchCullingProjectionType
class BatchCullingProjectionType(IntFlag):
    Unknown = 0
    Perspective = 1
    Orthographic = 2

# UnityEngine.Rendering.BatchCullingViewType
class BatchCullingViewType(IntFlag):
    Unknown = 0
    Camera = 1
    Light = 2
    Picking = 3
    SelectionOutline = 4
    Filtering = 5

# UnityEngine.Rendering.BatchDrawCommandFlags
class BatchDrawCommandFlags(IntFlag):
    NONE = 0
    FlipWinding = 1
    HasMotion = 2
    IsLightMapped = 4
    HasSortingPosition = 8
    LODCrossFadeKeyword = 16
    LODCrossFadeValuePacked = 32
    LODCrossFade = 48
    UseLegacyLightmapsKeyword = 64

# UnityEngine.Rendering.BatchDrawCommandType
class BatchDrawCommandType(IntFlag):
    Direct = 0
    Indirect = 1
    Procedural = 2
    ProceduralIndirect = 3

# UnityEngine.Rendering.BlendMode
class BlendMode(IntFlag):
    Zero = 0
    One = 1
    DstColor = 2
    SrcColor = 3
    OneMinusDstColor = 4
    SrcAlpha = 5
    OneMinusSrcColor = 6
    DstAlpha = 7
    OneMinusDstAlpha = 8
    SrcAlphaSaturate = 9
    OneMinusSrcAlpha = 10

# UnityEngine.Rendering.BlendOp
class BlendOp(IntFlag):
    Add = 0
    Subtract = 1
    ReverseSubtract = 2
    Min = 3
    Max = 4
    LogicalClear = 5
    LogicalSet = 6
    LogicalCopy = 7
    LogicalCopyInverted = 8
    LogicalNoop = 9
    LogicalInvert = 10
    LogicalAnd = 11
    LogicalNand = 12
    LogicalOr = 13
    LogicalNor = 14
    LogicalXor = 15
    LogicalEquivalence = 16
    LogicalAndReverse = 17
    LogicalAndInverted = 18
    LogicalOrReverse = 19
    LogicalOrInverted = 20
    Multiply = 21
    Screen = 22
    Overlay = 23
    Darken = 24
    Lighten = 25
    ColorDodge = 26
    ColorBurn = 27
    HardLight = 28
    SoftLight = 29
    Difference = 30
    Exclusion = 31
    HSLHue = 32
    HSLSaturation = 33
    HSLColor = 34
    HSLLuminosity = 35

# UnityEngine.Rendering.Blitter
class Blitter(IntFlag):
    Nearest = 0
    Bilinear = 1
    NearestQuad = 2
    BilinearQuad = 3
    NearestQuadPadding = 4
    BilinearQuadPadding = 5
    NearestQuadPaddingRepeat = 6
    BilinearQuadPaddingRepeat = 7
    BilinearQuadPaddingOctahedral = 8
    NearestQuadPaddingAlphaBlend = 9
    BilinearQuadPaddingAlphaBlend = 10
    NearestQuadPaddingAlphaBlendRepeat = 11
    BilinearQuadPaddingAlphaBlendRepeat = 12
    BilinearQuadPaddingAlphaBlendOctahedral = 13
    CubeToOctahedral = 14
    CubeToOctahedralLuminance = 15
    CubeToOctahedralAlpha = 16
    CubeToOctahedralRed = 17
    BilinearQuadLuminance = 18
    BilinearQuadAlpha = 19
    BilinearQuadRed = 20
    NearestCubeToOctahedralPadding = 21
    BilinearCubeToOctahedralPadding = 22

# UnityEngine.Rendering.Blitter
class Blitter(IntFlag):
    ColorOnly = 0
    ColorAndDepth = 1

# UnityEngine.Rendering.BoolParameter
class BoolParameter(IntFlag):
    Checkbox = 0
    EnumPopup = 1

# UnityEngine.Rendering.BuiltinRenderTextureType
class BuiltinRenderTextureType(IntFlag):
    PropertyName = -4
    BufferPtr = -3
    RenderTexture = -2
    BindableTexture = -1
    NONE = 0
    CurrentActive = 1
    CameraTarget = 2
    Depth = 3
    DepthNormals = 4
    ResolvedDepth = 5
    PrepassNormalsSpec = 7
    PrepassLight = 8
    PrepassLightSpec = 9
    GBuffer0 = 10
    GBuffer1 = 11
    GBuffer2 = 12
    GBuffer3 = 13
    Reflections = 14
    MotionVectors = 15
    GBuffer4 = 16
    GBuffer5 = 17
    GBuffer6 = 18
    GBuffer7 = 19

# UnityEngine.Rendering.BuiltinShaderDefine
class BuiltinShaderDefine(IntFlag):
    UNITY_NO_DXT5nm = 0
    UNITY_NO_RGBM = 1
    UNITY_USE_NATIVE_HDR = 2
    UNITY_ENABLE_REFLECTION_BUFFERS = 3
    UNITY_FRAMEBUFFER_FETCH_AVAILABLE = 4
    UNITY_ENABLE_NATIVE_SHADOW_LOOKUPS = 5
    UNITY_METAL_SHADOWS_USE_POINT_FILTERING = 6
    UNITY_NO_CUBEMAP_ARRAY = 7
    UNITY_NO_SCREENSPACE_SHADOWS = 8
    UNITY_USE_DITHER_MASK_FOR_ALPHABLENDED_SHADOWS = 9
    UNITY_PBS_USE_BRDF1 = 10
    UNITY_PBS_USE_BRDF2 = 11
    UNITY_PBS_USE_BRDF3 = 12
    UNITY_NO_FULL_STANDARD_SHADER = 13
    UNITY_SPECCUBE_BOX_PROJECTION = 14
    UNITY_SPECCUBE_BLENDING = 15
    UNITY_ENABLE_DETAIL_NORMALMAP = 16
    SHADER_API_MOBILE = 17
    SHADER_API_DESKTOP = 18
    UNITY_HARDWARE_TIER1 = 19
    UNITY_HARDWARE_TIER2 = 20
    UNITY_HARDWARE_TIER3 = 21
    UNITY_COLORSPACE_GAMMA = 22
    UNITY_LIGHT_PROBE_PROXY_VOLUME = 23
    UNITY_HALF_PRECISION_FRAGMENT_SHADER_REGISTERS = 24
    UNITY_LIGHTMAP_DLDR_ENCODING = 25
    UNITY_LIGHTMAP_RGBM_ENCODING = 26
    UNITY_LIGHTMAP_FULL_HDR = 27
    UNITY_VIRTUAL_TEXTURING = 28
    UNITY_PRETRANSFORM_TO_DISPLAY_ORIENTATION = 29
    UNITY_ASTC_NORMALMAP_ENCODING = 30
    SHADER_API_GLES30 = 31
    UNITY_UNIFIED_SHADER_PRECISION_MODEL = 32
    UNITY_PLATFORM_SUPPORTS_WAVE_32 = 33
    UNITY_PLATFORM_SUPPORTS_WAVE_64 = 34
    UNITY_NEEDS_RENDERPASS_FBFETCH_FALLBACK = 35
    UNITY_PLATFORM_SUPPORTS_DEPTH_FETCH = 36

# UnityEngine.Rendering.CameraEvent
class CameraEvent(IntFlag):
    BeforeDepthTexture = 0
    AfterDepthTexture = 1
    BeforeDepthNormalsTexture = 2
    AfterDepthNormalsTexture = 3
    BeforeGBuffer = 4
    AfterGBuffer = 5
    BeforeLighting = 6
    AfterLighting = 7
    BeforeFinalPass = 8
    AfterFinalPass = 9
    BeforeForwardOpaque = 10
    AfterForwardOpaque = 11
    BeforeImageEffectsOpaque = 12
    AfterImageEffectsOpaque = 13
    BeforeSkybox = 14
    AfterSkybox = 15
    BeforeForwardAlpha = 16
    AfterForwardAlpha = 17
    BeforeImageEffects = 18
    AfterImageEffects = 19
    AfterEverything = 20
    BeforeReflections = 21
    AfterReflections = 22
    BeforeHaloAndLensFlares = 23
    AfterHaloAndLensFlares = 24

# UnityEngine.Rendering.CameraLateLatchMatrixType
class CameraLateLatchMatrixType(IntFlag):
    View = 0
    InverseView = 1
    ViewProjection = 2
    InverseViewProjection = 3

# UnityEngine.Rendering.ClearFlag
class ClearFlag(IntFlag):
    NONE = 0
    Color = 1
    Depth = 2
    Stencil = 4
    DepthStencil = 6
    ColorStencil = 5
    All = 7

# UnityEngine.Rendering.ColorWriteMask
class ColorWriteMask(IntFlag):
    Alpha = 1
    Blue = 2
    Green = 4
    Red = 8
    All = 15

# UnityEngine.Rendering.CommandBufferExecutionFlags
class CommandBufferExecutionFlags(IntFlag):
    NONE = 0
    AsyncCompute = 2

# UnityEngine.Rendering.CompareFunction
class CompareFunction(IntFlag):
    Disabled = 0
    Never = 1
    Less = 2
    Equal = 3
    LessEqual = 4
    Greater = 5
    NotEqual = 6
    GreaterEqual = 7
    Always = 8

# UnityEngine.Rendering.ComputeQueueType
class ComputeQueueType(IntFlag):
    Default = 0
    Background = 1
    Urgent = 2

# UnityEngine.Rendering.CopyTextureSupport
class CopyTextureSupport(IntFlag):
    NONE = 0
    Basic = 1
    Copy3D = 2
    DifferentTypes = 4
    TextureToRT = 8
    RTToTexture = 16

# UnityEngine.Rendering.CoreProfileId
class CoreProfileId(IntFlag):
    BlitTextureInPotAtlas = 0
    APVCellStreamingUpdate = 1
    APVScenarioBlendingUpdate = 2
    APVIndexDefragUpdate = 3
    APVDiskStreamingUpdate = 4
    APVDiskStreamingUpdatePool = 5
    APVSamplingDebug = 6

# UnityEngine.Rendering.CullMode
class CullMode(IntFlag):
    Off = 0
    Front = 1
    Back = 2

# UnityEngine.Rendering.CullingJob
class CullingJob(IntFlag):
    kDisabled = 0
    kCrossFadeOut = 1
    kCrossFadeIn = 2
    kVisible = 3

# UnityEngine.Rendering.CullingOptions
class CullingOptions(IntFlag):
    NONE = 0
    ForceEvenIfCameraIsNotActive = 1
    OcclusionCull = 2
    NeedsLighting = 4
    NeedsReflectionProbes = 8
    Stereo = 16
    DisablePerObjectCulling = 32
    ShadowCasters = 64

# UnityEngine.Rendering.DebugAction
class DebugAction(IntFlag):
    EnableDebugMenu = 0
    PreviousDebugPanel = 1
    NextDebugPanel = 2
    Action = 3
    MakePersistent = 4
    MoveVertical = 5
    MoveHorizontal = 6
    Multiplier = 7
    ResetAll = 8
    DebugActionCount = 9

# UnityEngine.Rendering.DebugActionRepeatMode
class DebugActionRepeatMode(IntFlag):
    Never = 0
    Delay = 1

# UnityEngine.Rendering.DebugActionState
class DebugActionState(IntFlag):
    Button = 0
    Axis = 1
    Key = 2

# UnityEngine.Rendering.DebugDisplayStats
class DebugDisplayStats(IntFlag):
    CPU = 0
    InlineCPU = 1
    GPU = 2

# UnityEngine.Rendering.DebugManager
class DebugManager(IntFlag):
    EditorMode = 0
    RuntimeMode = 1

# UnityEngine.Rendering.DebugProbeShadingMode
class DebugProbeShadingMode(IntFlag):
    SH = 0
    SHL0 = 1
    SHL0L1 = 2
    Validity = 3
    ValidityOverDilationThreshold = 4
    RenderingLayerMasks = 5
    InvalidatedByAdjustmentVolumes = 6
    Size = 7
    SkyOcclusionSH = 8
    SkyDirection = 9
    ProbeOcclusion = 10

# UnityEngine.Rendering.DebugUI
class DebugUI(IntFlag):
    NONE = 0
    EditorOnly = 2
    RuntimeOnly = 4
    EditorForceUpdate = 8
    FrequentlyUsed = 16

# UnityEngine.Rendering.DebugUI
class DebugUI(IntFlag):
    Info = 0
    Warning = 1
    Error = 2

# UnityEngine.Rendering.DefaultMaterialType
class DefaultMaterialType(IntFlag):
    Default = 0
    Particle = 1
    Line = 2
    Terrain = 3
    Sprite = 4
    SpriteMask = 5
    UGUI = 6
    UGUI_Overdraw = 7
    UGUI_ETC1Supported = 8

# UnityEngine.Rendering.DefaultShaderType
class DefaultShaderType(IntFlag):
    Default = 0
    AutodeskInteractive = 1
    AutodeskInteractiveTransparent = 2
    AutodeskInteractiveMasked = 3
    TerrainDetailLit = 4
    TerrainDetailGrass = 5
    TerrainDetailGrassBillboard = 6
    SpeedTree7 = 7
    SpeedTree8 = 8
    SpeedTree9 = 9

# UnityEngine.Rendering.DepthBits
class DepthBits(IntFlag):
    NONE = 0
    Depth8 = 8
    Depth16 = 16
    Depth24 = 24
    Depth32 = 32

# UnityEngine.Rendering.DistanceMetric
class DistanceMetric(IntFlag):
    Perspective = 0
    Orthographic = 1
    CustomAxis = 2

# UnityEngine.Rendering.DrawRendererFlags
class DrawRendererFlags(IntFlag):
    NONE = 0
    EnableDynamicBatching = 1
    EnableInstancing = 2

# UnityEngine.Rendering.DynamicResScalePolicyType
class DynamicResScalePolicyType(IntFlag):
    ReturnsPercentage = 0
    ReturnsMinMaxLerpFactor = 1

# UnityEngine.Rendering.DynamicResScalerSlot
class DynamicResScalerSlot(IntFlag):
    User = 0
    System = 1
    Count = 2

# UnityEngine.Rendering.DynamicResUpscaleFilter
class DynamicResUpscaleFilter(IntFlag):
    Bilinear = 0
    CatmullRom = 1
    Lanczos = 2
    ContrastAdaptiveSharpen = 3
    EdgeAdaptiveScalingUpres = 4
    TAAU = 5

# UnityEngine.Rendering.DynamicResolutionHandler
class DynamicResolutionHandler(IntFlag):
    BeforePost = 0
    AfterDepthOfField = 1
    AfterPost = 2

# UnityEngine.Rendering.DynamicResolutionType
class DynamicResolutionType(IntFlag):
    Software = 0
    Hardware = 1

# UnityEngine.Rendering.FastMemoryFlags
class FastMemoryFlags(IntFlag):
    NONE = 0
    SpillTop = 1
    SpillBottom = 2

# UnityEngine.Rendering.FieldPacking
class FieldPacking(IntFlag):
    NoPacking = 0
    R11G11B10 = 1
    PackedFloat = 2
    PackedUint = 3

# UnityEngine.Rendering.FieldPrecision
class FieldPrecision(IntFlag):
    Half = 0
    Real = 1
    Default = 2

# UnityEngine.Rendering.FormatSwizzle
class FormatSwizzle(IntFlag):
    FormatSwizzleR = 0
    FormatSwizzleG = 1
    FormatSwizzleB = 2
    FormatSwizzleA = 3
    FormatSwizzle0 = 4
    FormatSwizzle1 = 5

# UnityEngine.Rendering.FoveatedRenderingCaps
class FoveatedRenderingCaps(IntFlag):
    NONE = 0
    FoveationImage = 1
    NonUniformRaster = 2
    ModeChangeOnlyBeforeRenderTargetSet = 4

# UnityEngine.Rendering.FoveatedRenderingMode
class FoveatedRenderingMode(IntFlag):
    Disabled = 0
    Enabled = 1

# UnityEngine.Rendering.GPUResidentDrawerMode
class GPUResidentDrawerMode(IntFlag):
    Disabled = 0
    InstancedDrawing = 1

# UnityEngine.Rendering.GPUResidentDrawerResources
class GPUResidentDrawerResources(IntFlag):
    Initial = 0
    Count = 1
    Latest = 0

# UnityEngine.Rendering.GPUSort
class GPUSort(IntFlag):
    LocalBMS = 0
    LocalDisperse = 1
    BigFlip = 2
    BigDisperse = 3

# UnityEngine.Rendering.GizmoSubset
class GizmoSubset(IntFlag):
    PreImageEffects = 0
    PostImageEffects = 1

# UnityEngine.Rendering.GraphicsDeviceType
class GraphicsDeviceType(IntFlag):
    OpenGL2 = 0
    Direct3D9 = 1
    Direct3D11 = 2
    PlayStation3 = 3
    Null = 4
    Xbox360 = 6
    OpenGLES2 = 8
    OpenGLES3 = 11
    PlayStationVita = 12
    PlayStation4 = 13
    XboxOne = 14
    PlayStationMobile = 15
    Metal = 16
    OpenGLCore = 17
    Direct3D12 = 18
    N3DS = 19
    Vulkan = 21
    Switch = 22
    XboxOneD3D12 = 23
    GameCoreXboxOne = 24
    GameCoreScarlett = -1
    GameCoreXboxSeries = 25
    PlayStation5 = 26
    PlayStation5NGGC = 27
    WebGPU = 28
    ReservedCFE = 29

# UnityEngine.Rendering.GraphicsFenceType
class GraphicsFenceType(IntFlag):
    AsyncQueueSynchronisation = 0
    CPUSynchronisation = 1

# UnityEngine.Rendering.GraphicsTier
class GraphicsTier(IntFlag):
    Tier1 = 0
    Tier2 = 1
    Tier3 = 2

# UnityEngine.Rendering.HDRColorspace
class HDRColorspace(IntFlag):
    Rec709 = 0
    Rec2020 = 1
    P3D65 = 2

# UnityEngine.Rendering.HDREncoding
class HDREncoding(IntFlag):
    Linear = 3
    PQ = 2
    Gamma22 = 4
    sRGB = 0

# UnityEngine.Rendering.HDROutputUtils
class HDROutputUtils(IntFlag):
    NONE = 0
    ColorConversion = 1
    ColorEncoding = 2

# UnityEngine.Rendering.HDRRangeReduction
class HDRRangeReduction(IntFlag):
    NONE = 0
    Reinhard = 1
    BT2390 = 2
    ACES1000Nits = 3
    ACES2000Nits = 4
    ACES4000Nits = 5

# UnityEngine.Rendering.IncludeAdditionalRPAssets
class IncludeAdditionalRPAssets(IntFlag):
    Initial = 0
    Count = 1
    Last = 0

# UnityEngine.Rendering.IndexFormat
class IndexFormat(IntFlag):
    UInt16 = 0
    UInt32 = 1

# UnityEngine.Rendering.IndirectAllocator
class IndirectAllocator(IntFlag):
    NextInstanceIndex = 0
    NextDrawIndex = 1
    Count = 2

# UnityEngine.Rendering.IndirectBufferContext
class IndirectBufferContext(IntFlag):
    Pending = 0
    Zeroed = 1
    NoOcclusionTest = 2
    AllInstancesOcclusionTested = 3
    OccludedInstancesReTested = 4

# UnityEngine.Rendering.InstanceComponentGroup
class InstanceComponentGroup(IntFlag):
    Default = 1
    Wind = 2
    LightProbe = 4
    Lightmap = 8
    DefaultWind = 3
    DefaultLightProbe = 5
    DefaultLightmap = 9
    DefaultWindLightProbe = 7
    DefaultWindLightmap = 11

# UnityEngine.Rendering.InstanceCullerSplitDebugCounter
class InstanceCullerSplitDebugCounter(IntFlag):
    VisibleInstances = 0
    VisiblePrimitives = 1
    DrawCommands = 2
    Count = 3

# UnityEngine.Rendering.InstanceFlags
class InstanceFlags(IntFlag):
    NONE = 0
    AffectsLightmaps = 1
    IsShadowsOff = 2
    IsShadowsOnly = 4
    HasProgressiveLod = 8
    SmallMeshCulling = 16

# UnityEngine.Rendering.InstanceOcclusionEventType
class InstanceOcclusionEventType(IntFlag):
    OcclusionTest = 0
    OccluderUpdate = 1

# UnityEngine.Rendering.InstanceOcclusionTestDebugCounter
class InstanceOcclusionTestDebugCounter(IntFlag):
    InstancesOccluded = 0
    InstancesNotOccluded = 1
    PrimitivesOccluded = 2
    PrimitivesNotOccluded = 3
    Count = 4

# UnityEngine.Rendering.InstanceType
class InstanceType(IntFlag):
    MeshRenderer = 0
    SpeedTree = 1
    Count = 2
    LODGroup = 0

# UnityEngine.Rendering.LensFlareComponentSRP
class LensFlareComponentSRP(IntFlag):
    Initial = 0

# UnityEngine.Rendering.LensFlareOcclusionPermutation
class LensFlareOcclusionPermutation(IntFlag):
    Depth = 1
    FogOpacity = 4

# UnityEngine.Rendering.LightProbeUsage
class LightProbeUsage(IntFlag):
    Off = 0
    BlendProbes = 1
    UseProxyVolume = 2
    CustomProvided = 4

# UnityEngine.Rendering.LightShadowResolution
class LightShadowResolution(IntFlag):
    FromQualitySettings = -1
    Low = 0
    Medium = 1
    High = 2
    VeryHigh = 3

# UnityEngine.Rendering.LightUnit
class LightUnit(IntFlag):
    Lumen = 0
    Candela = 1
    Lux = 2
    Nits = 3
    Ev100 = 4

# UnityEngine.Rendering.MSAASamples
class MSAASamples(IntFlag):
    NONE = 1
    MSAA2x = 2
    MSAA4x = 4
    MSAA8x = 8

# UnityEngine.Rendering.MaterialQuality
class MaterialQuality(IntFlag):
    Low = 1
    Medium = 2
    High = 4

# UnityEngine.Rendering.MeshUpdateFlags
class MeshUpdateFlags(IntFlag):
    Default = 0
    DontValidateIndices = 1
    DontResetBoneBounds = 2
    DontNotifyMeshUsers = 4
    DontRecalculateBounds = 8

# UnityEngine.Rendering.OcclusionCullingCommonConfig
class OcclusionCullingCommonConfig(IntFlag):
    MaxOccluderMips = 8
    MaxOccluderSilhouettePlanes = 6
    MaxSubviewsPerView = 6
    DebugPyramidOffset = 4

# UnityEngine.Rendering.OcclusionTest
class OcclusionTest(IntFlag):
    NONE = 0
    TestAll = 1
    TestCulled = 2

# UnityEngine.Rendering.OcclusionTestDebugFlag
class OcclusionTestDebugFlag(IntFlag):
    AlwaysPass = 1
    CountVisible = 2

# UnityEngine.Rendering.OpaqueSortMode
class OpaqueSortMode(IntFlag):
    Default = 0
    FrontToBack = 1
    NoDistanceSort = 2

# UnityEngine.Rendering.OpenGLESVersion
class OpenGLESVersion(IntFlag):
    NONE = 0
    OpenGLES20 = 1
    OpenGLES30 = 2
    OpenGLES31 = 3
    OpenGLES31AEP = 4
    OpenGLES32 = 5

# UnityEngine.Rendering.PackingRules
class PackingRules(IntFlag):
    Exact = 0
    Aggressive = 1

# UnityEngine.Rendering.PerObjectData
class PerObjectData(IntFlag):
    NONE = 0
    LightProbe = 1
    ReflectionProbes = 2
    LightProbeProxyVolume = 4
    Lightmaps = 8
    LightData = 16
    MotionVectors = 32
    LightIndices = 64
    ReflectionProbeData = 128
    OcclusionProbe = 256
    OcclusionProbeProxyVolume = 512
    ShadowMask = 1024

# UnityEngine.Rendering.PerformanceBottleneck
class PerformanceBottleneck(IntFlag):
    Indeterminate = 0
    PresentLimited = 1
    CPU = 2
    GPU = 3
    Balanced = 4

# UnityEngine.Rendering.PowerOfTwoTextureAtlas
class PowerOfTwoTextureAtlas(IntFlag):
    Padding = 0
    PaddingMultiply = 1
    OctahedralPadding = 2
    OctahedralPaddingMultiply = 3

# UnityEngine.Rendering.ProbeAdjustmentVolume
class ProbeAdjustmentVolume(IntFlag):
    Box = 0
    Sphere = 1

# UnityEngine.Rendering.ProbeAdjustmentVolume
class ProbeAdjustmentVolume(IntFlag):
    InvalidateProbes = 0
    OverrideValidityThreshold = 1
    ApplyVirtualOffset = 2
    OverrideVirtualOffsetSettings = 3
    OverrideSkyDirection = 4
    OverrideSampleCount = 5
    OverrideRenderingLayerMask = 6
    IntensityScale = 99

# UnityEngine.Rendering.ProbeAdjustmentVolume
class ProbeAdjustmentVolume(IntFlag):
    Override = 0
    Add = 1
    Remove = 2

# UnityEngine.Rendering.ProbeAdjustmentVolume
class ProbeAdjustmentVolume(IntFlag):
    Initial = 0
    Mode = 1
    Count = 2

# UnityEngine.Rendering.ProbeReferenceVolume
class ProbeReferenceVolume(IntFlag):
    Pending = 0
    Active = 1
    Canceled = 2
    Invalid = 3
    Complete = 4

# UnityEngine.Rendering.ProbeSamplingDebugUpdate
class ProbeSamplingDebugUpdate(IntFlag):
    Never = 0
    Once = 1
    Always = 2

# UnityEngine.Rendering.ProbeVolume
class ProbeVolume(IntFlag):
    Global = 0
    Scene = 1
    Local = 2

# UnityEngine.Rendering.ProbeVolume
class ProbeVolume(IntFlag):
    Initial = 0
    LocalMode = 1
    InvertOverrideLevels = 2
    Count = 3

# UnityEngine.Rendering.ProbeVolumeBakingProcessSettings
class ProbeVolumeBakingProcessSettings(IntFlag):
    Initial = 0
    ThreadedVirtualOffset = 1
    Max = 2
    Current = 1

# UnityEngine.Rendering.ProbeVolumeBakingSet
class ProbeVolumeBakingSet(IntFlag):
    Initial = 0
    RemoveProbeVolumeSceneData = 1
    AssetsAlwaysReferenced = 2

# UnityEngine.Rendering.ProbeVolumeBlendingTextureMemoryBudget
class ProbeVolumeBlendingTextureMemoryBudget(IntFlag):
    MemoryBudgetLow = 128
    MemoryBudgetMedium = 256
    MemoryBudgetHigh = 512

# UnityEngine.Rendering.ProbeVolumeSHBands
class ProbeVolumeSHBands(IntFlag):
    SphericalHarmonicsL1 = 1
    SphericalHarmonicsL2 = 2

# UnityEngine.Rendering.ProbeVolumeTextureMemoryBudget
class ProbeVolumeTextureMemoryBudget(IntFlag):
    MemoryBudgetLow = 512
    MemoryBudgetMedium = 1024
    MemoryBudgetHigh = 2048

# UnityEngine.Rendering.RTClearFlags
class RTClearFlags(IntFlag):
    NONE = 0
    Color = 1
    Depth = 2
    Stencil = 4
    All = 7
    DepthStencil = 6
    ColorDepth = 3
    ColorStencil = 5

# UnityEngine.Rendering.RTHandleSystem
class RTHandleSystem(IntFlag):
    Auto = 0
    OnDemand = 1

# UnityEngine.Rendering.RayTracingAccelerationStructureBuildFlags
class RayTracingAccelerationStructureBuildFlags(IntFlag):
    NONE = 0
    PreferFastTrace = 1
    PreferFastBuild = 2
    MinimizeMemory = 4

# UnityEngine.Rendering.ReflectionProbeRefreshMode
class ReflectionProbeRefreshMode(IntFlag):
    OnAwake = 0
    EveryFrame = 1
    ViaScripting = 2

# UnityEngine.Rendering.ReflectionProbeSortingCriteria
class ReflectionProbeSortingCriteria(IntFlag):
    NONE = 0
    Importance = 1
    Size = 2
    ImportanceThenSize = 3

# UnityEngine.Rendering.ReflectionProbeUsage
class ReflectionProbeUsage(IntFlag):
    Off = 0
    BlendProbes = 1
    BlendProbesAndSkybox = 2
    Simple = 3

# UnityEngine.Rendering.ReloadAttribute
class ReloadAttribute(IntFlag):
    Builtin = 0
    Root = 1
    BuiltinExtra = 2

# UnityEngine.Rendering.RenderBufferLoadAction
class RenderBufferLoadAction(IntFlag):
    Load = 0
    Clear = 1
    DontCare = 2

# UnityEngine.Rendering.RenderBufferStoreAction
class RenderBufferStoreAction(IntFlag):
    Store = 0
    Resolve = 1
    StoreAndResolve = 2
    DontCare = 3

# UnityEngine.Rendering.RenderGraphGlobalSettings
class RenderGraphGlobalSettings(IntFlag):
    Initial = 0
    Count = 1
    Last = 0

# UnityEngine.Rendering.RenderStateMask
class RenderStateMask(IntFlag):
    Nothing = 0
    Blend = 1
    Raster = 2
    Depth = 4
    Stencil = 8
    Everything = 15

# UnityEngine.Rendering.RenderTargetFlags
class RenderTargetFlags(IntFlag):
    NONE = 0
    ReadOnlyDepth = 1
    ReadOnlyStencil = 2
    ReadOnlyDepthStencil = 3

# UnityEngine.Rendering.RenderTextureSubElement
class RenderTextureSubElement(IntFlag):
    Color = 0
    Depth = 1
    Stencil = 2
    Default = 3
    ShadingRate = 4

# UnityEngine.Rendering.RendererListStatus
class RendererListStatus(IntFlag):
    kRendererListInvalid = -2
    kRendererListProcessing = -1
    kRendererListEmpty = 0
    kRendererListPopulated = 1

# UnityEngine.Rendering.RenderersParameters
class RenderersParameters(IntFlag):
    NONE = 0
    UseBoundingSphereParameter = 1

# UnityEngine.Rendering.RenderingThreadingMode
class RenderingThreadingMode(IntFlag):
    Direct = 0
    SingleThreaded = 1
    MultiThreaded = 2
    LegacyJobified = 3
    NativeGraphicsJobs = 4
    NativeGraphicsJobsWithoutRenderThread = 5
    NativeGraphicsJobsSplitThreading = 6

# UnityEngine.Rendering.SRPLensFlareBlendMode
class SRPLensFlareBlendMode(IntFlag):
    Additive = 0
    Screen = 1
    Premultiply = 2
    Lerp = 3

# UnityEngine.Rendering.SRPLensFlareColorType
class SRPLensFlareColorType(IntFlag):
    Constant = 0
    RadialGradient = 1
    AngularGradient = 2

# UnityEngine.Rendering.SRPLensFlareDistribution
class SRPLensFlareDistribution(IntFlag):
    Uniform = 0
    Curve = 1
    Random = 2

# UnityEngine.Rendering.SRPLensFlareType
class SRPLensFlareType(IntFlag):
    Image = 0
    Circle = 1
    Polygon = 2
    Ring = 3
    LensFlareDataSRP = 4

# UnityEngine.Rendering.STP
class STP(IntFlag):
    DepthMotion = 0
    Luma = 1
    Convergence = 2
    Feedback = 3
    Count = 4

# UnityEngine.Rendering.STP
class STP(IntFlag):
    Count = 8

# UnityEngine.Rendering.STP
class STP(IntFlag):
    StpSetup = 0
    StpPreTaa = 1
    StpTaa = 2

# UnityEngine.Rendering.SearchType
class SearchType(IntFlag):
    ProjectPath = 0
    BuiltinPath = 1
    BuiltinExtraPath = 2
    ShaderName = 3

# UnityEngine.Rendering.ShaderDebugPrintManager
class ShaderDebugPrintManager(IntFlag):
    TypeUint = 1
    TypeInt = 2
    TypeFloat = 3
    TypeUint2 = 4
    TypeInt2 = 5
    TypeFloat2 = 6
    TypeUint3 = 7
    TypeInt3 = 8
    TypeFloat3 = 9
    TypeUint4 = 10
    TypeInt4 = 11
    TypeFloat4 = 12
    TypeBool = 13

# UnityEngine.Rendering.ShaderHardwareTier
class ShaderHardwareTier(IntFlag):
    Tier1 = 0
    Tier2 = 1
    Tier3 = 2

# UnityEngine.Rendering.ShaderPropertyFlags
class ShaderPropertyFlags(IntFlag):
    NONE = 0
    HideInInspector = 1
    PerRendererData = 2
    NoScaleOffset = 4
    Normal = 8
    HDR = 16
    Gamma = 32
    NonModifiableTextureData = 64
    MainTexture = 128
    MainColor = 256

# UnityEngine.Rendering.ShaderPropertyType
class ShaderPropertyType(IntFlag):
    Color = 0
    Vector = 1
    Float = 2
    Range = 3
    Texture = 4
    Int = 5

# UnityEngine.Rendering.ShaderStrippingSetting
class ShaderStrippingSetting(IntFlag):
    Initial = 0

# UnityEngine.Rendering.ShaderVariantLogLevel
class ShaderVariantLogLevel(IntFlag):
    Disabled = 0
    OnlySRPShaders = 1
    AllShaders = 2

# UnityEngine.Rendering.ShadingRateCombiner
class ShadingRateCombiner(IntFlag):
    Keep = 0
    Override = 1
    Min = 2
    Max = 3

# UnityEngine.Rendering.ShadingRateCombinerStage
class ShadingRateCombinerStage(IntFlag):
    Primitive = 0
    Fragment = 1

# UnityEngine.Rendering.ShadingRateFragmentSize
class ShadingRateFragmentSize(IntFlag):
    FragmentSize1x1 = 0
    FragmentSize1x2 = 1
    FragmentSize2x1 = 2
    FragmentSize2x2 = 3
    FragmentSize1x4 = 4
    FragmentSize4x1 = 5
    FragmentSize2x4 = 6
    FragmentSize4x2 = 7
    FragmentSize4x4 = 8

# UnityEngine.Rendering.ShadowCastingMode
class ShadowCastingMode(IntFlag):
    Off = 0
    On = 1
    TwoSided = 2
    ShadowsOnly = 3

# UnityEngine.Rendering.ShadowSamplingMode
class ShadowSamplingMode(IntFlag):
    CompareDepths = 0
    RawDepth = 1
    NONE = 2

# UnityEngine.Rendering.SinglePassStereoMode
class SinglePassStereoMode(IntFlag):
    NONE = 0
    SideBySide = 1
    Instancing = 2
    Multiview = 3

# UnityEngine.Rendering.SortingCriteria
class SortingCriteria(IntFlag):
    NONE = 0
    SortingLayer = 1
    RenderQueue = 2
    BackToFront = 4
    QuantizedFrontToBack = 8
    OptimizeStateChanges = 16
    CanvasOrder = 32
    RendererPriority = 64
    CommonOpaque = 59
    CommonTransparent = 23

# UnityEngine.Rendering.StencilOp
class StencilOp(IntFlag):
    Keep = 0
    Zero = 1
    Replace = 2
    IncrementSaturate = 3
    DecrementSaturate = 4
    Invert = 5
    IncrementWrap = 6
    DecrementWrap = 7

# UnityEngine.Rendering.SubPassFlags
class SubPassFlags(IntFlag):
    NONE = 0
    ReadOnlyDepth = 2
    ReadOnlyStencil = 4
    ReadOnlyDepthStencil = 6
    UseShadingRateImage = 8

# UnityEngine.Rendering.SupportedOnRenderPipelineAttribute
class SupportedOnRenderPipelineAttribute(IntFlag):
    Unsupported = 0
    Supported = 1
    SupportedByBaseClass = 2

# UnityEngine.Rendering.SupportedRenderingFeatures
class SupportedRenderingFeatures(IntFlag):
    NONE = 0
    Rotation = 1

# UnityEngine.Rendering.SupportedRenderingFeatures
class SupportedRenderingFeatures(IntFlag):
    NONE = 0
    IndirectOnly = 1
    Subtractive = 2
    Shadowmask = 4

# UnityEngine.Rendering.SynchronisationStage
class SynchronisationStage(IntFlag):
    VertexProcessing = 0
    PixelProcessing = 1

# UnityEngine.Rendering.SynchronisationStageFlags
class SynchronisationStageFlags(IntFlag):
    VertexProcessing = 1
    PixelProcessing = 2
    ComputeProcessing = 4
    AllGPUOperations = 7

# UnityEngine.Rendering.Texture2DAtlas
class Texture2DAtlas(IntFlag):
    Default = 0
    CubeTo2DOctahedral = 1
    SingleChannel = 2
    CubeTo2DOctahedralSingleChannel = 3

# UnityEngine.Rendering.TextureDimension
class TextureDimension(IntFlag):
    Unknown = -1
    NONE = 0
    Any = 1
    Tex2D = 2
    Tex3D = 3
    Cube = 4
    Tex2DArray = 5
    CubeArray = 6

# UnityEngine.Rendering.TransformUpdateFlags
class TransformUpdateFlags(IntFlag):
    NONE = 0
    HasLightProbeCombined = 1
    IsPartOfStaticBatch = 2

# UnityEngine.Rendering.UISubset
class UISubset(IntFlag):
    UIToolkit_UGUI = 1
    LowLevel = 2
    All = -1

# UnityEngine.Rendering.VertexAttribute
class VertexAttribute(IntFlag):
    Position = 0
    Normal = 1
    Tangent = 2
    Color = 3
    TexCoord0 = 4
    TexCoord1 = 5
    TexCoord2 = 6
    TexCoord3 = 7
    TexCoord4 = 8
    TexCoord5 = 9
    TexCoord6 = 10
    TexCoord7 = 11
    BlendWeight = 12
    BlendIndices = 13

# UnityEngine.Rendering.VertexAttributeFormat
class VertexAttributeFormat(IntFlag):
    Float32 = 0
    Float16 = 1
    UNorm8 = 2
    SNorm8 = 3
    UNorm16 = 4
    SNorm16 = 5
    UInt8 = 6
    SInt8 = 7
    UInt16 = 8
    SInt16 = 9
    UInt32 = 10
    SInt32 = 11

# UnityEngine.Rendering.VisibleLightFlags
class VisibleLightFlags(IntFlag):
    IntersectsNearPlane = 1
    IntersectsFarPlane = 2
    ForcedVisible = 4

# UnityEngine.Rendering.VolumeProfile
class VolumeProfile(IntFlag):
    NONE = 0
    DirtyByComponentChange = 1
    DirtyByProfileReset = 2
    Other = 4

