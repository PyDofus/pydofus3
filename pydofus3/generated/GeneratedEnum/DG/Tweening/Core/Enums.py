from enum import IntEnum

class FilterType(IntEnum):
	All = 0
	TargetOrId = 1
	TargetAndId = 2
	AllExceptTargetsOrIds = 3
	DOGetter = 4

class NestedTweenFailureBehaviour(IntEnum):
	TryToPreserveSequence = 0
	KillWholeSequence = 1

class OperationType(IntEnum):
	Complete = 0
	Despawn = 1
	Flip = 2
	Goto = 3
	Pause = 4
	Play = 5
	PlayForward = 6
	PlayBackwards = 7
	Rewind = 8
	SmoothRewind = 9
	Restart = 10
	TogglePause = 11
	IsTweening = 12

class RewindCallbackMode(IntEnum):
	FireIfPositionChanged = 0
	FireAlwaysWithRewind = 1
	FireAlways = 2

class SpecialStartupMode(IntEnum):
	None_ = 0
	SetLookAt = 1
	SetShake = 2
	SetPunch = 3
	SetCameraShakePosition = 4

class UpdateMode(IntEnum):
	Update = 0
	Goto = 1
	IgnoreOnUpdate = 2
	IgnoreOnComplete = 3

class UpdateNotice(IntEnum):
	None_ = 0
	RewindStep = 1

