from enum import IntFlag

# UnityEngine.UIElements.Layout.LayoutAlign
class LayoutAlign(IntFlag):
    Auto = 0
    FlexStart = 1
    Center = 2
    FlexEnd = 3
    Stretch = 4
    Baseline = 5
    SpaceBetween = 6
    SpaceAround = 7

# UnityEngine.UIElements.Layout.LayoutConfigDataType
class LayoutConfigDataType(IntFlag):
    Config = 0

# UnityEngine.UIElements.Layout.LayoutDirection
class LayoutDirection(IntFlag):
    Inherit = 0
    LTR = 1
    RTL = 2

# UnityEngine.UIElements.Layout.LayoutDisplay
class LayoutDisplay(IntFlag):
    Flex = 0
    NONE = 1

# UnityEngine.UIElements.Layout.LayoutEdge
class LayoutEdge(IntFlag):
    Left = 0
    Top = 1
    Right = 2
    Bottom = 3
    Start = 4
    End = 5
    Horizontal = 6
    Vertical = 7
    All = 8

# UnityEngine.UIElements.Layout.LayoutFlexDirection
class LayoutFlexDirection(IntFlag):
    Column = 0
    ColumnReverse = 1
    Row = 2
    RowReverse = 3

# UnityEngine.UIElements.Layout.LayoutJustify
class LayoutJustify(IntFlag):
    FlexStart = 0
    Center = 1
    FlexEnd = 2
    SpaceBetween = 3
    SpaceAround = 4
    SpaceEvenly = 5

# UnityEngine.UIElements.Layout.LayoutMeasureMode
class LayoutMeasureMode(IntFlag):
    Undefined = 0
    Exactly = 1
    AtMost = 2
    Invalid = -1

# UnityEngine.UIElements.Layout.LayoutNative
class LayoutNative(IntFlag):
    NONE = 0
    Error = 1
    Measure = 2
    Layout = 3
    CacheUsage = 4
    BeginLayout = 5
    EndLayout = 6

# UnityEngine.UIElements.Layout.LayoutNodeData
class LayoutNodeData(IntFlag):
    IsDirty = 1
    HasNewLayout = 4
    DependsOnParentSize = 64
    Fixed = 8
    MinViolation = 16
    MaxViolation = 32

# UnityEngine.UIElements.Layout.LayoutNodeDataType
class LayoutNodeDataType(IntFlag):
    Node = 0
    Style = 1
    Computed = 2
    Cache = 3

# UnityEngine.UIElements.Layout.LayoutOverflow
class LayoutOverflow(IntFlag):
    Visible = 0
    Hidden = 1
    Scroll = 2

# UnityEngine.UIElements.Layout.LayoutPositionType
class LayoutPositionType(IntFlag):
    Relative = 0
    Absolute = 1

# UnityEngine.UIElements.Layout.LayoutUnit
class LayoutUnit(IntFlag):
    Undefined = 0
    Point = 1
    Percent = 2
    Auto = 3

# UnityEngine.UIElements.Layout.LayoutWrap
class LayoutWrap(IntFlag):
    NoWrap = 0
    Wrap = 1
    WrapReverse = 2

