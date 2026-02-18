from enum import IntFlag

# UnityEngine.Rendering.Universal.AdditionalLightsShadowAtlasLayout
class AdditionalLightsShadowAtlasLayout(IntFlag):
    NONE = 0
    SoftShadow = 1
    PointLightShadow = 2
    All = 65535

# UnityEngine.Rendering.Universal.AntialiasingMode
class AntialiasingMode(IntFlag):
    NONE = 0
    FastApproximateAntialiasing = 1
    SubpixelMorphologicalAntiAliasing = 2
    TemporalAntiAliasing = 3

# UnityEngine.Rendering.Universal.AntialiasingQuality
class AntialiasingQuality(IntFlag):
    Low = 0
    Medium = 1
    High = 2

# UnityEngine.Rendering.Universal.BloomDownscaleMode
class BloomDownscaleMode(IntFlag):
    Half = 0
    Quarter = 1

# UnityEngine.Rendering.Universal.CameraOverrideOption
class CameraOverrideOption(IntFlag):
    Off = 0
    On = 1
    UsePipelineSettings = 2

# UnityEngine.Rendering.Universal.CameraRenderType
class CameraRenderType(IntFlag):
    Base = 0
    Overlay = 1

# UnityEngine.Rendering.Universal.ColorGradingMode
class ColorGradingMode(IntFlag):
    LowDynamicRange = 0
    HighDynamicRange = 1

# UnityEngine.Rendering.Universal.CopyDepthMode
class CopyDepthMode(IntFlag):
    AfterOpaques = 0
    AfterTransparents = 1
    ForcePrepass = 2

# UnityEngine.Rendering.Universal.DebugDisplaySettingsMaterial
class DebugDisplaySettingsMaterial(IntFlag):
    DefaultLuminance = 0
    BlackAcrylicPaint = 1
    DarkSoil = 2
    WornAsphalt = 3
    DryClaySoil = 4
    GreenGrass = 5
    OldConcrete = 6
    RedClayTile = 7
    DrySand = 8
    NewConcrete = 9
    WhiteAcrylicPaint = 10
    FreshSnow = 11
    BlueSky = 12
    Foliage = 13
    Custom = 14

# UnityEngine.Rendering.Universal.DebugDisplaySettingsRendering
class DebugDisplaySettingsRendering(IntFlag):
    NONE = 0
    ShowRawFrame = 1
    ShowRawFrameNoJitter = 2
    ShowClampedHistory = 3

# UnityEngine.Rendering.Universal.DebugFullScreenMode
class DebugFullScreenMode(IntFlag):
    NONE = 0
    Depth = 1
    MotionVector = 2
    AdditionalLightsShadowMap = 3
    MainLightShadowMap = 4
    AdditionalLightsCookieAtlas = 5
    ReflectionProbeAtlas = 6
    STP = 7

# UnityEngine.Rendering.Universal.DebugLightingFeatureFlags
class DebugLightingFeatureFlags(IntFlag):
    NONE = 0
    GlobalIllumination = 1
    MainLight = 2
    AdditionalLights = 4
    VertexLighting = 8
    Emission = 16
    AmbientOcclusion = 32

# UnityEngine.Rendering.Universal.DebugLightingMode
class DebugLightingMode(IntFlag):
    NONE = 0
    ShadowCascades = 1
    LightingWithoutNormalMaps = 2
    LightingWithNormalMaps = 3
    Reflections = 4
    ReflectionsWithSmoothness = 5
    GlobalIllumination = 6

# UnityEngine.Rendering.Universal.DebugMaterialMode
class DebugMaterialMode(IntFlag):
    NONE = 0
    Albedo = 1
    Specular = 2
    Alpha = 3
    Smoothness = 4
    AmbientOcclusion = 5
    Emission = 6
    NormalWorldSpace = 7
    NormalTangentSpace = 8
    LightingComplexity = 9
    Metallic = 10
    SpriteMask = 11
    RenderingLayerMasks = 12

# UnityEngine.Rendering.Universal.DebugMaterialValidationMode
class DebugMaterialValidationMode(IntFlag):
    NONE = 0
    Albedo = 1
    Metallic = 2

# UnityEngine.Rendering.Universal.DebugMipInfoMode
class DebugMipInfoMode(IntFlag):
    NONE = 0
    MipStreamingPerformance = 1
    MipStreamingStatus = 2
    MipStreamingActivity = 3
    MipStreamingPriority = 4
    MipCount = 5
    MipRatio = 6

# UnityEngine.Rendering.Universal.DebugMipMapModeTerrainTexture
class DebugMipMapModeTerrainTexture(IntFlag):
    Control = 0
    Layer0 = 1
    Layer1 = 2
    Layer2 = 3
    Layer3 = 4

# UnityEngine.Rendering.Universal.DebugMipMapStatusMode
class DebugMipMapStatusMode(IntFlag):
    Material = 0
    Texture = 1

# UnityEngine.Rendering.Universal.DebugOverdrawMode
class DebugOverdrawMode(IntFlag):
    NONE = 0
    Opaque = 1
    Transparent = 2
    All = 3

# UnityEngine.Rendering.Universal.DebugPostProcessingMode
class DebugPostProcessingMode(IntFlag):
    Disabled = 0
    Auto = 1
    Enabled = 2

# UnityEngine.Rendering.Universal.DebugSceneOverrideMode
class DebugSceneOverrideMode(IntFlag):
    NONE = 0
    Overdraw = 1
    Wireframe = 2
    SolidWireframe = 3
    ShadedWireframe = 4

# UnityEngine.Rendering.Universal.DebugValidationMode
class DebugValidationMode(IntFlag):
    NONE = 0
    HighlightNanInfNegative = 1
    HighlightOutsideOfRange = 2

# UnityEngine.Rendering.Universal.DebugVertexAttributeMode
class DebugVertexAttributeMode(IntFlag):
    NONE = 0
    Texcoord0 = 1
    Texcoord1 = 2
    Texcoord2 = 3
    Texcoord3 = 4
    Color = 5
    Tangent = 6
    Normal = 7

# UnityEngine.Rendering.Universal.DebugWireframeMode
class DebugWireframeMode(IntFlag):
    NONE = 0
    Wireframe = 1
    SolidWireframe = 2
    ShadedWireframe = 3

# UnityEngine.Rendering.Universal.DecalNormalBlend
class DecalNormalBlend(IntFlag):
    Low = 0
    Medium = 1
    High = 2

# UnityEngine.Rendering.Universal.DecalScaleMode
class DecalScaleMode(IntFlag):
    ScaleInvariant = 0
    InheritFromHierarchy = 1

# UnityEngine.Rendering.Universal.DecalSurfaceData
class DecalSurfaceData(IntFlag):
    Albedo = 0
    AlbedoNormal = 1
    AlbedoNormalMAOS = 2

# UnityEngine.Rendering.Universal.DecalTechnique
class DecalTechnique(IntFlag):
    Invalid = 0
    DBuffer = 1
    ScreenSpace = 2
    GBuffer = 3

# UnityEngine.Rendering.Universal.DecalTechniqueOption
class DecalTechniqueOption(IntFlag):
    Automatic = 0
    DBuffer = 1
    ScreenSpace = 2

# UnityEngine.Rendering.Universal.DefaultMaterialType
class DefaultMaterialType(IntFlag):
    Default = 0
    Particle = 1
    Terrain = 2
    Sprite = 3
    SpriteMask = 4
    Decal = 5

# UnityEngine.Rendering.Universal.DepthFormat
class DepthFormat(IntFlag):
    Default = 0
    Depth_16 = 90
    Depth_24 = 91
    Depth_32 = 93
    Depth_16_Stencil_8 = 151
    Depth_24_Stencil_8 = 92
    Depth_32_Stencil_8 = 94

# UnityEngine.Rendering.Universal.DepthOfFieldMode
class DepthOfFieldMode(IntFlag):
    Off = 0
    Gaussian = 1
    Bokeh = 2

# UnityEngine.Rendering.Universal.DepthPrimingMode
class DepthPrimingMode(IntFlag):
    Disabled = 0
    Auto = 1
    Forced = 2

# UnityEngine.Rendering.Universal.Downsampling
class Downsampling(IntFlag):
    NONE = 0
    _2xBilinear = 1
    _4xBox = 2
    _4xBilinear = 3

# UnityEngine.Rendering.Universal.FilmGrainLookup
class FilmGrainLookup(IntFlag):
    Thin1 = 0
    Thin2 = 1
    Medium1 = 2
    Medium2 = 3
    Medium3 = 4
    Medium4 = 5
    Medium5 = 6
    Medium6 = 7
    Large01 = 8
    Large02 = 9
    Custom = 10

# UnityEngine.Rendering.Universal.FramebufferFetchEvent
class FramebufferFetchEvent(IntFlag):
    NONE = 0
    FetchGbufferInDeferred = 1

# UnityEngine.Rendering.Universal.FullScreenPassRendererFeature
class FullScreenPassRendererFeature(IntFlag):
    BeforeRenderingTransparents = 450
    BeforeRenderingPostProcessing = 550
    AfterRenderingPostProcessing = 600

# UnityEngine.Rendering.Universal.FullScreenPassRendererFeature
class FullScreenPassRendererFeature(IntFlag):
    Uninitialised = -1
    Initial = 0
    AddFetchColorBufferCheckbox = 1
    Count = 2
    Latest = 1

# UnityEngine.Rendering.Universal.HDRACESPreset
class HDRACESPreset(IntFlag):
    ACES1000Nits = 3
    ACES2000Nits = 4
    ACES4000Nits = 5

# UnityEngine.Rendering.Universal.HDRColorBufferPrecision
class HDRColorBufferPrecision(IntFlag):
    _32Bits = 0
    _64Bits = 1

# UnityEngine.Rendering.Universal.HDRDebugMode
class HDRDebugMode(IntFlag):
    NONE = 0
    GamutView = 1
    GamutClip = 2
    ValuesAbovePaperWhite = 3

# UnityEngine.Rendering.Universal.HDRDebugViewPass
class HDRDebugViewPass(IntFlag):
    CIExyPrepass = 0
    DebugViewPass = 1

# UnityEngine.Rendering.Universal.ImageScalingMode
class ImageScalingMode(IntFlag):
    NONE = 0
    Upscaling = 1
    Downscaling = 2

# UnityEngine.Rendering.Universal.ImageUpscalingFilter
class ImageUpscalingFilter(IntFlag):
    Linear = 0
    Point = 1
    FSR = 2
    STP = 3

# UnityEngine.Rendering.Universal.IntermediateTextureMode
class IntermediateTextureMode(IntFlag):
    Auto = 0
    Always = 1

# UnityEngine.Rendering.Universal.LODCrossFadeDitheringType
class LODCrossFadeDitheringType(IntFlag):
    BayerMatrix = 0
    BlueNoise = 1
    Stencil = 2

# UnityEngine.Rendering.Universal.LightCookieFormat
class LightCookieFormat(IntFlag):
    GrayscaleLow = 0
    GrayscaleHigh = 1
    ColorLow = 2
    ColorHigh = 3
    ColorHDR = 4

# UnityEngine.Rendering.Universal.LightCookieManager
class LightCookieManager(IntFlag):
    NONE = -1
    RGB = 0
    Alpha = 1
    Red = 2

# UnityEngine.Rendering.Universal.LightCookieResolution
class LightCookieResolution(IntFlag):
    _256 = 256
    _512 = 512
    _1024 = 1024
    _2048 = 2048
    _4096 = 4096

# UnityEngine.Rendering.Universal.LightLayerEnum
class LightLayerEnum(IntFlag):
    Nothing = 0
    LightLayerDefault = 1
    LightLayer1 = 2
    LightLayer2 = 4
    LightLayer3 = 8
    LightLayer4 = 16
    LightLayer5 = 32
    LightLayer6 = 64
    LightLayer7 = 128
    Everything = 255

# UnityEngine.Rendering.Universal.LightProbeSystem
class LightProbeSystem(IntFlag):
    LegacyLightProbes = 0
    ProbeVolumes = 1

# UnityEngine.Rendering.Universal.LightRenderingMode
class LightRenderingMode(IntFlag):
    Disabled = 0
    PerVertex = 2
    PerPixel = 1

# UnityEngine.Rendering.Universal.MixedLightingSetup
class MixedLightingSetup(IntFlag):
    NONE = 0
    ShadowMask = 1
    Subtractive = 2

# UnityEngine.Rendering.Universal.MotionBlurMode
class MotionBlurMode(IntFlag):
    CameraOnly = 0
    CameraAndObjects = 1

# UnityEngine.Rendering.Universal.MotionBlurQuality
class MotionBlurQuality(IntFlag):
    Low = 0
    Medium = 1
    High = 2

# UnityEngine.Rendering.Universal.MsaaQuality
class MsaaQuality(IntFlag):
    Disabled = 1
    _2x = 2
    _4x = 4
    _8x = 8

# UnityEngine.Rendering.Universal.NeutralRangeReductionMode
class NeutralRangeReductionMode(IntFlag):
    Reinhard = 1
    BT2390 = 2

# UnityEngine.Rendering.Universal.PipelineDebugLevel
class PipelineDebugLevel(IntFlag):
    Disabled = 0
    Profiling = 1

# UnityEngine.Rendering.Universal.PixelValidationChannels
class PixelValidationChannels(IntFlag):
    RGB = 0
    R = 1
    G = 2
    B = 3
    A = 4

# UnityEngine.Rendering.Universal.RenderGraphSettings
class RenderGraphSettings(IntFlag):
    Initial = 0

# UnityEngine.Rendering.Universal.RenderObjects
class RenderObjects(IntFlag):
    NONE = 0
    Material = 1
    Shader = 2

# UnityEngine.Rendering.Universal.RenderPassEvent
class RenderPassEvent(IntFlag):
    BeforeRendering = 0
    BeforeRenderingShadows = 50
    AfterRenderingShadows = 100
    BeforeRenderingPrePasses = 150
    AfterRenderingPrePasses = 200
    BeforeRenderingGbuffer = 210
    AfterRenderingGbuffer = 220
    BeforeRenderingDeferredLights = 230
    AfterRenderingDeferredLights = 240
    BeforeRenderingOpaques = 250
    AfterRenderingOpaques = 300
    BeforeRenderingSkybox = 350
    AfterRenderingSkybox = 400
    BeforeRenderingTransparents = 450
    AfterRenderingTransparents = 500
    BeforeRenderingPostProcessing = 550
    AfterRenderingPostProcessing = 600
    AfterRendering = 1000

# UnityEngine.Rendering.Universal.RenderPathCompatibility
class RenderPathCompatibility(IntFlag):
    Forward = 1
    Deferred = 2
    ForwardPlus = 4
    DeferredPlus = 8
    All = 15

# UnityEngine.Rendering.Universal.RenderQueueType
class RenderQueueType(IntFlag):
    Opaque = 0
    Transparent = 1

# UnityEngine.Rendering.Universal.RendererOverrideOption
class RendererOverrideOption(IntFlag):
    Custom = 0
    UsePipelineSettings = 1

# UnityEngine.Rendering.Universal.RendererType
class RendererType(IntFlag):
    Custom = 0
    UniversalRenderer = 1
    _2DRenderer = 2

# UnityEngine.Rendering.Universal.RenderingLayerUtils
class RenderingLayerUtils(IntFlag):
    DepthNormalPrePass = 0
    Opaque = 1

# UnityEngine.Rendering.Universal.RenderingLayerUtils
class RenderingLayerUtils(IntFlag):
    Bits8 = 0
    Bits16 = 1
    Bits24 = 2
    Bits32 = 3

# UnityEngine.Rendering.Universal.RenderingMode
class RenderingMode(IntFlag):
    Forward = 0
    ForwardPlus = 2
    Deferred = 1
    DeferredPlus = 3

# UnityEngine.Rendering.Universal.SampleCount
class SampleCount(IntFlag):
    One = 1
    Two = 2
    Four = 4

# UnityEngine.Rendering.Universal.ScreenSpaceAmbientOcclusionPass
class ScreenSpaceAmbientOcclusionPass(IntFlag):
    Bilateral = 0
    Gaussian = 1
    Kawase = 2

# UnityEngine.Rendering.Universal.ScreenSpaceAmbientOcclusionPass
class ScreenSpaceAmbientOcclusionPass(IntFlag):
    AmbientOcclusion = 0
    BilateralBlurHorizontal = 1
    BilateralBlurVertical = 2
    BilateralBlurFinal = 3
    BilateralAfterOpaque = 4
    GaussianBlurHorizontal = 5
    GaussianBlurVertical = 6
    GaussianAfterOpaque = 7
    KawaseBlur = 8
    KawaseAfterOpaque = 9

# UnityEngine.Rendering.Universal.ScreenSpaceAmbientOcclusionSettings
class ScreenSpaceAmbientOcclusionSettings(IntFlag):
    Depth = 0
    DepthNormals = 1

# UnityEngine.Rendering.Universal.ScreenSpaceAmbientOcclusionSettings
class ScreenSpaceAmbientOcclusionSettings(IntFlag):
    Low = 0
    Medium = 1
    High = 2

# UnityEngine.Rendering.Universal.ScreenSpaceAmbientOcclusionSettings
class ScreenSpaceAmbientOcclusionSettings(IntFlag):
    High = 0
    Medium = 1
    Low = 2

# UnityEngine.Rendering.Universal.ScreenSpaceAmbientOcclusionSettings
class ScreenSpaceAmbientOcclusionSettings(IntFlag):
    BlueNoise = 0
    InterleavedGradient = 1

# UnityEngine.Rendering.Universal.ScreenSpaceAmbientOcclusionSettings
class ScreenSpaceAmbientOcclusionSettings(IntFlag):
    High = 0
    Medium = 1
    Low = 2

# UnityEngine.Rendering.Universal.ScreenSpaceLensFlareResolution
class ScreenSpaceLensFlareResolution(IntFlag):
    Half = 2
    Quarter = 4
    Eighth = 8

# UnityEngine.Rendering.Universal.ScriptableRenderPassInput
class ScriptableRenderPassInput(IntFlag):
    NONE = 0
    Depth = 1
    Normal = 2
    Color = 4
    Motion = 8

# UnityEngine.Rendering.Universal.ShEvalMode
class ShEvalMode(IntFlag):
    Auto = 0
    PerVertex = 1
    Mixed = 2
    PerPixel = 3

# UnityEngine.Rendering.Universal.ShaderPathID
class ShaderPathID(IntFlag):
    Lit = 0
    SimpleLit = 1
    Unlit = 2
    TerrainLit = 3
    ParticlesLit = 4
    ParticlesSimpleLit = 5
    ParticlesUnlit = 6
    BakedLit = 7
    SpeedTree7 = 8
    SpeedTree7Billboard = 9
    SpeedTree8 = 10
    SpeedTree9 = 11
    ComplexLit = 12

# UnityEngine.Rendering.Universal.ShaderVariantLogLevel
class ShaderVariantLogLevel(IntFlag):
    Disabled = 0
    OnlyUniversalRPShaders = 1
    AllShaders = 2

# UnityEngine.Rendering.Universal.ShadowCascadesOption
class ShadowCascadesOption(IntFlag):
    NoCascades = 0
    TwoCascades = 1
    FourCascades = 2

# UnityEngine.Rendering.Universal.ShadowQuality
class ShadowQuality(IntFlag):
    Disabled = 0
    HardShadows = 1
    SoftShadows = 2

# UnityEngine.Rendering.Universal.ShadowResolution
class ShadowResolution(IntFlag):
    _256 = 256
    _512 = 512
    _1024 = 1024
    _2048 = 2048
    _4096 = 4096
    _8192 = 8192

# UnityEngine.Rendering.Universal.SoftShadowQuality
class SoftShadowQuality(IntFlag):
    UsePipelineSettings = 0
    Low = 1
    Medium = 2
    High = 3

# UnityEngine.Rendering.Universal.StoreActionsOptimization
class StoreActionsOptimization(IntFlag):
    Auto = 0
    Discard = 1
    Store = 2

# UnityEngine.Rendering.Universal.TemporalAAQuality
class TemporalAAQuality(IntFlag):
    VeryLow = 0
    Low = 1
    Medium = 2
    High = 3
    VeryHigh = 4

# UnityEngine.Rendering.Universal.TileSize
class TileSize(IntFlag):
    _8 = 8
    _16 = 16
    _32 = 32
    _64 = 64

# UnityEngine.Rendering.Universal.TonemappingMode
class TonemappingMode(IntFlag):
    NONE = 0
    Neutral = 1
    ACES = 2

# UnityEngine.Rendering.Universal.URPDefaultVolumeProfileSettings
class URPDefaultVolumeProfileSettings(IntFlag):
    Initial = 0

# UnityEngine.Rendering.Universal.URPProfileId
class URPProfileId(IntFlag):
    UniversalRenderTotal = 0
    UpdateVolumeFramework = 1
    RenderCameraStack = 2
    AdditionalLightsShadow = 3
    ColorGradingLUT = 4
    CopyColor = 5
    CopyDepth = 6
    DrawDepthNormalPrepass = 7
    DepthPrepass = 8
    UpdateReflectionProbeAtlas = 9
    DrawOpaqueObjects = 10
    DrawTransparentObjects = 11
    DrawScreenSpaceUI = 12
    RecordRenderGraph = 13
    LightCookies = 14
    MainLightShadow = 15
    ResolveShadows = 16
    SSAO = 17
    StopNaNs = 18
    SMAA = 19
    GaussianDepthOfField = 20
    BokehDepthOfField = 21
    TemporalAA = 22
    MotionBlur = 23
    PaniniProjection = 24
    UberPostProcess = 25
    Bloom = 26
    LensFlareDataDrivenComputeOcclusion = 27
    LensFlareDataDriven = 28
    LensFlareScreenSpace = 29
    DrawMotionVectors = 30
    DrawFullscreen = 31
    RG_SetupPostFX = 32
    RG_StopNaNs = 33
    RG_SMAAMaterialSetup = 34
    RG_SMAAEdgeDetection = 35
    RG_SMAABlendWeight = 36
    RG_SMAANeighborhoodBlend = 37
    RG_SetupDoF = 38
    RG_DOFComputeCOC = 39
    RG_DOFDownscalePrefilter = 40
    RG_DOFBlurH = 41
    RG_DOFBlurV = 42
    RG_DOFBlurBokeh = 43
    RG_DOFPostFilter = 44
    RG_DOFComposite = 45
    RG_TAA = 46
    RG_TAACopyHistory = 47
    RG_MotionBlur = 48
    RG_BloomSetup = 49
    RG_BloomPrefilter = 50
    RG_BloomDownsample = 51
    RG_BloomUpsample = 52
    RG_UberPostSetupBloomPass = 53
    RG_UberPost = 54
    RG_FinalSetup = 55
    RG_FinalFSRScale = 56
    RG_FinalBlit = 57
    BlitFinalToBackBuffer = 58
    DrawSkybox = 59

# UnityEngine.Rendering.Universal.URPShaderStrippingSetting
class URPShaderStrippingSetting(IntFlag):
    Initial = 0

# UnityEngine.Rendering.Universal.UniversalRenderer
class UniversalRenderer(IntFlag):
    NONE = 0
    DepthPrepass = 1
    ForwardOpaque = 2
    GBuffer = 3

# UnityEngine.Rendering.Universal.UniversalRenderer
class UniversalRenderer(IntFlag):
    DuringPrepass = 0
    AfterPrepass = 1
    AfterGBuffer = 2
    AfterOpaques = 3
    AfterSkybox = 4
    AfterTransparents = 5
    NONE = 6

# UnityEngine.Rendering.Universal.UniversalRenderer
class UniversalRenderer(IntFlag):
    AfterSkybox = 0
    NONE = 1

# UnityEngine.Rendering.Universal.UniversalRendererStencilRef
class UniversalRendererStencilRef(IntFlag):
    CrossFadeStencilRef_0 = 4
    CrossFadeStencilRef_1 = 8
    CrossFadeStencilRef_All = 12

# UnityEngine.Rendering.Universal.UniversalResource
class UniversalResource(IntFlag):
    BackBufferColor = 0
    BackBufferDepth = 1
    CameraColor = 2
    CameraDepth = 3
    MainShadowsTexture = 4
    AdditionalShadowsTexture = 5
    GBuffer0 = 6
    GBuffer1 = 7
    GBuffer2 = 8
    GBuffer3 = 9
    GBuffer4 = 10
    GBuffer5 = 11
    GBuffer6 = 12
    CameraOpaqueTexture = 13
    CameraDepthTexture = 14
    CameraNormalsTexture = 15
    MotionVectorColor = 16
    MotionVectorDepth = 17
    InternalColorLut = 18
    DebugScreenColor = 19
    DebugScreenDepth = 20
    AfterPostProcessColor = 21
    OverlayUITexture = 22
    RenderingLayersTexture = 23
    DBuffer0 = 24
    DBuffer1 = 25
    DBuffer2 = 26
    DBufferDepth = 27
    SSAOTexture = 28

# UnityEngine.Rendering.Universal.UniversalResourceDataBase
class UniversalResourceDataBase(IntFlag):
    Camera = 0
    BackBuffer = 1

# UnityEngine.Rendering.Universal.UpscalingFilterSelection
class UpscalingFilterSelection(IntFlag):
    Auto = 0
    Linear = 1
    Point = 2
    FSR = 3
    STP = 4

# UnityEngine.Rendering.Universal.VolumeFrameworkUpdateMode
class VolumeFrameworkUpdateMode(IntFlag):
    EveryFrame = 0
    ViaScripting = 1
    UsePipelineSettings = 2

