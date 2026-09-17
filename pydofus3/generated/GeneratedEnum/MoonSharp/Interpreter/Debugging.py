from enum import IntEnum
from enum import IntFlag

class DebuggerAction:
	class ActionType(IntEnum):
		ByteCodeStepIn = 0
		ByteCodeStepOver = 1
		ByteCodeStepOut = 2
		StepIn = 3
		StepOver = 4
		StepOut = 5
		Run = 6
		ToggleBreakpoint = 7
		SetBreakpoint = 8
		ClearBreakpoint = 9
		ResetBreakpoints = 10
		Refresh = 11
		HardRefresh = 12
		None_ = 13

class DebuggerCaps(IntFlag):
	CanDebugSourceCode = 1
	CanDebugByteCode = 2
	HasLineBasedBreakpoints = 4

class WatchType(IntEnum):
	Watches = 0
	VStack = 1
	CallStack = 2
	Coroutines = 3
	Locals = 4
	Threads = 5
	MaxValue = 6

