from enum import IntEnum
from enum import IntFlag

class DelayType(IntEnum):
	DeltaTime = 0
	UnscaledDeltaTime = 1
	Realtime = 2

class InjectPlayerLoopTimings(IntFlag):
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
	Minimum = 8464
	TimeUpdate = 16384
	Standard = 30037
	LastTimeUpdate = 32768
	All = 65535

class PlayerLoopTiming(IntEnum):
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

class UniTaskStatus(IntEnum):
	Pending = 0
	Succeeded = 1
	Faulted = 2
	Canceled = 3

class WhenEachState(IntEnum):
	NotRunning = 0
	Running = 1
	Completed = 2

