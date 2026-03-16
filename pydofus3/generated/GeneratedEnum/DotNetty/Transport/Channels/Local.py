from enum import IntEnum

class LocalChannel:
	class State(IntEnum):
		Open = 0
		Bound = 1
		Connected = 2
		Closed = 3

