from enum import IntEnum

class ApiTypes(IntEnum):
	UNKNOWN = 0
	OVR = 1
	REWIRED = 2
	LUA = 3

class COLLISION_EVENT(IntEnum):
	COLLISION_ENTER = 0
	COLLISION_STAY = 1
	COLLISION_EXIT = 2

class CollisionDetectionMode(IntEnum):
	Discrete = 0
	Continuous = 1
	ContinuousDynamic = 2
	ContinuousSpeculative = 3

class CoordinateConversion(IntEnum):
	None_ = 0
	Local = 1
	WorldToScreenPoint = 2
	WorldToViewportPoint = 3
	ScreenToWorldPoint = 4
	ScreenToViewportPoint = 5
	ViewportToWorldPoint = 6
	ViewportToScreenPoint = 7

class FileCollisionOption(IntEnum):
	ThrowErrorIfExists = 0
	UseExisting = 1
	GenerateUniqueName = 2

class InputMapOutputTypes(IntEnum):
	DEBUG = 0
	JSON = 1
	MULTI = 2

class LogLevel(IntEnum):
	DISABLED = 0
	ERROR = 1
	WARN = 2
	INFO = 4
	DEBUG = 8
	TRACE = 16

class LogType(IntEnum):
	Error = 0
	Assert = 1
	Warning = 2
	Log = 3
	Exception = 4

class MouseButtons(IntEnum):
	LEFT = 0
	RIGHT = 1
	MIDDLE = 2

class ObjectListFilter(IntEnum):
	UNTAGGED = 0
	TAGGED = 1
	ALL = 2

class PhysicMaterialCombine(IntEnum):
	Average = 0
	Multiply = 1
	Minimum = 2
	Maximum = 3

class RigidbodyConstraints(IntEnum):
	None_ = 0
	FreezePositionX = 2
	FreezePositionY = 4
	FreezePositionZ = 8
	FreezePosition = 14
	FreezeRotationX = 16
	FreezeRotationY = 32
	FreezeRotationZ = 64
	FreezeRotation = 112
	FreezeAll = 126

class RigidbodyInterpolation(IntEnum):
	None_ = 0
	Interpolate = 1
	Extrapolate = 2

class ScriptExecutionMode(IntEnum):
	Once = 0
	EveryFrame = 1
	EveryNthFrames = 2

class Space(IntEnum):
	World = 0
	Self = 1

class UNREAL_HIT_EVENT(IntEnum):
	HIT_EVENT = 0
	OVERLAP_BEGIN_EVENT = 1
	OVERLAP_END_EVENT = 2

class XRDeviceModes(IntEnum):
	NONE = 1
	CONTROLLER = 2
	HAND = 4

