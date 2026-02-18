from enum import IntFlag

# Core.UILogic.Components.AnswerType
class AnswerType(IntFlag):
    NONE = 0
    RepeatedQuest = 1
    Quest = 2
    QuestBack = 3
    Fight = 4

# Core.UILogic.Components.BaseGridView
class BaseGridView(IntFlag):
    KeepCurrentScrollPosition = 0
    ScrollToBeginning = 1

# Core.UILogic.Components.BaseProgressBar
class BaseProgressBar(IntFlag):
    large = 0
    small = 1

# Core.UILogic.Components.BaseProgressBar
class BaseProgressBar(IntFlag):
    horizontal = 0
    vertical = 1

# Core.UILogic.Components.BaseProgressBar
class BaseProgressBar(IntFlag):
    custom = 0
    primary = 1
    green = 2
    red = 3
    orange = 4
    grey = 5
    purple = 6

# Core.UILogic.Components.DofusChatTextField
class DofusChatTextField(IntFlag):
    NONE = 0
    Title = 1
    Upper = 2

# Core.UILogic.Components.DofusLabel
class DofusLabel(IntFlag):
    NONE = 0
    Title = 1
    Upper = 2

# Core.UILogic.Components.MagneticDragWindow
class MagneticDragWindow(IntFlag):
    LeftToRight = 0
    RightToLeft = 1
    TopToBottom = 2
    BottomToTop = 3

# Core.UILogic.Components.ResizableWindow
class ResizableWindow(IntFlag):
    NONE = 0
    Top = 1
    Bottom = 2
    Left = 3
    Right = 4
    Custom = 5

# Core.UILogic.Components.ResizeHandler
class ResizeHandler(IntFlag):
    BottomRight = 0
    BottomLeft = 1
    TopLeft = 2
    TopRight = 3
    Right = 4
    Left = 5
    Bottom = 6
    Top = 7

