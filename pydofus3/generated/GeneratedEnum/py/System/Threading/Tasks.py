from enum import IntFlag

# System.Threading.Tasks.AsyncCausalityStatus
class AsyncCausalityStatus(IntFlag):
    Started = 0
    Completed = 1
    Canceled = 2
    Error = 3

# System.Threading.Tasks.CausalityRelation
class CausalityRelation(IntFlag):
    AssignDelegate = 0
    Join = 1
    Choice = 2
    Cancel = 3
    Error = 4

# System.Threading.Tasks.CausalitySynchronousWork
class CausalitySynchronousWork(IntFlag):
    CompletionNotification = 0
    ProgressNotification = 1
    Execution = 2

# System.Threading.Tasks.CausalityTraceLevel
class CausalityTraceLevel(IntFlag):
    Required = 0
    Important = 1
    Verbose = 2

# System.Threading.Tasks.InternalTaskOptions
class InternalTaskOptions(IntFlag):
    NONE = 0
    InternalOptionsMask = 65280
    ContinuationTask = 512
    PromiseTask = 1024
    LazyCancellation = 4096
    QueuedByRuntime = 8192
    DoNotDispose = 16384

# System.Threading.Tasks.ParallelEtwProvider
class ParallelEtwProvider(IntFlag):
    ParallelInvoke = 1
    ParallelFor = 2
    ParallelForEach = 3

# System.Threading.Tasks.TaskContinuationOptions
class TaskContinuationOptions(IntFlag):
    NONE = 0
    PreferFairness = 1
    LongRunning = 2
    AttachedToParent = 4
    DenyChildAttach = 8
    HideScheduler = 16
    LazyCancellation = 32
    RunContinuationsAsynchronously = 64
    NotOnRanToCompletion = 65536
    NotOnFaulted = 131072
    NotOnCanceled = 262144
    OnlyOnRanToCompletion = 393216
    OnlyOnFaulted = 327680
    OnlyOnCanceled = 196608
    ExecuteSynchronously = 524288

# System.Threading.Tasks.TaskCreationOptions
class TaskCreationOptions(IntFlag):
    NONE = 0
    PreferFairness = 1
    LongRunning = 2
    AttachedToParent = 4
    DenyChildAttach = 8
    HideScheduler = 16
    RunContinuationsAsynchronously = 64

# System.Threading.Tasks.TaskStatus
class TaskStatus(IntFlag):
    Created = 0
    WaitingForActivation = 1
    WaitingToRun = 2
    Running = 3
    WaitingForChildrenToComplete = 4
    RanToCompletion = 5
    Canceled = 6
    Faulted = 7

