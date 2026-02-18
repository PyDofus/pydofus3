from enum import IntFlag

# System.Net.Http.Headers.HttpHeaderKind
class HttpHeaderKind(IntFlag):
    NONE = 0
    Request = 1
    Response = 2
    Content = 4

# System.Net.Http.Headers.Token
class Token(IntFlag):
    Error = 0
    End = 1
    Token = 2
    QuotedString = 3
    SeparatorEqual = 4
    SeparatorSemicolon = 5
    SeparatorSlash = 6
    SeparatorDash = 7
    SeparatorComma = 8
    OpenParens = 9

