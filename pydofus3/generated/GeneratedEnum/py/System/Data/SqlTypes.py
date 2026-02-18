from enum import IntFlag

# System.Data.SqlTypes.EComparison
class EComparison(IntFlag):
    LT = 0
    LE = 1
    EQ = 2
    GE = 3
    GT = 4
    NE = 5

# System.Data.SqlTypes.SqlBytesCharsState
class SqlBytesCharsState(IntFlag):
    Null = 0
    Buffer = 1
    Stream = 3

# System.Data.SqlTypes.SqlCompareOptions
class SqlCompareOptions(IntFlag):
    NONE = 0
    IgnoreCase = 1
    IgnoreNonSpace = 2
    IgnoreKanaType = 8
    IgnoreWidth = 16
    BinarySort = 32768
    BinarySort2 = 16384

