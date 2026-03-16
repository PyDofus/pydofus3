from enum import IntEnum

class EmbeddedChannel:
	class State(IntEnum):
		Open = 0
		Active = 1
		Closed = 2

class SingleThreadedEmbeddedChannel:
	class State(IntEnum):
		Open = 0
		Active = 1
		Closed = 2

