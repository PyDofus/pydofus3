from enum import IntEnum

class AgentInterface:
	class PlayerSettingsActiveInputHandler(IntEnum):
		Legacy = 0
		New = 1
		Both = 2

