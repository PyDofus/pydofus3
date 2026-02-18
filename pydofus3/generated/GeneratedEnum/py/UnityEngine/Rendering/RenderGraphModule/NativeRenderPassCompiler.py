from enum import IntFlag

# UnityEngine.Rendering.RenderGraphModule.NativeRenderPassCompiler.LoadReason
class LoadReason(IntFlag):
    InvalidReason = 0
    LoadImported = 1
    LoadPreviouslyWritten = 2
    ClearImported = 3
    ClearCreated = 4
    FullyRewritten = 5
    Count = 6

# UnityEngine.Rendering.RenderGraphModule.NativeRenderPassCompiler.NativePassCompiler
class NativePassCompiler(IntFlag):
    NRPRGComp_PrepareNativePass = 0
    NRPRGComp_SetupContextData = 1
    NRPRGComp_BuildGraph = 2
    NRPRGComp_CullNodes = 3
    NRPRGComp_TryMergeNativePasses = 4
    NRPRGComp_FindResourceUsageRanges = 5
    NRPRGComp_DetectMemorylessResources = 6
    NRPRGComp_ExecuteCreateResources = 7
    NRPRGComp_ExecuteBeginRenderpassCommand = 8
    NRPRGComp_ExecuteDestroyResources = 9

# UnityEngine.Rendering.RenderGraphModule.NativeRenderPassCompiler.PassBreakReason
class PassBreakReason(IntFlag):
    NotOptimized = 0
    TargetSizeMismatch = 1
    NextPassReadsTexture = 2
    NonRasterPass = 3
    DifferentDepthTextures = 4
    AttachmentLimitReached = 5
    SubPassLimitReached = 6
    EndOfGraph = 7
    FRStateMismatch = 8
    DifferentShadingRateImages = 9
    DifferentShadingRateStates = 10
    PassMergingDisabled = 11
    Merged = 12
    Count = 13

# UnityEngine.Rendering.RenderGraphModule.NativeRenderPassCompiler.PassMergeState
class PassMergeState(IntFlag):
    NONE = -1
    Begin = 0
    SubPass = 1
    End = 2

# UnityEngine.Rendering.RenderGraphModule.NativeRenderPassCompiler.StoreReason
class StoreReason(IntFlag):
    InvalidReason = 0
    StoreImported = 1
    StoreUsedByLaterPass = 2
    DiscardImported = 3
    DiscardUnused = 4
    DiscardBindMs = 5
    NoMSAABuffer = 6
    Count = 7

