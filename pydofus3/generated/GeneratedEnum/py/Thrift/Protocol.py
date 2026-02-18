from enum import IntFlag

# Thrift.Protocol.TMessageType
class TMessageType(IntFlag):
    Call = 1
    Reply = 2
    Exception = 3
    Oneway = 4

# Thrift.Protocol.TType
class TType(IntFlag):
    Stop = 0
    Void = 1
    Bool = 2
    Byte = 3
    Double = 4
    I16 = 6
    I32 = 8
    I64 = 10
    String = 11
    Struct = 12
    Map = 13
    Set = 14
    List = 15

