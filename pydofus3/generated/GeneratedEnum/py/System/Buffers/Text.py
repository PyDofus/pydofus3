from enum import IntFlag

# System.Buffers.Text.FormattingHelpers
class FormattingHelpers(IntFlag):
    Uppercase = 0
    Lowercase = 8224

# System.Buffers.Text.SequenceValidity
class SequenceValidity(IntFlag):
    Empty = 0
    WellFormed = 1
    Incomplete = 2
    Invalid = 3

# System.Buffers.Text.Utf8Parser
class Utf8Parser(IntFlag):
    AllowExponent = 1

# System.Buffers.Text.Utf8Parser
class Utf8Parser(IntFlag):
    NoMoreData = 0
    Colon = 1
    Period = 2
    ParseFailure = 3

