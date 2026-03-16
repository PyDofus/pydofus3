from enum import IntEnum
from enum import IntFlag

class AutoPlay(IntEnum):
	None_ = 0
	AutoPlaySequences = 1
	AutoPlayTweeners = 2
	All = 3

class AxisConstraint(IntFlag):
	None_ = 0
	X = 2
	Y = 4
	Z = 8
	W = 16

class Ease(IntEnum):
	Unset = 0
	Linear = 1
	InSine = 2
	OutSine = 3
	InOutSine = 4
	InQuad = 5
	OutQuad = 6
	InOutQuad = 7
	InCubic = 8
	OutCubic = 9
	InOutCubic = 10
	InQuart = 11
	OutQuart = 12
	InOutQuart = 13
	InQuint = 14
	OutQuint = 15
	InOutQuint = 16
	InExpo = 17
	OutExpo = 18
	InOutExpo = 19
	InCirc = 20
	OutCirc = 21
	InOutCirc = 22
	InElastic = 23
	OutElastic = 24
	InOutElastic = 25
	InBack = 26
	OutBack = 27
	InOutBack = 28
	InBounce = 29
	OutBounce = 30
	InOutBounce = 31
	Flash = 32
	InFlash = 33
	OutFlash = 34
	InOutFlash = 35
	INTERNAL_Zero = 36
	INTERNAL_Custom = 37

class LinkBehaviour(IntEnum):
	PauseOnDisable = 0
	PauseOnDisablePlayOnEnable = 1
	PauseOnDisableRestartOnEnable = 2
	PlayOnEnable = 3
	RestartOnEnable = 4
	KillOnDisable = 5
	KillOnDestroy = 6
	CompleteOnDisable = 7
	CompleteAndKillOnDisable = 8
	RewindOnDisable = 9
	RewindAndKillOnDisable = 10

class LogBehaviour(IntEnum):
	Default = 0
	Verbose = 1
	ErrorsOnly = 2

class LoopType(IntEnum):
	Restart = 0
	Yoyo = 1
	Incremental = 2

class PathMode(IntEnum):
	Ignore = 0
	Full3D = 1
	TopDown2D = 2
	Sidescroller2D = 3

class PathType(IntEnum):
	Linear = 0
	CatmullRom = 1
	CubicBezier = 2

class RotateMode(IntEnum):
	Fast = 0
	FastBeyond360 = 1
	WorldAxisAdd = 2
	LocalAxisAdd = 3

class ScrambleMode(IntEnum):
	None_ = 0
	All = 1
	Uppercase = 2
	Lowercase = 3
	Numerals = 4
	Custom = 5

class TweenType(IntEnum):
	Tweener = 0
	Sequence = 1
	Callback = 2

class UpdateType(IntEnum):
	Normal = 0
	Late = 1
	Fixed = 2
	Manual = 3

