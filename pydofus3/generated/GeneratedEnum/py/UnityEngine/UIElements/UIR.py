from enum import IntFlag

# UnityEngine.UIElements.UIR.ClipMethod
class ClipMethod(IntFlag):
    Undetermined = 0
    NotClipped = 1
    Scissor = 2
    ShaderDiscard = 3
    Stencil = 4

# UnityEngine.UIElements.UIR.CommandType
class CommandType(IntFlag):
    Draw = 0
    ImmediateCull = 1
    Immediate = 2
    PushView = 3
    PopView = 4
    PushScissor = 5
    PopScissor = 6
    PushRenderTexture = 7
    PopRenderTexture = 8
    BlitToPreviousRT = 9
    PushDefaultMaterial = 10
    PopDefaultMaterial = 11
    BeginDisable = 12
    EndDisable = 13
    CutRenderChain = 14

# UnityEngine.UIElements.UIR.EntryFlags
class EntryFlags(IntFlag):
    UsesTextCoreSettings = 1

# UnityEngine.UIElements.UIR.EntryType
class EntryType(IntFlag):
    DrawSolidMesh = 0
    DrawTexturedMesh = 1
    DrawTexturedMeshSkipAtlas = 2
    DrawTextMesh = 3
    DrawGradients = 4
    DrawImmediate = 5
    DrawImmediateCull = 6
    DrawChildren = 7
    BeginStencilMask = 8
    EndStencilMask = 9
    PopStencilMask = 10
    PushClippingRect = 11
    PopClippingRect = 12
    PushScissors = 13
    PopScissors = 14
    PushGroupMatrix = 15
    PopGroupMatrix = 16
    PushRenderTexture = 17
    BlitAndPopRenderTexture = 18
    PushDefaultMaterial = 19
    PopDefaultMaterial = 20
    CutRenderChain = 21
    DedicatedPlaceholder = 22

# UnityEngine.UIElements.UIR.OwnedState
class OwnedState(IntFlag):
    Inherited = 0
    Owned = 1

# UnityEngine.UIElements.UIR.RenderChain
class RenderChain(IntFlag):
    Head = 0
    Tail = 1

# UnityEngine.UIElements.UIR.RenderDataDirtyTypeClasses
class RenderDataDirtyTypeClasses(IntFlag):
    Clipping = 0
    Opacity = 1
    Color = 2
    TransformSize = 3
    Visuals = 4
    Count = 5

# UnityEngine.UIElements.UIR.RenderDataDirtyTypes
class RenderDataDirtyTypes(IntFlag):
    NONE = 0
    Transform = 1
    ClipRectSize = 2
    Clipping = 4
    ClippingHierarchy = 8
    Visuals = 16
    VisualsHierarchy = 32
    VisualsOpacityId = 64
    Opacity = 128
    OpacityHierarchy = 256
    Color = 512
    AllVisuals = 112

# UnityEngine.UIElements.UIR.RenderDataFlags
class RenderDataFlags(IntFlag):
    IsInChain = 1
    IsGroupTransform = 2
    IsIgnoringDynamicColorHint = 4
    HasExtraData = 8
    HasExtraMeshes = 16

# UnityEngine.UIElements.UIR.SerializedCommandType
class SerializedCommandType(IntFlag):
    DrawRanges = 0
    SetTexture = 1
    ApplyBatchProps = 2

# UnityEngine.UIElements.UIR.Utility
class Utility(IntFlag):
    Vertex = 0
    Index = 1

# UnityEngine.UIElements.UIR.VertexFlags
class VertexFlags(IntFlag):
    IsSolid = 0
    IsText = 1
    IsTextured = 2
    IsDynamic = 3
    IsSvgGradients = 4

