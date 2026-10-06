from enum import IntEnum
from enum import IntFlag

class Animation:
	class hbc(IntFlag):
		ebcx = 0
		ebcy = 1
		ebcz = 2
		ebda = 4
		ebdb = 8
		ebdc = 16
		ebdd = 32
		ebde = 64
		ebdf = 128

	class hbd(IntEnum):
		ebdg = 0
		ebdh = 1
		ebdi = 2
		ebdj = 4
		ebdk = 8
		ebdl = 16
		ebdm = 32
		ebdn = 64
		ebdo = 128

	class hbe(IntFlag):
		ebdp = 0
		ebdq = 1
		ebdr = 2
		ebds = 4

	class hbf(IntEnum):
		ebdt = 0
		ebdu = 1
		ebdv = 2
		ebdw = 3
		ebdx = 4
		ebdy = 5
		ebdz = 6
		ebea = 7
		ebeb = 8
		ebec = 9
		ebed = 10
		ebee = 11
		ebef = 12
		ebeg = 13
		ebeh = 14
		ebei = 15

class Animator2D:
	class hbh(IntEnum):
		ebet = 0
		ebeu = 1
		ebev = 2

