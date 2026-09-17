from enum import IntEnum

class HandshakeState(IntEnum):
	NOT_STARTED = 0
	OPEN = 1
	SENT = 2
	DONE = 3

