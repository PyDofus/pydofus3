from enum import IntFlag

# Core.UILogic.Components.Tooltips.Builder.TextTooltipBuilder
class TextTooltipBuilder(IntFlag):
    Normal = 0
    Malus = 1
    Npc = 2

# Core.UILogic.Components.Tooltips.Builder.TooltipCollisionDodgeDirection
class TooltipCollisionDodgeDirection(IntFlag):
    NONE = 0
    Up = 1
    Right = 2
    Down = 4
    Left = 8
    All = 15

# Core.UILogic.Components.Tooltips.Builder.TooltipPositioning
class TooltipPositioning(IntFlag):
    TopLeft = 0
    TopCenter = 1
    TopRight = 2
    CenterLeft = 3
    Center = 4
    CenterRight = 5
    BottomLeft = 6
    BottomCenter = 7
    BottomRight = 8

