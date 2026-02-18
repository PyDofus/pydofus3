from enum import IntFlag

# System.Reflection.Internal.MemoryBlock
class MemoryBlock(IntFlag):
    Equal = 0
    BytesStartWithText = 1
    TextStartsWithBytes = 2
    Unequal = 3
    Inconclusive = 4

