from enum import IntFlag

# System.Globalization.CalendarId
class CalendarId(IntFlag):
    UNINITIALIZED_VALUE = 0
    GREGORIAN = 1
    GREGORIAN_US = 2
    JAPAN = 3
    TAIWAN = 4
    KOREA = 5
    HIJRI = 6
    THAI = 7
    HEBREW = 8
    GREGORIAN_ME_FRENCH = 9
    GREGORIAN_ARABIC = 10
    GREGORIAN_XLIT_ENGLISH = 11
    GREGORIAN_XLIT_FRENCH = 12
    JULIAN = 13
    JAPANESELUNISOLAR = 14
    CHINESELUNISOLAR = 15
    SAKA = 16
    LUNAR_ETO_CHN = 17
    LUNAR_ETO_KOR = 18
    LUNAR_ETO_ROKUYOU = 19
    KOREANLUNISOLAR = 20
    TAIWANLUNISOLAR = 21
    PERSIAN = 22
    UMALQURA = 23
    LAST_CALENDAR = 23

# System.Globalization.CompareOptions
class CompareOptions(IntFlag):
    NONE = 0
    IgnoreCase = 1
    IgnoreNonSpace = 2
    IgnoreSymbols = 4
    IgnoreKanaType = 8
    IgnoreWidth = 16
    OrdinalIgnoreCase = 268435456
    StringSort = 536870912
    Ordinal = 1073741824

# System.Globalization.CultureTypes
class CultureTypes(IntFlag):
    NeutralCultures = 1
    SpecificCultures = 2
    InstalledWin32Cultures = 4
    AllCultures = 7
    UserCustomCulture = 8
    ReplacementCultures = 16
    WindowsOnlyCultures = 32
    FrameworkCultures = 64

# System.Globalization.DateTimeFormatFlags
class DateTimeFormatFlags(IntFlag):
    NONE = 0
    UseGenitiveMonth = 1
    UseLeapYearMonth = 2
    UseSpacesInMonthNames = 4
    UseHebrewRule = 8
    UseSpacesInDayNames = 16
    UseDigitPrefixInTokens = 32
    NotInitialized = -1

# System.Globalization.DateTimeFormatInfoScanner
class DateTimeFormatInfoScanner(IntFlag):
    NONE = 0
    FoundYearPatternFlag = 1
    FoundMonthPatternFlag = 2
    FoundDayPatternFlag = 4
    FoundYMDPatternFlag = 7

# System.Globalization.DateTimeStyles
class DateTimeStyles(IntFlag):
    NONE = 0
    AllowLeadingWhite = 1
    AllowTrailingWhite = 2
    AllowInnerWhite = 4
    AllowWhiteSpaces = 7
    NoCurrentDateDefault = 8
    AdjustToUniversal = 16
    AssumeLocal = 32
    AssumeUniversal = 64
    RoundtripKind = 128

# System.Globalization.FORMATFLAGS
class FORMATFLAGS(IntFlag):
    NONE = 0
    UseGenitiveMonth = 1
    UseLeapYearMonth = 2
    UseSpacesInMonthNames = 4
    UseHebrewParsing = 8
    UseSpacesInDayNames = 16
    UseDigitPrefixInTokens = 32

# System.Globalization.GregorianCalendarTypes
class GregorianCalendarTypes(IntFlag):
    Localized = 1
    USEnglish = 2
    MiddleEastFrench = 9
    Arabic = 10
    TransliteratedEnglish = 11
    TransliteratedFrench = 12

# System.Globalization.HebrewNumber
class HebrewNumber(IntFlag):
    Invalid = -1
    Digit400 = 0
    Digit200_300 = 1
    Digit100 = 2
    Digit10 = 3
    Digit1 = 4
    Digit6_7 = 5
    Digit7 = 6
    Digit9 = 7
    SingleQuote = 8
    DoubleQuote = 9

# System.Globalization.HebrewNumber
class HebrewNumber(IntFlag):
    _err = -1
    Start = 0
    S400 = 1
    S400_400 = 2
    S400_X00 = 3
    S400_X0 = 4
    X00_DQ = 5
    S400_X00_X0 = 6
    X0_DQ = 7
    X = 8
    X0 = 9
    X00 = 10
    S400_DQ = 11
    S400_400_DQ = 12
    S400_400_100 = 13
    S9 = 14
    X00_S9 = 15
    S9_DQ = 16
    END = 100

# System.Globalization.HebrewNumberParsingState
class HebrewNumberParsingState(IntFlag):
    InvalidHebrewNumber = 0
    NotHebrewDigit = 1
    FoundEndOfHebrewNumber = 2
    ContinueParsing = 3

# System.Globalization.MonthNameStyles
class MonthNameStyles(IntFlag):
    Regular = 0
    Genitive = 1
    LeapYear = 2

# System.Globalization.NumberStyles
class NumberStyles(IntFlag):
    NONE = 0
    AllowLeadingWhite = 1
    AllowTrailingWhite = 2
    AllowLeadingSign = 4
    AllowTrailingSign = 8
    AllowParentheses = 16
    AllowDecimalPoint = 32
    AllowThousands = 64
    AllowExponent = 128
    AllowCurrencySymbol = 256
    AllowHexSpecifier = 512
    Integer = 7
    HexNumber = 515
    Number = 111
    Float = 167
    Currency = 383
    Any = 511

# System.Globalization.TimeSpanFormat
class TimeSpanFormat(IntFlag):
    NONE = 0
    Minimum = 1
    Full = 2

# System.Globalization.TimeSpanParse
class TimeSpanParse(IntFlag):
    NONE = 0
    ArgumentNull = 1
    Format = 2
    FormatWithParameter = 3
    Overflow = 4

# System.Globalization.TimeSpanParse
class TimeSpanParse(IntFlag):
    NONE = 0
    Invariant = 1
    Localized = 2
    RequireFull = 4
    Any = 3

# System.Globalization.TimeSpanParse
class TimeSpanParse(IntFlag):
    NONE = 0
    End = 1
    Num = 2
    Sep = 3
    NumOverflow = 4

# System.Globalization.UnicodeCategory
class UnicodeCategory(IntFlag):
    UppercaseLetter = 0
    LowercaseLetter = 1
    TitlecaseLetter = 2
    ModifierLetter = 3
    OtherLetter = 4
    NonSpacingMark = 5
    SpacingCombiningMark = 6
    EnclosingMark = 7
    DecimalDigitNumber = 8
    LetterNumber = 9
    OtherNumber = 10
    SpaceSeparator = 11
    LineSeparator = 12
    ParagraphSeparator = 13
    Control = 14
    Format = 15
    Surrogate = 16
    PrivateUse = 17
    ConnectorPunctuation = 18
    DashPunctuation = 19
    OpenPunctuation = 20
    ClosePunctuation = 21
    InitialQuotePunctuation = 22
    FinalQuotePunctuation = 23
    OtherPunctuation = 24
    MathSymbol = 25
    CurrencySymbol = 26
    ModifierSymbol = 27
    OtherSymbol = 28
    OtherNotAssigned = 29

