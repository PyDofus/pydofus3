from enum import IntFlag

# UnityEngine.UIElements.AddressMode
class AddressMode(IntFlag):
    Wrap = 0
    Clamp = 1
    Mirror = 2

# UnityEngine.UIElements.Align
class Align(IntFlag):
    Auto = 0
    FlexStart = 1
    Center = 2
    FlexEnd = 3
    Stretch = 4

# UnityEngine.UIElements.AlternatingRowBackground
class AlternatingRowBackground(IntFlag):
    NONE = 0
    ContentOnly = 1
    All = 2

# UnityEngine.UIElements.Angle
class Angle(IntFlag):
    Degree = 0
    Gradian = 1
    Radian = 2
    Turn = 3
    NONE = 4

# UnityEngine.UIElements.AngleUnit
class AngleUnit(IntFlag):
    Degree = 0
    Gradian = 1
    Radian = 2
    Turn = 3

# UnityEngine.UIElements.ArcDirection
class ArcDirection(IntFlag):
    Clockwise = 0
    CounterClockwise = 1

# UnityEngine.UIElements.Axis
class Axis(IntFlag):
    X = 0
    Y = 1
    Z = 2

# UnityEngine.UIElements.BackgroundPositionKeyword
class BackgroundPositionKeyword(IntFlag):
    Center = 0
    Top = 1
    Bottom = 2
    Left = 3
    Right = 4

# UnityEngine.UIElements.BackgroundSizeType
class BackgroundSizeType(IntFlag):
    Length = 0
    Cover = 1
    Contain = 2

# UnityEngine.UIElements.BaseSlider
class BaseSlider(IntFlag):
    NONE = 0
    Lowest = 1
    LowerPage = 2
    Lower = 3
    Higher = 4
    HigherPage = 5
    Highest = 6

# UnityEngine.UIElements.BaseVisualTreeHierarchyTrackerUpdater
class BaseVisualTreeHierarchyTrackerUpdater(IntFlag):
    Waiting = 0
    TrackingAddOrMove = 1
    TrackingRemove = 2

# UnityEngine.UIElements.BindingLogLevel
class BindingLogLevel(IntFlag):
    NONE = 0
    Once = 1
    All = 2

# UnityEngine.UIElements.BindingMode
class BindingMode(IntFlag):
    TwoWay = 0
    ToSource = 1
    ToTarget = 2
    ToTargetOnce = 3

# UnityEngine.UIElements.BindingSourceSelectionMode
class BindingSourceSelectionMode(IntFlag):
    Manual = 0
    AutoAssign = 1

# UnityEngine.UIElements.BindingStatus
class BindingStatus(IntFlag):
    Success = 0
    Failure = 1
    Pending = 2

# UnityEngine.UIElements.BindingUpdateStage
class BindingUpdateStage(IntFlag):
    UpdateUI = 0
    UpdateSource = 1

# UnityEngine.UIElements.BindingUpdateTrigger
class BindingUpdateTrigger(IntFlag):
    WhenDirty = 0
    OnSourceChanged = 1
    EveryUpdate = 2

# UnityEngine.UIElements.ClampedDragger
class ClampedDragger(IntFlag):
    NONE = 0
    LowToHigh = 1
    HighToLow = 2
    Free = 4

# UnityEngine.UIElements.CollectionVirtualizationMethod
class CollectionVirtualizationMethod(IntFlag):
    FixedHeight = 0
    DynamicHeight = 1

# UnityEngine.UIElements.ColumnDataType
class ColumnDataType(IntFlag):
    Name = 0
    Title = 1
    Icon = 2
    Visibility = 3
    Width = 4
    MaxWidth = 5
    MinWidth = 6
    Stretchable = 7
    Sortable = 8
    Optional = 9
    Resizable = 10
    HeaderTemplate = 11
    CellTemplate = 12

# UnityEngine.UIElements.ColumnSortingMode
class ColumnSortingMode(IntFlag):
    NONE = 0
    Default = 1
    Custom = 2

# UnityEngine.UIElements.Columns
class Columns(IntFlag):
    Grow = 0
    GrowAndFill = 1

# UnityEngine.UIElements.ColumnsDataType
class ColumnsDataType(IntFlag):
    PrimaryColumn = 0
    StretchMode = 1
    Reorderable = 2
    Resizable = 3
    ResizePreview = 4

# UnityEngine.UIElements.ContextType
class ContextType(IntFlag):
    Player = 0
    Editor = 1

# UnityEngine.UIElements.DefaultEventSystem
class DefaultEventSystem(IntFlag):
    Always = 0
    IgnoreIfAppNotFocused = 1

# UnityEngine.UIElements.DeltaSpeed
class DeltaSpeed(IntFlag):
    Fast = 0
    Normal = 1
    Slow = 2

# UnityEngine.UIElements.DispatchMode
class DispatchMode(IntFlag):
    Default = 1
    Queued = 1
    Immediate = 2

# UnityEngine.UIElements.DisplayStyle
class DisplayStyle(IntFlag):
    Flex = 0
    NONE = 1

# UnityEngine.UIElements.DragAndDropPosition
class DragAndDropPosition(IntFlag):
    OverItem = 0
    BetweenItems = 1
    OutsideItems = 2

# UnityEngine.UIElements.DragEventsProcessor
class DragEventsProcessor(IntFlag):
    NONE = 0
    CanStartDrag = 1
    Dragging = 2

# UnityEngine.UIElements.DragVisualMode
class DragVisualMode(IntFlag):
    NONE = 0
    Copy = 1
    Move = 2
    Rejected = 3

# UnityEngine.UIElements.DropdownMenuAction
class DropdownMenuAction(IntFlag):
    NONE = 0
    Normal = 1
    Disabled = 2
    Checked = 4
    Hidden = 8

# UnityEngine.UIElements.DynamicAtlasFilters
class DynamicAtlasFilters(IntFlag):
    NONE = 0
    Readability = 1
    Size = 2
    Format = 4
    ColorSpace = 8
    FilterMode = 16

# UnityEngine.UIElements.DynamicHeightVirtualizationController
class DynamicHeightVirtualizationController(IntFlag):
    NONE = 0
    Resize = 1
    Scroll = 2
    ForcedScroll = 3

# UnityEngine.UIElements.DynamicHeightVirtualizationController
class DynamicHeightVirtualizationController(IntFlag):
    Idle = 0
    Up = 1
    Down = 2

# UnityEngine.UIElements.EasingMode
class EasingMode(IntFlag):
    Ease = 0
    EaseIn = 1
    EaseOut = 2
    EaseInOut = 3
    Linear = 4
    EaseInSine = 5
    EaseOutSine = 6
    EaseInOutSine = 7
    EaseInCubic = 8
    EaseOutCubic = 9
    EaseInOutCubic = 10
    EaseInCirc = 11
    EaseOutCirc = 12
    EaseInOutCirc = 13
    EaseInElastic = 14
    EaseOutElastic = 15
    EaseInOutElastic = 16
    EaseInBack = 17
    EaseOutBack = 18
    EaseInOutBack = 19
    EaseInBounce = 20
    EaseOutBounce = 21
    EaseInOutBounce = 22

# UnityEngine.UIElements.EditorTextRenderingMode
class EditorTextRenderingMode(IntFlag):
    SDF = 0
    Bitmap = 1

# UnityEngine.UIElements.EventBase
class EventBase(IntFlag):
    NONE = 0
    Bubbles = 1
    TricklesDown = 2
    SkipDisabledElements = 4
    BubblesOrTricklesDown = 3

# UnityEngine.UIElements.EventBase
class EventBase(IntFlag):
    NONE = 0
    PropagationStopped = 1
    ImmediatePropagationStopped = 2
    Dispatching = 4
    Pooled = 8
    IMGUIEventIsValid = 16
    PropagateToIMGUI = 32
    Dispatched = 64
    Processed = 128
    ProcessedByFocusController = 256

# UnityEngine.UIElements.EventCategory
class EventCategory(IntFlag):
    Default = 0
    Pointer = 1
    PointerMove = 2
    PointerDown = 3
    EnterLeave = 4
    EnterLeaveWindow = 5
    Keyboard = 6
    Geometry = 7
    Style = 8
    ChangeValue = 9
    Bind = 10
    Focus = 11
    ChangePanel = 12
    StyleTransition = 13
    Navigation = 14
    Command = 15
    Tooltip = 16
    DragAndDrop = 17
    IMGUI = 18

# UnityEngine.UIElements.EventCategoryFlags
class EventCategoryFlags(IntFlag):
    NONE = 0
    All = -1
    TriggeredByOS = 426094
    TargetOnly = 5536

# UnityEngine.UIElements.EventInterestOptions
class EventInterestOptions(IntFlag):
    Inherit = 0
    AllEventTypes = -1

# UnityEngine.UIElements.EventInterestOptionsInternal
class EventInterestOptionsInternal(IntFlag):
    TriggeredByOS = 426094

# UnityEngine.UIElements.FillRule
class FillRule(IntFlag):
    NonZero = 0
    OddEven = 1

# UnityEngine.UIElements.FlexDirection
class FlexDirection(IntFlag):
    Column = 0
    ColumnReverse = 1
    Row = 2
    RowReverse = 3

# UnityEngine.UIElements.GradientType
class GradientType(IntFlag):
    Linear = 0
    Radial = 1

# UnityEngine.UIElements.HelpBoxMessageType
class HelpBoxMessageType(IntFlag):
    NONE = 0
    Info = 1
    Warning = 2
    Error = 3

# UnityEngine.UIElements.HierarchyChangeType
class HierarchyChangeType(IntFlag):
    AddedToParent = 0
    RemovedFromParent = 1
    ChildrenReordered = 2
    AttachedToPanel = 3
    DetachedFromPanel = 4

# UnityEngine.UIElements.InvokePolicy
class InvokePolicy(IntFlag):
    Default = 0
    IncludeDisabled = 1
    Once = 2

# UnityEngine.UIElements.Justify
class Justify(IntFlag):
    FlexStart = 0
    Center = 1
    FlexEnd = 2
    SpaceBetween = 3
    SpaceAround = 4
    SpaceEvenly = 5

# UnityEngine.UIElements.KeyboardNavigationOperation
class KeyboardNavigationOperation(IntFlag):
    NONE = 0
    SelectAll = 1
    Cancel = 2
    Submit = 3
    Previous = 4
    Next = 5
    MoveRight = 6
    MoveLeft = 7
    PageUp = 8
    PageDown = 9
    Begin = 10
    End = 11

# UnityEngine.UIElements.LanguageDirection
class LanguageDirection(IntFlag):
    Inherit = 0
    LTR = 1
    RTL = 2

# UnityEngine.UIElements.Length
class Length(IntFlag):
    Pixel = 0
    Percent = 1
    Auto = 2
    NONE = 3

# UnityEngine.UIElements.LengthUnit
class LengthUnit(IntFlag):
    Pixel = 0
    Percent = 1

# UnityEngine.UIElements.LibraryVisibility
class LibraryVisibility(IntFlag):
    Default = 0
    Visible = 1
    Hidden = 2

# UnityEngine.UIElements.LineCap
class LineCap(IntFlag):
    Butt = 0
    Round = 1

# UnityEngine.UIElements.LineJoin
class LineJoin(IntFlag):
    Miter = 0
    Bevel = 1
    Round = 2

# UnityEngine.UIElements.ListViewReorderMode
class ListViewReorderMode(IntFlag):
    Simple = 0
    Animated = 1

# UnityEngine.UIElements.MeshGenerationCallbackType
class MeshGenerationCallbackType(IntFlag):
    Fork = 0
    WorkThenFork = 1
    Work = 2

# UnityEngine.UIElements.MeshGenerationContext
class MeshGenerationContext(IntFlag):
    NONE = 0
    SkipDynamicAtlas = 2
    IsUsingVectorImageGradients = 4
    SliceTiled = 8

# UnityEngine.UIElements.MinMaxSlider
class MinMaxSlider(IntFlag):
    MinThumb = 0
    MaxThumb = 1
    MiddleThumb = 2
    NoThumb = 3

# UnityEngine.UIElements.MouseButton
class MouseButton(IntFlag):
    LeftMouse = 0
    RightMouse = 1
    MiddleMouse = 2

# UnityEngine.UIElements.NavigationDeviceType
class NavigationDeviceType(IntFlag):
    Unknown = 0
    Keyboard = 1
    NonKeyboard = 2

# UnityEngine.UIElements.NavigationMoveEvent
class NavigationMoveEvent(IntFlag):
    NONE = 0
    Left = 1
    Up = 2
    Right = 3
    Down = 4
    Next = 5
    Previous = 6

# UnityEngine.UIElements.Overflow
class Overflow(IntFlag):
    Visible = 0
    Hidden = 1

# UnityEngine.UIElements.OverflowClipBox
class OverflowClipBox(IntFlag):
    PaddingBox = 0
    ContentBox = 1

# UnityEngine.UIElements.OverflowInternal
class OverflowInternal(IntFlag):
    Visible = 0
    Hidden = 1
    Scroll = 2

# UnityEngine.UIElements.PanelEventHandler
class PanelEventHandler(IntFlag):
    Default = 0
    Down = 1
    Up = 2

# UnityEngine.UIElements.PanelRenderMode
class PanelRenderMode(IntFlag):
    ScreenSpaceOverlay = 0
    WorldSpace = 1

# UnityEngine.UIElements.PanelScaleMode
class PanelScaleMode(IntFlag):
    ConstantPixelSize = 0
    ConstantPhysicalSize = 1
    ScaleWithScreenSize = 2

# UnityEngine.UIElements.PanelScreenMatchMode
class PanelScreenMatchMode(IntFlag):
    MatchWidthOrHeight = 0
    Shrink = 1
    Expand = 2

# UnityEngine.UIElements.PickingMode
class PickingMode(IntFlag):
    Position = 0
    Ignore = 1

# UnityEngine.UIElements.PointerDeviceState
class PointerDeviceState(IntFlag):
    NONE = 0
    OutsidePanel = 1

# UnityEngine.UIElements.Position
class Position(IntFlag):
    Relative = 0
    Absolute = 1

# UnityEngine.UIElements.PropagationPhase
class PropagationPhase(IntFlag):
    NONE = 0
    TrickleDown = 1
    BubbleUp = 3
    AtTarget = 2
    DefaultAction = 4
    DefaultActionAtTarget = 5

# UnityEngine.UIElements.PseudoStates
class PseudoStates(IntFlag):
    Active = 1
    Hover = 2
    Checked = 8
    Disabled = 32
    Focus = 64
    Root = 128

# UnityEngine.UIElements.RenderHints
class RenderHints(IntFlag):
    NONE = 0
    GroupTransform = 1
    BoneTransform = 2
    ClipWithScissors = 4
    MaskContainer = 8
    DynamicColor = 16
    DirtyOffset = 5
    DirtyGroupTransform = 32
    DirtyBoneTransform = 64
    DirtyClipWithScissors = 128
    DirtyMaskContainer = 256
    DirtyDynamicColor = 512
    DirtyAll = 992

# UnityEngine.UIElements.Repeat
class Repeat(IntFlag):
    NoRepeat = 0
    Space = 1
    Round = 2
    Repeat = 3

# UnityEngine.UIElements.Salt
class Salt(IntFlag):
    TagNameSalt = 13
    IdSalt = 17
    ClassSalt = 19

# UnityEngine.UIElements.ScrollView
class ScrollView(IntFlag):
    Unrestricted = 0
    Elastic = 1
    Clamped = 2

# UnityEngine.UIElements.ScrollView
class ScrollView(IntFlag):
    Default = 0
    StopScrolling = 1
    ForwardScrolling = 2

# UnityEngine.UIElements.ScrollView
class ScrollView(IntFlag):
    Apply = 0
    Forward = 1
    Block = 2

# UnityEngine.UIElements.ScrollViewMode
class ScrollViewMode(IntFlag):
    Vertical = 0
    Horizontal = 1
    VerticalAndHorizontal = 2

# UnityEngine.UIElements.ScrollerVisibility
class ScrollerVisibility(IntFlag):
    Auto = 0
    AlwaysVisible = 1
    Hidden = 2

# UnityEngine.UIElements.SelectionType
class SelectionType(IntFlag):
    NONE = 0
    Single = 1
    Multiple = 2

# UnityEngine.UIElements.SliceType
class SliceType(IntFlag):
    Sliced = 0
    Tiled = 1

# UnityEngine.UIElements.SliderDirection
class SliderDirection(IntFlag):
    Horizontal = 0
    Vertical = 1

# UnityEngine.UIElements.SortDirection
class SortDirection(IntFlag):
    Ascending = 0
    Descending = 1

# UnityEngine.UIElements.StyleKeyword
class StyleKeyword(IntFlag):
    Undefined = 0
    Null = 1
    Auto = 2
    NONE = 3
    Initial = 4

# UnityEngine.UIElements.StylePropertyAnimationSystem
class StylePropertyAnimationSystem(IntFlag):
    NONE = 0
    Running = 1
    Started = 2
    Ended = 4
    Canceled = 8

# UnityEngine.UIElements.StyleSelectorRelationship
class StyleSelectorRelationship(IntFlag):
    NONE = 0
    Child = 1
    Descendent = 2

# UnityEngine.UIElements.StyleSelectorType
class StyleSelectorType(IntFlag):
    Unknown = 0
    Wildcard = 1
    Type = 2
    Class = 3
    PseudoClass = 4
    RecursivePseudoClass = 5
    ID = 6
    Predicate = 7

# UnityEngine.UIElements.StyleSheet
class StyleSheet(IntFlag):
    NONE = -1
    Name = 0
    Type = 1
    Class = 2
    Length = 3

# UnityEngine.UIElements.StyleValueFunction
class StyleValueFunction(IntFlag):
    Unknown = 0
    Var = 1
    Env = 2
    LinearGradient = 3

# UnityEngine.UIElements.StyleValueKeyword
class StyleValueKeyword(IntFlag):
    Inherit = 0
    Initial = 1
    Auto = 2
    Unset = 3
    TRUE = 4
    FALSE = 5
    NONE = 6
    Cover = 7
    Contain = 8

# UnityEngine.UIElements.StyleValueType
class StyleValueType(IntFlag):
    Invalid = 0
    Keyword = 1
    Float = 2
    Dimension = 3
    Color = 4
    ResourcePath = 5
    AssetReference = 6
    Enum = 7
    Variable = 8
    String = 9
    Function = 10
    CommaSeparator = 11
    ScalableImage = 12
    MissingAssetReference = 13

# UnityEngine.UIElements.StyleVariableResolver
class StyleVariableResolver(IntFlag):
    Valid = 0
    Invalid = 1
    NotFound = 2

# UnityEngine.UIElements.TextOverflow
class TextOverflow(IntFlag):
    Clip = 0
    Ellipsis = 1

# UnityEngine.UIElements.TextOverflowPosition
class TextOverflowPosition(IntFlag):
    End = 0
    Start = 1
    Middle = 2

# UnityEngine.UIElements.TimeUnit
class TimeUnit(IntFlag):
    Second = 0
    Millisecond = 1

# UnityEngine.UIElements.TransformOriginOffset
class TransformOriginOffset(IntFlag):
    Left = 1
    Right = 2
    Top = 3
    Bottom = 4
    Center = 5

# UnityEngine.UIElements.TrickleDown
class TrickleDown(IntFlag):
    NoTrickleDown = 0
    TrickleDown = 1

# UnityEngine.UIElements.TwoPaneSplitViewOrientation
class TwoPaneSplitViewOrientation(IntFlag):
    Horizontal = 0
    Vertical = 1

# UnityEngine.UIElements.UIDocument
class UIDocument(IntFlag):
    Dynamic = 0
    Fixed = 1

# UnityEngine.UIElements.UsageHints
class UsageHints(IntFlag):
    NONE = 0
    DynamicTransform = 1
    GroupTransform = 2
    MaskContainer = 4
    DynamicColor = 8

# UnityEngine.UIElements.UxmlAttributeDescription
class UxmlAttributeDescription(IntFlag):
    NONE = 0
    Optional = 1
    Prohibited = 2
    Required = 3

# UnityEngine.UIElements.UxmlSerializedData
class UxmlSerializedData(IntFlag):
    Ignore = 0
    OverriddenInUxml = 1
    DefaultValue = 2

# UnityEngine.UIElements.VersionChangeType
class VersionChangeType(IntFlag):
    Bindings = 1
    ViewData = 2
    Hierarchy = 4
    Layout = 8
    StyleSheet = 16
    Styles = 32
    Overflow = 64
    BorderRadius = 128
    BorderWidth = 256
    Transform = 512
    Size = 1024
    Repaint = 2048
    Opacity = 4096
    Color = 8192
    RenderHints = 16384
    TransitionProperty = 32768
    EventCallbackCategories = 65536
    DisableRendering = 131072
    BindingRegistration = 262144
    DataSource = 524288
    Picking = 1048576

# UnityEngine.UIElements.Visibility
class Visibility(IntFlag):
    Visible = 0
    Hidden = 1

# UnityEngine.UIElements.VisualElement
class VisualElement(IntFlag):
    Undefined = 0
    Exactly = 1
    AtMost = 2

# UnityEngine.UIElements.VisualElement
class VisualElement(IntFlag):
    NONE = 0
    NoColorConversion = 1
    LinearToGamma = 2
    GammaToLinear = 3

# UnityEngine.UIElements.VisualElementFlags
class VisualElementFlags(IntFlag):
    WorldTransformDirty = 1
    WorldTransformInverseDirty = 2
    WorldClipDirty = 4
    BoundingBoxDirty = 8
    WorldBoundingBoxDirty = 16
    EventInterestParentCategoriesDirty = 32
    LayoutManual = 64
    CompositeRoot = 128
    RequireMeasureFunction = 256
    EnableViewDataPersistence = 512
    DisableClipping = 1024
    NeedsAttachToPanelEvent = 2048
    HierarchyDisplayed = 4096
    StyleInitialized = 8192
    DisableRendering = 16384
    Needs3DBounds = 32768
    LocalBounds3DDirty = 65536
    DetachedDataSource = 131072
    PointerCapture = 262144
    ReceivesHierarchyGeometryChangedEvents = 524288
    BoundingBoxDirtiedSinceLastLayoutPass = 1048576
    Init = 196671

# UnityEngine.UIElements.VisualElementFocusRing
class VisualElementFocusRing(IntFlag):
    ChildOrder = 0
    PositionXY = 1
    PositionYX = 2

# UnityEngine.UIElements.VisualTreeUpdatePhase
class VisualTreeUpdatePhase(IntFlag):
    Bindings = 0
    DataBinding = 1
    Animation = 2
    Styles = 3
    Layout = 4
    TransformClip = 5
    Repaint = 6
    Count = 7

# UnityEngine.UIElements.WhiteSpace
class WhiteSpace(IntFlag):
    Normal = 0
    NoWrap = 1
    Pre = 2
    PreWrap = 3

# UnityEngine.UIElements.Wrap
class Wrap(IntFlag):
    NoWrap = 0
    Wrap = 1
    WrapReverse = 2

