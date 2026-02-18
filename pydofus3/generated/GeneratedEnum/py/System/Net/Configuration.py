from enum import IntFlag

# System.Net.Configuration.UnicodeDecodingConformance
class UnicodeDecodingConformance(IntFlag):
    Auto = 0
    Strict = 1
    Compat = 2
    Loose = 3

# System.Net.Configuration.UnicodeEncodingConformance
class UnicodeEncodingConformance(IntFlag):
    Auto = 0
    Strict = 1
    Compat = 2

