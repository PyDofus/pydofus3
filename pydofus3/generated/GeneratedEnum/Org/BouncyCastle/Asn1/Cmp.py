from enum import IntEnum

class PkiStatus(IntEnum):
	Granted = 0
	GrantedWithMods = 1
	Rejection = 2
	Waiting = 3
	RevocationWarning = 4
	RevocationNotification = 5
	KeyUpdateWarning = 6

