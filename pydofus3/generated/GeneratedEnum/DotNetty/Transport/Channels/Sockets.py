from enum import IntFlag

class AbstractSocketChannel:
	class StateFlags(IntFlag):
		Open = 1
		ReadScheduled = 2
		WriteScheduled = 4
		Active = 8

