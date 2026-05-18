from enum import IntEnum

class Transition:
	class fpd(IntEnum):
		dplo = 0
		dplp = 1
		dplq = 2
		dplr = 4
		dpls = 8
		dplt = 16
		dplu = 32
		dplv = 64

