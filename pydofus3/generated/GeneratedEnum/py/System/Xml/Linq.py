from enum import IntFlag

# System.Xml.Linq.LoadOptions
class LoadOptions(IntFlag):
    NONE = 0
    PreserveWhitespace = 1
    SetBaseUri = 2
    SetLineInfo = 4

# System.Xml.Linq.SaveOptions
class SaveOptions(IntFlag):
    NONE = 0
    DisableFormatting = 1
    OmitDuplicateNamespaces = 2

# System.Xml.Linq.XObjectChange
class XObjectChange(IntFlag):
    Add = 0
    Remove = 1
    Name = 2
    Value = 3

