from enum import IntFlag

# UnityEngine.TextCore.GlyphClassDefinitionType
class GlyphClassDefinitionType(IntFlag):
    Undefined = 0
    Base = 1
    Ligature = 2
    Mark = 3
    Component = 4

# UnityEngine.TextCore.HorizontalAlignment
class HorizontalAlignment(IntFlag):
    Left = 0
    Center = 1
    Right = 2
    Justified = 3

# UnityEngine.TextCore.LanguageDirection
class LanguageDirection(IntFlag):
    LTR = 0
    RTL = 1

# UnityEngine.TextCore.OTL_FeatureTag
class OTL_FeatureTag(IntFlag):
    kern = 1801810542
    liga = 1818847073
    mark = 1835102827
    mkmk = 1835756907

# UnityEngine.TextCore.RichTextTagParser
class RichTextTagParser(IntFlag):
    Hyperlink = 0
    Align = 1
    AllCaps = 2
    Alpha = 3
    Bold = 4
    Br = 5
    Color = 6
    CSpace = 7
    Font = 8
    FontWeight = 9
    Italic = 10
    Indent = 11
    LineHeight = 12
    LineIndent = 13
    Link = 14
    Lowercase = 15
    Mark = 16
    Mspace = 17
    NoBr = 18
    NoParse = 19
    Strikethrough = 20
    Size = 21
    SmallCaps = 22
    Space = 23
    Sprite = 24
    Style = 25
    Subscript = 26
    Superscript = 27
    Underline = 28
    Uppercase = 29
    Unknown = 30

# UnityEngine.TextCore.RichTextTagParser
class RichTextTagParser(IntFlag):
    NONE = 0
    NumericalValue = 1
    StringValue = 2
    ColorValue = 4

# UnityEngine.TextCore.RichTextTagParser
class RichTextTagParser(IntFlag):
    Pixels = 0
    FontUnits = 1
    Percentage = 2

# UnityEngine.TextCore.TextOverflow
class TextOverflow(IntFlag):
    Clip = 0
    Ellipsis = 1

# UnityEngine.TextCore.VerticalAlignment
class VerticalAlignment(IntFlag):
    Top = 0
    Middle = 1
    Bottom = 2

# UnityEngine.TextCore.WhiteSpace
class WhiteSpace(IntFlag):
    Normal = 0
    NoWrap = 1
    Pre = 2
    PreWrap = 3

