from enum import IntFlag

# Core.UILogic.Tutorial.ArrowOrientation
class ArrowOrientation(IntFlag):
    UpperLeftToBottomRight = 0
    TopToBottom = 1
    UpperRightToBottomLeft = 2
    LeftToRight = 3
    RightToLeft = 4
    BottomLeftToUpperRight = 5
    BottomToTop = 6
    BottomRightToUpperLeft = 7

# Core.UILogic.Tutorial.ArrowOrigin
class ArrowOrigin(IntFlag):
    TopLeft = 0
    TopCenter = 1
    TopRight = 2
    CenterLeft = 3
    CenterCenter = 4
    CenterRight = 5
    BottomLeft = 6
    BottomCenter = 7
    BottomRight = 8

