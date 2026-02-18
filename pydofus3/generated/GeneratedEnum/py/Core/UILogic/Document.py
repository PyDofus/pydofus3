from enum import IntFlag

# Core.UILogic.Document.CascadingStyle
class CascadingStyle(IntFlag):
    Null = 0
    NONE = 1
    Square = 2
    Circle = 3
    DecimalLeadingZero = 4

# Core.UILogic.Document.CascadingStyleSheet
class CascadingStyleSheet(IntFlag):
    NONE = 0
    Body = 1
    Paragraph = 2
    Line = 3
    OrderedList = 4

# Core.UILogic.Document.DocumentBase
class DocumentBase(IntFlag):
    Spell = 0
    State = 1
    Item = 2

