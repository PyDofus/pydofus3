from enum import IntEnum

class ServerState(IntEnum):
	Ready = 0
	Start = 1
	ShuttingDown = 2
	Stop = 3

