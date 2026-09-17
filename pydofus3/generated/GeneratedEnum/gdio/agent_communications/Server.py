from enum import IntEnum

class AbstractConnection:
	class ServerHandShakeState(IntEnum):
		NOT_STARTED = 0
		STARTED = 1
		COMPLETE = 2

