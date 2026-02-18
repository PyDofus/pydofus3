from enum import IntFlag

# UnityEngine.Bindings.BlittableArrayWrapper
class BlittableArrayWrapper(IntFlag):
    NoUpdateNeeded = 0
    SizeChanged = 1
    DataIsNativePointer = 2
    DataIsNativeOwnedMemory = 3
    DataIsEmpty = 4
    DataIsNull = 5

# UnityEngine.Bindings.CodegenOptions
class CodegenOptions(IntFlag):
    Auto = 0
    Custom = 1
    Force = 2

# UnityEngine.Bindings.StaticAccessorType
class StaticAccessorType(IntFlag):
    Dot = 0
    Arrow = 1
    DoubleColon = 2
    ArrowWithDefaultReturnIfNull = 3

# UnityEngine.Bindings.TargetType
class TargetType(IntFlag):
    Function = 0
    Field = 1

