from enum import IntEnum

class AgentInterface:
	class PlayerSettingsActiveInputHandler(IntEnum):
		Legacy = 0
		New = 1
		Both = 2

class ObsoleteHandling(IntEnum):
	Ignore = 0
	Penalize = 1
	Exclude = 2
	Warn = 3

