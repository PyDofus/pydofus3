from enum import IntFlag

# Unity.Collections.Allocator
class Allocator(IntFlag):
    Invalid = 0
    NONE = 1
    Temp = 2
    TempJob = 3
    Persistent = 4
    AudioKernel = 5
    Domain = 6
    FirstUserIndex = 64

# Unity.Collections.ConversionError
class ConversionError(IntFlag):
    NONE = 0
    Overflow = 1
    Encoding = 2
    CodePoint = 3

# Unity.Collections.CopyError
class CopyError(IntFlag):
    NONE = 0
    Truncation = 1

# Unity.Collections.FormatError
class FormatError(IntFlag):
    NONE = 0
    Overflow = 1
    BadFormatSpecifier = 2

# Unity.Collections.GenerateTestsForBurstCompatibilityAttribute
class GenerateTestsForBurstCompatibilityAttribute(IntFlag):
    Player = 0
    Editor = 1
    PlayerAndEditor = 2

# Unity.Collections.LeakCategory
class LeakCategory(IntFlag):
    Invalid = 0
    Malloc = 1
    TempJob = 2
    Persistent = 3
    LightProbesQuery = 4
    NativeTest = 5
    MeshDataArray = 6
    TransformAccessArray = 7
    NavMeshQuery = 8

# Unity.Collections.NativeArrayOptions
class NativeArrayOptions(IntFlag):
    UninitializedMemory = 0
    ClearMemory = 1

# Unity.Collections.ParseError
class ParseError(IntFlag):
    NONE = 0
    Syntax = 1
    Overflow = 2
    Underflow = 3

