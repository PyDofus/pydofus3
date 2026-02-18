from enum import IntFlag

# System.Diagnostics.DebuggableAttribute
class DebuggableAttribute(IntFlag):
    NONE = 0
    Default = 1
    DisableOptimizations = 256
    IgnoreSymbolStoreSequencePoints = 2
    EnableEditAndContinue = 4

# System.Diagnostics.DebuggerBrowsableState
class DebuggerBrowsableState(IntFlag):
    Never = 0
    Collapsed = 2
    RootHidden = 3

# System.Diagnostics.EnhancedStackTrace
class EnhancedStackTrace(IntFlag):
    NONE = 0
    ThisProxyField = 52
    HoistedLocalField = 53
    DisplayClassLocalOrField = 56
    LambdaMethod = 98
    LambdaDisplayClass = 99
    StateMachineType = 100
    LocalFunction = 103
    AwaiterField = 117
    HoistedSynthesizedLocalField = 115
    StateMachineStateField = 49
    IteratorCurrentBackingField = 50
    StateMachineParameterProxyField = 51
    ReusableHoistedLocalField = 55
    LambdaCacheField = 57
    FixedBufferField = 101
    AnonymousType = 102
    TransparentIdentifier = 104
    AnonymousTypeField = 105
    AutoPropertyBackingField = 107
    IteratorCurrentThreadIdField = 108
    IteratorFinallyMethod = 109
    BaseMethodWrapper = 110
    AsyncBuilderField = 116
    DynamicCallSiteContainerType = 111
    DynamicCallSiteField = 112

# System.Diagnostics.Process
class Process(IntFlag):
    undefined = 0
    syncMode = 1
    asyncMode = 2

# System.Diagnostics.Process
class Process(IntFlag):
    HaveId = 1
    IsLocal = 2
    IsNt = 4
    HaveProcessInfo = 8
    Exited = 16
    Associated = 32
    IsWin2k = 64
    HaveNtProcessInfo = 12

# System.Diagnostics.ProcessWindowStyle
class ProcessWindowStyle(IntFlag):
    Hidden = 1
    Maximized = 3
    Minimized = 2
    Normal = 0

# System.Diagnostics.StackTrace
class StackTrace(IntFlag):
    Normal = 0
    TrailingNewLine = 1
    NoResourceLookup = 2

# System.Diagnostics.TraceEventType
class TraceEventType(IntFlag):
    Critical = 1
    Error = 2
    Warning = 4
    Information = 8
    Verbose = 16
    Start = 256
    Stop = 512
    Suspend = 1024
    Resume = 2048
    Transfer = 4096

# System.Diagnostics.TraceLevel
class TraceLevel(IntFlag):
    Off = 0
    Error = 1
    Warning = 2
    Info = 3
    Verbose = 4

# System.Diagnostics.TraceOptions
class TraceOptions(IntFlag):
    NONE = 0
    LogicalOperationStack = 1
    DateTime = 2
    Timestamp = 4
    ProcessId = 8
    ThreadId = 16
    Callstack = 32

