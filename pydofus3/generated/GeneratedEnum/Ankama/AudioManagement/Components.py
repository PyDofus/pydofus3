from enum import IntEnum
from enum import IntFlag

class AudioEventContext:
	class Flags(IntFlag):
		None_ = 0
		Valid = 1
		OneShot = 2
		Restart = 4
		RespondsToMusicMarkers = 8

class AudioEventLoader:
	class InitializationState(IntEnum):
		None_ = 0
		Loading = 1
		Loaded = 2
		Error = 3

