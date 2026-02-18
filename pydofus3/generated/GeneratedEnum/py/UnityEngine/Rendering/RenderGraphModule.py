from enum import IntFlag

# UnityEngine.Rendering.RenderGraphModule.AccessFlags
class AccessFlags(IntFlag):
    NONE = 0
    Read = 1
    Write = 2
    Discard = 4
    WriteAll = 6
    ReadWrite = 3

# UnityEngine.Rendering.RenderGraphModule.DepthAccess
class DepthAccess(IntFlag):
    Read = 1
    Write = 2
    ReadWrite = 3

# UnityEngine.Rendering.RenderGraphModule.RenderGraphPassType
class RenderGraphPassType(IntFlag):
    Legacy = 0
    Unsafe = 1
    Raster = 2
    Compute = 3

# UnityEngine.Rendering.RenderGraphModule.RenderGraphProfileId
class RenderGraphProfileId(IntFlag):
    CompileRenderGraph = 0
    ExecuteRenderGraph = 1
    ComputeHashRenderGraph = 2

# UnityEngine.Rendering.RenderGraphModule.RenderGraphResourceType
class RenderGraphResourceType(IntFlag):
    Texture = 0
    Buffer = 1
    AccelerationStructure = 2
    Count = 3

# UnityEngine.Rendering.RenderGraphModule.RendererListHandleType
class RendererListHandleType(IntFlag):
    Renderers = 0
    Legacy = 1

# UnityEngine.Rendering.RenderGraphModule.TextureSizeMode
class TextureSizeMode(IntFlag):
    Explicit = 0
    Scale = 1
    Functor = 2

