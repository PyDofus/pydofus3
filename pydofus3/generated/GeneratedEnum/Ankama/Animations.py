from enum import IntEnum
from enum import IntFlag

class Animation:
	class hbi(IntFlag):
		eatv = 0
		eatw = 1
		eatx = 2
		eaty = 4
		eatz = 8
		eaua = 16
		eaub = 32
		eauc = 64
		eaud = 128

	class hbj(IntEnum):
		eaue = 0
		eauf = 1
		eaug = 2
		eauh = 4
		eaui = 8
		eauj = 16
		eauk = 32
		eaul = 64
		eaum = 128

	class hbk(IntFlag):
		eaun = 0
		eauo = 1
		eaup = 2
		eauq = 4

	class hbl(IntEnum):
		eaur = 0
		eaus = 1
		eaut = 2
		eauu = 3
		eauv = 4
		eauw = 5
		eaux = 6
		eauy = 7
		eauz = 8
		eava = 9
		eavb = 10
		eavc = 11
		eavd = 12
		eave = 13
		eavf = 14
		eavg = 15

class Animator2D:
	class hbn(IntEnum):
		eavr = 0
		eavs = 1
		eavt = 2

