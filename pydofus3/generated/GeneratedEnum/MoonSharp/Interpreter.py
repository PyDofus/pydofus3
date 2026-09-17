from enum import IntEnum
from enum import IntFlag

class Closure:
	class UpvaluesType(IntEnum):
		None_ = 0
		Environment = 1
		Closure = 2

class ColonOperatorBehaviour(IntEnum):
	TreatAsDot = 0
	TreatAsDotOnUserData = 1
	TreatAsColon = 2

class CoreModules(IntFlag):
	None_ = 0
	GlobalConsts = 1
	TableIterators = 2
	Metatables = 4
	String = 8
	LoadMethods = 16
	Table = 32
	Basic = 64
	ErrorHandling = 128
	Math = 256
	Coroutine = 512
	Bit32 = 1024
	Preset_HardSandbox = 1387
	OS_Time = 2048
	OS_System = 4096
	IO = 8192
	Debug = 16384
	Dynamic = 32768
	Json = 65536
	Preset_SoftSandbox = 102383
	Preset_Default = 114687
	Preset_Complete = 131071

class Coroutine:
	class CoroutineType(IntEnum):
		Coroutine = 0
		ClrCallback = 1
		ClrCallbackDead = 2

class CoroutineState(IntEnum):
	Main = 0
	NotStarted = 1
	Suspended = 2
	ForceSuspended = 3
	Running = 4
	Dead = 5

class DataType(IntEnum):
	Nil = 0
	Void = 1
	Boolean = 2
	Number = 3
	String = 4
	Function = 5
	Table = 6
	Tuple = 7
	UserData = 8
	Thread = 9
	ClrFunction = 10
	TailCallRequest = 11
	YieldRequest = 12

class InteropAccessMode(IntEnum):
	Reflection = 0
	LazyOptimized = 1
	Preoptimized = 2
	BackgroundOptimized = 3
	Hardwired = 4
	HideMembers = 5
	NoReflectionAllowed = 6
	Default = 7

class SymbolRefType(IntEnum):
	Local = 0
	Upvalue = 1
	Global = 2
	DefaultEnv = 3

class TypeValidationFlags(IntFlag):
	None_ = 0
	AllowNil = 1
	AutoConvert = 2
	Default = 2

