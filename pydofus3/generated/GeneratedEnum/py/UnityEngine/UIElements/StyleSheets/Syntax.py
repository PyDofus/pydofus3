from enum import IntFlag

# UnityEngine.UIElements.StyleSheets.Syntax.DataType
class DataType(IntFlag):
    NONE = 0
    Number = 1
    Integer = 2
    Length = 3
    Percentage = 4
    Color = 5
    Resource = 6
    Url = 7
    Time = 8
    Angle = 9
    CustomIdent = 10

# UnityEngine.UIElements.StyleSheets.Syntax.ExpressionCombinator
class ExpressionCombinator(IntFlag):
    NONE = 0
    Or = 1
    OrOr = 2
    AndAnd = 3
    Juxtaposition = 4
    Group = 5

# UnityEngine.UIElements.StyleSheets.Syntax.ExpressionMultiplierType
class ExpressionMultiplierType(IntFlag):
    NONE = 0
    ZeroOrMore = 1
    OneOrMore = 2
    ZeroOrOne = 3
    Ranges = 4
    OneOrMoreComma = 5
    GroupAtLeastOne = 6

# UnityEngine.UIElements.StyleSheets.Syntax.ExpressionType
class ExpressionType(IntFlag):
    Unknown = 0
    Data = 1
    Keyword = 2
    Combinator = 3

# UnityEngine.UIElements.StyleSheets.Syntax.StyleSyntaxTokenType
class StyleSyntaxTokenType(IntFlag):
    Unknown = 0
    String = 1
    Number = 2
    Space = 3
    SingleBar = 4
    DoubleBar = 5
    DoubleAmpersand = 6
    Comma = 7
    SingleQuote = 8
    Asterisk = 9
    Plus = 10
    QuestionMark = 11
    HashMark = 12
    ExclamationPoint = 13
    OpenBracket = 14
    CloseBracket = 15
    OpenBrace = 16
    CloseBrace = 17
    LessThan = 18
    GreaterThan = 19
    End = 20

