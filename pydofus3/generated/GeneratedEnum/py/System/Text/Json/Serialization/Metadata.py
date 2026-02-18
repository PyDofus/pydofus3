from enum import IntFlag

# System.Text.Json.Serialization.Metadata.FSharpCoreReflectionProxy
class FSharpCoreReflectionProxy(IntFlag):
    Unrecognized = 0
    Option = 1
    ValueOption = 2
    List = 3
    Set = 4
    Map = 5
    Record = 6
    Union = 7

# System.Text.Json.Serialization.Metadata.FSharpCoreReflectionProxy
class FSharpCoreReflectionProxy(IntFlag):
    NONE = 0
    SumType = 1
    RecordType = 2
    ObjectType = 3
    Field = 4
    Exception = 5
    Closure = 6
    Module = 7
    UnionCase = 8
    Value = 9
    KindMask = 31
    NonPublicRepresentation = 32

