from enum import IntEnum
from enum import IntFlag

class AtlasPopulationMode(IntEnum):
	Static = 0
	Dynamic = 1
	DynamicOS = 2

class CaretPosition(IntEnum):
	None_ = 0
	Left = 1
	Right = 2

class ColorMode(IntEnum):
	Single = 0
	HorizontalGradient = 1
	VerticalGradient = 2
	FourCornersGradient = 3

class ColorTween:
	class ColorTweenMode(IntEnum):
		All = 0
		RGB = 1
		Alpha = 2

class Compute_DistanceTransform_EventTypes(IntEnum):
	Processing = 0
	Completed = 1

class FontFeatureLookupFlags(IntFlag):
	None_ = 0
	IgnoreLigatures = 4
	IgnoreSpacingAdjustments = 256

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

class FontWeight(IntEnum):
	Thin = 100
	ExtraLight = 200
	Light = 300
	Regular = 400
	Medium = 500
	SemiBold = 600
	Bold = 700
	Heavy = 800
	Black = 900

class HorizontalAlignmentOptions(IntEnum):
	Left = 1
	Center = 2
	Right = 4
	Justified = 8
	Flush = 16
	Geometry = 32

class MarkupTag(IntEnum):
	PADDING = -2144568463
	GRADIENT = -1999759898
	FONT_WEIGHT = -1889896162
	SLASH_GRADIENT = -1854491959
	ACTION = -1827519330
	SLASH_MARGIN = -1649644303
	SLASH_MONOSPACE = -1638865562
	CENTER = -1591113269
	CHARACTER_SPACE = -1584382009
	INDENT = -1514123076
	LOWERCASE = -1506899689
	SLASH_INDENT = -1496889389
	SLASH_LOWERCASE = -1451284584
	SLASH_CHARACTER_SPACE = -1394426712
	MARGIN = -1355614050
	MONOSPACE = -1340221943
	PURPLE = -1250222130
	STYLENAME = -1207081936
	SLASH_ACTION = -1187217679
	NORMAL = -1183493901
	ORANGE = -1108587920
	SLASH_MATERIAL = -1100708252
	ROTATE = -1000007783
	SPRITE = -991527447
	SLASH_TABLE = -979118220
	YELLOW = -882444668
	LINE_INDENT = -844305121
	LINE_HEIGHT = -799081892
	SLASH_ALLCAPS = -797437649
	SMALLCAPS = -766062114
	SLASH_ROTATE = -764695562
	SLASH_FONT_WEIGHT = -757976431
	DEFAULT = -620974005
	SLASH_UPPERCASE = -582368199
	MARGIN_RIGHT = -447416589
	NO_PARSE = -408011596
	UPPERCASE = -305409418
	SLASH_NO_PARSE = -294095813
	MARGIN_LEFT = -272933656
	SLASH_VERTICAL_OFFSET = -11107948
	PERCENTAGE = 37
	PLUS = 43
	MINUS = 45
	A = 65
	BOLD = 66
	ITALIC = 73
	STRIKETHROUGH = 83
	UNDERLINE = 85
	PLUS_PERCENTAGE = 1454
	MINUS_PERCENTAGE = 1512
	SLASH_ITALIC = 1606
	SLASH_BOLD = 1613
	SLASH_A = 1614
	SLASH_UNDERLINE = 1626
	SLASH_STRIKETHROUGH = 1628
	EM = 2216
	BR = 2256
	CR = 2289
	PX = 2568
	MINUS_EM = 46789
	MINUS_PX = 47461
	PLUS_EM = 49091
	PLUS_PX = 49507
	PCT = 85031
	POSITION = 85420
	RED = 91635
	SUBSCRIPT = 92132
	SUPERSCRIPT = 92150
	SHY = 92674
	ZWJ = 99623
	MINUS_PCT = 1567082
	PLUS_PCT = 1634348
	SLASH_SUBSCRIPT = 1770219
	SLASH_SUPERSCRIPT = 1770233
	SLASH_POSITION = 1777699
	ANIM = 2283339
	BLUE = 2457214
	HREF = 2535353
	FONT = 2586451
	FRAC = 2598518
	GREY = 2638345
	LIGA = 2655971
	LINK = 2656128
	LEFT = 2660507
	MARK = 2699125
	PAGE = 2808691
	NO_BREAK = 2856657
	NONE = 2857034
	NBSP = 2869039
	NAME = 2875623
	TRUE = 2932022
	TINT = 2960519
	SIZE = 3061285
	ZWSP = 3288238
	TR = 5862467
	TD = 5862485
	TH = 5862489
	SLASH_NO_BREAK = 57477502
	SLASH_MARK = 57644506
	SLASH_LINK = 57686191
	SLASH_LIGA = 57686604
	SLASH_FONT = 57747708
	SLASH_FRAC = 57774681
	SLASH_SIZE = 58429962
	SLASH_PAGE = 58683868
	ALIGN = 75138797
	ALPHA = 75165780
	ANGLE = 75347905
	BLACK = 81074727
	COLOR = 81999901
	CLASS = 82115566
	INDEX = 84268030
	FALSE = 85422813
	FLUSH = 85552164
	GREEN = 87065851
	SLASH_LINE_INDENT = 93886352
	RIGHT = 99937376
	SPACE = 100083556
	STYLE = 100252951
	SCALE = 100553336
	WHITE = 105680263
	WIDTH = 105793766
	SLASH_TR = 193346060
	SLASH_TH = 193346070
	SLASH_TD = 193346074
	SLASH_SMALLCAPS = 199921873
	SLASH_LINE_HEIGHT = 200452819
	ALLCAPS = 218273952
	TABLE = 226476955
	LIGHTBLUE = 341063360
	DUOSPACE = 582810522
	NOTDEF = 612146780
	FAMILYNAME = 704251153
	JUSTIFIED = 817091359
	MATERIAL = 825491659
	REGULAR = 1291372090
	INVALID = 1585415185
	SLASH_COLOR = 1909026194
	SLASH_ALIGN = 1916026786
	SLASH_WIDTH = 1923459625
	SLASH_STYLE = 1927738392
	SLASH_SPACE = 1927873067
	SLASH_SCALE = 1928413879
	VERTICAL_OFFSET = 1952379995

class MaskingOffsetMode(IntEnum):
	Percentage = 0
	Pixel = 1

class MaskingTypes(IntEnum):
	MaskOff = 0
	MaskHard = 1
	MaskSoft = 2

class TagUnitType(IntEnum):
	Pixels = 0
	FontUnits = 1
	Percentage = 2

class TagValueType(IntEnum):
	None_ = 0
	NumericalValue = 1
	StringValue = 2
	ColorValue = 4

class TextAlignmentOptions(IntEnum):
	TopLeft = 257
	Top = 258
	TopRight = 260
	TopJustified = 264
	TopFlush = 272
	TopGeoAligned = 288
	Left = 513
	Center = 514
	Right = 516
	Justified = 520
	Flush = 528
	CenterGeoAligned = 544
	BottomLeft = 1025
	Bottom = 1026
	BottomRight = 1028
	BottomJustified = 1032
	BottomFlush = 1040
	BottomGeoAligned = 1056
	BaselineLeft = 2049
	Baseline = 2050
	BaselineRight = 2052
	BaselineJustified = 2056
	BaselineFlush = 2064
	BaselineGeoAligned = 2080
	MidlineLeft = 4097
	Midline = 4098
	MidlineRight = 4100
	MidlineJustified = 4104
	MidlineFlush = 4112
	MidlineGeoAligned = 4128
	CaplineLeft = 8193
	Capline = 8194
	CaplineRight = 8196
	CaplineJustified = 8200
	CaplineFlush = 8208
	CaplineGeoAligned = 8224
	Converted = 65535

class TextContainerAnchors(IntEnum):
	TopLeft = 0
	Top = 1
	TopRight = 2
	Left = 3
	Middle = 4
	Right = 5
	BottomLeft = 6
	Bottom = 7
	BottomRight = 8
	Custom = 9

class TextElementType(IntEnum):
	Character = 1
	Sprite = 2

class TextOverflowModes(IntEnum):
	Overflow = 0
	Ellipsis = 1
	Masking = 2
	Truncate = 3
	ScrollRect = 4
	Page = 5
	Linked = 6

class TextProcessingElementType(IntEnum):
	Undefined = 0
	TextCharacterElement = 1
	TextMarkupElement = 2

class TextRenderFlags(IntEnum):
	DontRender = 0
	Render = 255

class TextureMappingOptions(IntEnum):
	Character = 0
	Line = 1
	Paragraph = 2
	MatchAspect = 3

class TextWrappingModes(IntEnum):
	NoWrap = 0
	Normal = 1
	PreserveWhitespace = 2
	PreserveWhitespaceNoWrap = 3

class TMP_Compatibility:
	class AnchorPositions(IntEnum):
		TopLeft = 0
		Top = 1
		TopRight = 2
		Left = 3
		Center = 4
		Right = 5
		BottomLeft = 6
		Bottom = 7
		BottomRight = 8
		BaseLine = 9
		None_ = 10

class TMP_InputField:
	class ContentType(IntEnum):
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

	class InputType(IntEnum):
		Standard = 0
		AutoCorrect = 1
		Password = 2

	class CharacterValidation(IntEnum):
		None_ = 0
		Digit = 1
		Integer = 2
		Decimal = 3
		Alphanumeric = 4
		Name = 5
		Regex = 6
		EmailAddress = 7
		CustomValidator = 8

	class LineType(IntEnum):
		SingleLine = 0
		MultiLineSubmit = 1
		MultiLineNewline = 2

	class EditState(IntEnum):
		Continue = 0
		Finish = 1

class TMP_Text:
	class TextInputSources(IntEnum):
		TextInputBox = 0
		SetText = 1
		SetTextArray = 2
		TextString = 3

class TMP_TextElementType(IntEnum):
	Character = 0
	Sprite = 1

class TMP_VertexDataUpdateFlags(IntEnum):
	None_ = 0
	Vertices = 1
	Uv0 = 2
	Uv2 = 4
	Uv4 = 8
	Colors32 = 16
	All = 255

class VertexSortingOrder(IntEnum):
	Normal = 0
	Reverse = 1

class VerticalAlignmentOptions(IntEnum):
	Top = 256
	Middle = 512
	Bottom = 1024
	Baseline = 2048
	Geometry = 4096
	Capline = 8192

