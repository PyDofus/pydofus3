from enum import IntFlag

# UnityEngine.TextCore.Text.AtlasPopulationMode
class AtlasPopulationMode(IntFlag):
    Static = 0
    Dynamic = 1
    DynamicOS = 2

# UnityEngine.TextCore.Text.ColorGradientMode
class ColorGradientMode(IntFlag):
    Single = 0
    HorizontalGradient = 1
    VerticalGradient = 2
    FourCornersGradient = 3

# UnityEngine.TextCore.Text.FontStyles
class FontStyles(IntFlag):
    Normal = 0
    Bold = 1
    Italic = 2
    Underline = 4
    LowerCase = 8
    UpperCase = 16
    SmallCaps = 32
    Strikethrough = 64
    Superscript = 128
    Subscript = 256
    Highlight = 512

# UnityEngine.TextCore.Text.MarkupTag
class MarkupTag(IntFlag):
    BOLD = 66
    SLASH_BOLD = 1613
    ITALIC = 73
    SLASH_ITALIC = 1606
    UNDERLINE = 85
    SLASH_UNDERLINE = 1626
    STRIKETHROUGH = 83
    SLASH_STRIKETHROUGH = 1628
    MARK = 2699125
    SLASH_MARK = 57644506
    SUBSCRIPT = 92132
    SLASH_SUBSCRIPT = 1770219
    SUPERSCRIPT = 92150
    SLASH_SUPERSCRIPT = 1770233
    COLOR = 81999901
    SLASH_COLOR = 1909026194
    ALPHA = 75165780
    A = 65
    SLASH_A = 1614
    SIZE = 3061285
    SLASH_SIZE = 58429962
    SPRITE = -991527447
    NO_BREAK = 2856657
    SLASH_NO_BREAK = 57477502
    STYLE = 100252951
    SLASH_STYLE = 1927738392
    FONT = 2586451
    SLASH_FONT = 57747708
    SLASH_MATERIAL = -1100708252
    LINK = 2656128
    SLASH_LINK = 57686191
    FONT_WEIGHT = -1889896162
    SLASH_FONT_WEIGHT = -757976431
    NO_PARSE = -408011596
    SLASH_NO_PARSE = -294095813
    POSITION = 85420
    SLASH_POSITION = 1777699
    VERTICAL_OFFSET = 1952379995
    SLASH_VERTICAL_OFFSET = -11107948
    SPACE = 100083556
    SLASH_SPACE = 1927873067
    PAGE = 2808691
    SLASH_PAGE = 58683868
    ALIGN = 75138797
    SLASH_ALIGN = 1916026786
    WIDTH = 105793766
    SLASH_WIDTH = 1923459625
    GRADIENT = -1999759898
    SLASH_GRADIENT = -1854491959
    CHARACTER_SPACE = -1584382009
    SLASH_CHARACTER_SPACE = -1394426712
    MONOSPACE = -1340221943
    SLASH_MONOSPACE = -1638865562
    CLASS = 82115566
    INDENT = -1514123076
    SLASH_INDENT = -1496889389
    LINE_INDENT = -844305121
    SLASH_LINE_INDENT = 93886352
    MARGIN = -1355614050
    SLASH_MARGIN = -1649644303
    MARGIN_LEFT = -272933656
    MARGIN_RIGHT = -447416589
    LINE_HEIGHT = -799081892
    SLASH_LINE_HEIGHT = 200452819
    ACTION = -1827519330
    SLASH_ACTION = -1187217679
    SCALE = 100553336
    SLASH_SCALE = 1928413879
    ROTATE = -1000007783
    SLASH_ROTATE = -764695562
    TABLE = 226476955
    SLASH_TABLE = -979118220
    TH = 5862489
    SLASH_TH = 193346070
    TR = 5862467
    SLASH_TR = 193346060
    TD = 5862485
    SLASH_TD = 193346074
    LOWERCASE = -1506899689
    SLASH_LOWERCASE = -1451284584
    ALLCAPS = 218273952
    SLASH_ALLCAPS = -797437649
    UPPERCASE = -305409418
    SLASH_UPPERCASE = -582368199
    SMALLCAPS = -766062114
    SLASH_SMALLCAPS = 199921873
    LIGA = 2655971
    SLASH_LIGA = 57686604
    FRAC = 2598518
    SLASH_FRAC = 57774681
    NAME = 2875623
    INDEX = 84268030
    TINT = 2960519
    ANIM = 2283339
    MATERIAL = 825491659
    HREF = 2535353
    ANGLE = 75347905
    PADDING = -2144568463
    FAMILYNAME = 704251153
    STYLENAME = -1207081936
    DUOSPACE = 582810522
    RED = 91635
    GREEN = 87065851
    BLUE = 2457214
    YELLOW = -882444668
    ORANGE = -1108587920
    BLACK = 81074727
    WHITE = 105680263
    PURPLE = -1250222130
    GREY = 2638345
    LIGHTBLUE = 341063360
    TEAL = 2947772
    CYAN = 2504597
    DARKBLUE = -1960309918
    FUCHSIA = -1002715645
    SILVER = -960329321
    BROWN = 81017702
    MAROON = -1355621936
    OLIVE = 95492953
    NAVY = 2876352
    AQUA = 2284356
    MAGENTA = -1812576107
    TRANSPARENT = -1014785338
    LIME = 2656045
    BR = 2256
    CR = 2289
    ZWSP = 3288238
    ZWJ = 99623
    NBSP = 2869039
    SHY = 92674
    LEFT = 2660507
    RIGHT = 99937376
    CENTER = -1591113269
    JUSTIFIED = 817091359
    FLUSH = 85552164
    NONE = 2857034
    PLUS = 43
    MINUS = 45
    PX = 2568
    PLUS_PX = 49507
    MINUS_PX = 47461
    EM = 2216
    PLUS_EM = 49091
    MINUS_EM = 46789
    PCT = 85031
    PLUS_PCT = 1634348
    MINUS_PCT = 1567082
    PERCENTAGE = 37
    PLUS_PERCENTAGE = 1454
    MINUS_PERCENTAGE = 1512
    TRUE = 2932022
    FALSE = 85422813
    INVALID = 1585415185
    NOTDEF = 612146780
    NORMAL = -1183493901
    DEFAULT = -620974005
    REGULAR = 1291372090

# UnityEngine.TextCore.Text.OTL_FeatureTag
class OTL_FeatureTag(IntFlag):
    kern = 1801810542
    liga = 1818847073
    mark = 1835102827
    mkmk = 1835756907

# UnityEngine.TextCore.Text.TagUnitType
class TagUnitType(IntFlag):
    Pixels = 0
    FontUnits = 1
    Percentage = 2

# UnityEngine.TextCore.Text.TagValueType
class TagValueType(IntFlag):
    NONE = 0
    NumericalValue = 1
    StringValue = 2
    ColorValue = 4

# UnityEngine.TextCore.Text.TextAlignment
class TextAlignment(IntFlag):
    TopLeft = 257
    TopCenter = 258
    TopRight = 260
    TopJustified = 264
    TopFlush = 272
    TopGeoAligned = 288
    MiddleLeft = 513
    MiddleCenter = 514
    MiddleRight = 516
    MiddleJustified = 520
    MiddleFlush = 528
    MiddleGeoAligned = 544
    BottomLeft = 1025
    BottomCenter = 1026
    BottomRight = 1028
    BottomJustified = 1032
    BottomFlush = 1040
    BottomGeoAligned = 1056
    BaselineLeft = 2049
    BaselineCenter = 2050
    BaselineRight = 2052
    BaselineJustified = 2056
    BaselineFlush = 2064
    BaselineGeoAligned = 2080
    MidlineLeft = 4097
    MidlineCenter = 4098
    MidlineRight = 4100
    MidlineJustified = 4104
    MidlineFlush = 4112
    MidlineGeoAligned = 4128
    CaplineLeft = 8193
    CaplineCenter = 8194
    CaplineRight = 8196
    CaplineJustified = 8200
    CaplineFlush = 8208
    CaplineGeoAligned = 8224

# UnityEngine.TextCore.Text.TextElementType
class TextElementType(IntFlag):
    Character = 1
    Sprite = 2

# UnityEngine.TextCore.Text.TextFontWeight
class TextFontWeight(IntFlag):
    Thin = 100
    ExtraLight = 200
    Light = 300
    Regular = 400
    Medium = 500
    SemiBold = 600
    Bold = 700
    Heavy = 800
    Black = 900

# UnityEngine.TextCore.Text.TextOverflowMode
class TextOverflowMode(IntFlag):
    Overflow = 0
    Ellipsis = 1
    Masking = 2
    Truncate = 3
    ScrollRect = 4
    Linked = 6

# UnityEngine.TextCore.Text.TextProcessingElementType
class TextProcessingElementType(IntFlag):
    Undefined = 0
    TextCharacterElement = 1
    TextMarkupElement = 2

# UnityEngine.TextCore.Text.TextWrappingMode
class TextWrappingMode(IntFlag):
    NoWrap = 0
    Normal = 1
    PreserveWhitespace = 2
    PreserveWhitespaceNoWrap = 3

