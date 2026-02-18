from enum import IntFlag

# System.Buffers.ArrayPoolEventSource
class ArrayPoolEventSource(IntFlag):
    Pooled = 0
    OverMaximumSize = 1
    PoolExhausted = 2

# System.Buffers.ArrayPoolEventSource
class ArrayPoolEventSource(IntFlag):
    Pooled = 0
    OverMaximumSize = 1
    PoolExhausted = 2

# System.Buffers.OperationStatus
class OperationStatus(IntFlag):
    Done = 0
    DestinationTooSmall = 1
    NeedMoreData = 2
    InvalidData = 3

# System.Buffers.ReadOnlySequence
class ReadOnlySequence(IntFlag):
    MultiSegment = 0
    Array = 1
    MemoryManager = 2
    String = 3
    Empty = 4

# System.Buffers.ReadOnlySequence
class ReadOnlySequence(IntFlag):
    MultiSegment = 0
    Array = 1
    MemoryManager = 2
    String = 3
    Empty = 4

# System.Buffers.TlsOverPerCoreLockedStacksArrayPool
class TlsOverPerCoreLockedStacksArrayPool(IntFlag):
    Low = 0
    Medium = 1
    High = 2

