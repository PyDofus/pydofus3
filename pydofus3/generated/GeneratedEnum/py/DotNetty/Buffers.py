from enum import IntFlag

# DotNetty.Buffers.ByteOrder
class ByteOrder(IntFlag):
    LittleEndian = 0
    BigEndian = 1

# DotNetty.Buffers.SizeClass
class SizeClass(IntFlag):
    Tiny = 0
    Small = 1
    Normal = 2

