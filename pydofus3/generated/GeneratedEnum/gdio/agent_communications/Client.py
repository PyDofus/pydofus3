from enum import IntEnum

class GDioClient:
	class ClientHandShakeState(IntEnum):
		NOT_STARTED = 0
		CLIENT_INFORMATION_SENT = 1
		COMPLETE = 2

