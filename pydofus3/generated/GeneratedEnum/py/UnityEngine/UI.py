from enum import IntFlag

# UnityEngine.UI.AspectRatioFitter
class AspectRatioFitter(IntFlag):
    NONE = 0
    WidthControlsHeight = 1
    HeightControlsWidth = 2
    FitInParent = 3
    EnvelopeParent = 4

# UnityEngine.UI.CanvasScaler
class CanvasScaler(IntFlag):
    ConstantPixelSize = 0
    ScaleWithScreenSize = 1
    ConstantPhysicalSize = 2

# UnityEngine.UI.CanvasScaler
class CanvasScaler(IntFlag):
    MatchWidthOrHeight = 0
    Expand = 1
    Shrink = 2

# UnityEngine.UI.CanvasScaler
class CanvasScaler(IntFlag):
    Centimeters = 0
    Millimeters = 1
    Inches = 2
    Points = 3
    Picas = 4

# UnityEngine.UI.CanvasUpdate
class CanvasUpdate(IntFlag):
    Prelayout = 0
    Layout = 1
    PostLayout = 2
    PreRender = 3
    LatePreRender = 4
    MaxUpdateValue = 5

# UnityEngine.UI.ContentSizeFitter
class ContentSizeFitter(IntFlag):
    Unconstrained = 0
    MinSize = 1
    PreferredSize = 2

# UnityEngine.UI.GraphicRaycaster
class GraphicRaycaster(IntFlag):
    NONE = 0
    TwoD = 1
    ThreeD = 2
    All = 3

# UnityEngine.UI.GridLayoutGroup
class GridLayoutGroup(IntFlag):
    UpperLeft = 0
    UpperRight = 1
    LowerLeft = 2
    LowerRight = 3

# UnityEngine.UI.GridLayoutGroup
class GridLayoutGroup(IntFlag):
    Horizontal = 0
    Vertical = 1

# UnityEngine.UI.GridLayoutGroup
class GridLayoutGroup(IntFlag):
    Flexible = 0
    FixedColumnCount = 1
    FixedRowCount = 2

# UnityEngine.UI.Image
class Image(IntFlag):
    Simple = 0
    Sliced = 1
    Tiled = 2
    Filled = 3

# UnityEngine.UI.Image
class Image(IntFlag):
    Horizontal = 0
    Vertical = 1
    Radial90 = 2
    Radial180 = 3
    Radial360 = 4

# UnityEngine.UI.Image
class Image(IntFlag):
    Left = 0
    Right = 1

# UnityEngine.UI.Image
class Image(IntFlag):
    Bottom = 0
    Top = 1

# UnityEngine.UI.Image
class Image(IntFlag):
    BottomLeft = 0
    TopLeft = 1
    TopRight = 2
    BottomRight = 3

# UnityEngine.UI.Image
class Image(IntFlag):
    Bottom = 0
    Left = 1
    Top = 2
    Right = 3

# UnityEngine.UI.Image
class Image(IntFlag):
    Bottom = 0
    Right = 1
    Top = 2
    Left = 3

# UnityEngine.UI.InputField
class InputField(IntFlag):
    Standard = 0
    Autocorrected = 1
    IntegerNumber = 2
    DecimalNumber = 3
    Alphanumeric = 4
    Name = 5
    EmailAddress = 6
    Password = 7
    Pin = 8
    Custom = 9

# UnityEngine.UI.InputField
class InputField(IntFlag):
    Standard = 0
    AutoCorrect = 1
    Password = 2

# UnityEngine.UI.InputField
class InputField(IntFlag):
    NONE = 0
    Integer = 1
    Decimal = 2
    Alphanumeric = 3
    Name = 4
    EmailAddress = 5

# UnityEngine.UI.InputField
class InputField(IntFlag):
    SingleLine = 0
    MultiLineSubmit = 1
    MultiLineNewline = 2

# UnityEngine.UI.InputField
class InputField(IntFlag):
    Continue = 0
    Finish = 1

# UnityEngine.UI.Navigation
class Navigation(IntFlag):
    NONE = 0
    Horizontal = 1
    Vertical = 2
    Automatic = 3
    Explicit = 4

# UnityEngine.UI.ScrollRect
class ScrollRect(IntFlag):
    Unrestricted = 0
    Elastic = 1
    Clamped = 2

# UnityEngine.UI.ScrollRect
class ScrollRect(IntFlag):
    Permanent = 0
    AutoHide = 1
    AutoHideAndExpandViewport = 2

# UnityEngine.UI.Scrollbar
class Scrollbar(IntFlag):
    LeftToRight = 0
    RightToLeft = 1
    BottomToTop = 2
    TopToBottom = 3

# UnityEngine.UI.Scrollbar
class Scrollbar(IntFlag):
    Horizontal = 0
    Vertical = 1

# UnityEngine.UI.Selectable
class Selectable(IntFlag):
    NONE = 0
    ColorTint = 1
    SpriteSwap = 2
    Animation = 3

# UnityEngine.UI.Selectable
class Selectable(IntFlag):
    Normal = 0
    Highlighted = 1
    Pressed = 2
    Selected = 3
    Disabled = 4

# UnityEngine.UI.Slider
class Slider(IntFlag):
    LeftToRight = 0
    RightToLeft = 1
    BottomToTop = 2
    TopToBottom = 3

# UnityEngine.UI.Slider
class Slider(IntFlag):
    Horizontal = 0
    Vertical = 1

# UnityEngine.UI.Toggle
class Toggle(IntFlag):
    NONE = 0
    Fade = 1

