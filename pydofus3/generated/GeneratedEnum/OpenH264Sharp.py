from enum import IntEnum

class RuntimePlatform(IntEnum):
	Win64 = 0
	Linux64 = 1
	MacArm64 = 2
	MacX64 = 3
	AndroidArm64 = 4
	Static = 5
	Unknown = 6

