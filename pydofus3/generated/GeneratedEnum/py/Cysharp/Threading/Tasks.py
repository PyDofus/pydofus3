from enum import IntFlag

# Cysharp.Threading.Tasks.DelayType
class DelayType(IntFlag):
    DeltaTime = 0
    UnscaledDeltaTime = 1
    Realtime = 2

# Cysharp.Threading.Tasks.InjectPlayerLoopTimings
class InjectPlayerLoopTimings(IntFlag):
    All = 65535
    Standard = 30037
    Minimum = 8464
    Initialization = 1
    LastInitialization = 2
    EarlyUpdate = 4
    LastEarlyUpdate = 8
    FixedUpdate = 16
    LastFixedUpdate = 32
    PreUpdate = 64
    LastPreUpdate = 128
    Update = 256
    LastUpdate = 512
    PreLateUpdate = 1024
    LastPreLateUpdate = 2048
    PostLateUpdate = 4096
    LastPostLateUpdate = 8192
    TimeUpdate = 16384
    LastTimeUpdate = 32768

# Cysharp.Threading.Tasks.PlayerLoopTiming
class PlayerLoopTiming(IntFlag):
    Initialization = 0
    LastInitialization = 1
    EarlyUpdate = 2
    LastEarlyUpdate = 3
    FixedUpdate = 4
    LastFixedUpdate = 5
    PreUpdate = 6
    LastPreUpdate = 7
    Update = 8
    LastUpdate = 9
    PreLateUpdate = 10
    LastPreLateUpdate = 11
    PostLateUpdate = 12
    LastPostLateUpdate = 13
    TimeUpdate = 14
    LastTimeUpdate = 15

# Cysharp.Threading.Tasks.UniTaskStatus
class UniTaskStatus(IntFlag):
    Pending = 0
    Succeeded = 1
    Faulted = 2
    Canceled = 3

# Cysharp.Threading.Tasks.WhenEachState
class WhenEachState(IntFlag):
    NotRunning = 0
    Running = 1
    Completed = 2

