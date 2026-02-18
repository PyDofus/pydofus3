from enum import IntFlag

# System.Collections.Generic.InsertionBehavior
class InsertionBehavior(IntFlag):
    NONE = 0
    OverwriteExisting = 1
    ThrowOnExisting = 2

# System.Collections.Generic.NodeColor
class NodeColor(IntFlag):
    Black = 0
    Red = 1

# System.Collections.Generic.TreeRotation
class TreeRotation(IntFlag):
    Left = 0
    LeftRight = 1
    Right = 2
    RightLeft = 3

