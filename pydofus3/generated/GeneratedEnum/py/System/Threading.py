from enum import IntFlag

# System.Threading.EventResetMode
class EventResetMode(IntFlag):
    AutoReset = 0
    ManualReset = 1

# System.Threading.ExecutionContext
class ExecutionContext(IntFlag):
    NONE = 0
    IsNewCapture = 1
    IsFlowSuppressed = 2
    IsPreAllocatedDefault = 4

# System.Threading.ExecutionContext
class ExecutionContext(IntFlag):
    NONE = 0
    IgnoreSyncCtx = 1
    OptimizeDefaultCase = 2

# System.Threading.LazyThreadSafetyMode
class LazyThreadSafetyMode(IntFlag):
    NONE = 0
    PublicationOnly = 1
    ExecutionAndPublication = 2

# System.Threading.LockRecursionPolicy
class LockRecursionPolicy(IntFlag):
    NoRecursion = 0
    SupportsRecursion = 1

# System.Threading.StackCrawlMark
class StackCrawlMark(IntFlag):
    LookForMe = 0
    LookForMyCaller = 1
    LookForMyCallersCaller = 2
    LookForThread = 3

# System.Threading.SynchronizationContextProperties
class SynchronizationContextProperties(IntFlag):
    NONE = 0
    RequireWaitNotification = 1

# System.Threading.ThreadPriority
class ThreadPriority(IntFlag):
    Lowest = 0
    BelowNormal = 1
    Normal = 2
    AboveNormal = 3
    Highest = 4

# System.Threading.ThreadState
class ThreadState(IntFlag):
    Running = 0
    StopRequested = 1
    SuspendRequested = 2
    Background = 4
    Unstarted = 8
    Stopped = 16
    WaitSleepJoin = 32
    Suspended = 64
    AbortRequested = 128
    Aborted = 256

