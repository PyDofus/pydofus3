from enum import IntEnum

class PerformanceCounter(IntEnum):
	AstCreation = 0
	Compilation = 1
	Execution = 2
	AdaptersCompilation = 3
	LastValue = 4

class PerformanceCounterType(IntEnum):
	MemoryBytes = 0
	TimeMilliseconds = 1

