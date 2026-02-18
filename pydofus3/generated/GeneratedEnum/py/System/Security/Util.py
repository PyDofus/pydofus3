from enum import IntFlag

# System.Security.Util.Tokenizer
class Tokenizer(IntFlag):
    UnicodeByteArray = 0
    UTF8ByteArray = 1
    ASCIIByteArray = 2
    CharArray = 3
    String = 4
    NestedStrings = 5
    Other = 6

