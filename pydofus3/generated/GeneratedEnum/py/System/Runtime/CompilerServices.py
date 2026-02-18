from enum import IntFlag

# System.Runtime.CompilerServices.CompilationRelaxations
class CompilationRelaxations(IntFlag):
    NoStringInterning = 8

# System.Runtime.CompilerServices.LoadHint
class LoadHint(IntFlag):
    Default = 0
    Always = 1
    Sometimes = 2

# System.Runtime.CompilerServices.MethodCodeType
class MethodCodeType(IntFlag):
    IL = 0
    Native = 1
    OPTIL = 2
    Runtime = 3

# System.Runtime.CompilerServices.MethodImplOptions
class MethodImplOptions(IntFlag):
    Unmanaged = 4
    ForwardRef = 16
    PreserveSig = 128
    InternalCall = 4096
    Synchronized = 32
    NoInlining = 8
    AggressiveInlining = 256
    NoOptimization = 64
    SecurityMitigations = 1024

