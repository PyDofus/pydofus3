from enum import IntEnum
from enum import IntFlag

class Animation:
	class grz(IntFlag):
		dtic = 0
		dtid = 1
		dtie = 2
		dtif = 4
		dtig = 8
		dtih = 16
		dtii = 32
		dtij = 64
		dtik = 128

	class gsa(IntEnum):
		dtil = 0
		dtim = 1
		dtin = 2
		dtio = 4
		dtip = 8
		dtiq = 16
		dtir = 32
		dtis = 64
		dtit = 128

	class gsb(IntFlag):
		dtiu = 0
		dtiv = 1
		dtiw = 2
		dtix = 4

	class gsc(IntEnum):
		dtiy = 0
		dtiz = 1
		dtja = 2
		dtjb = 3
		dtjc = 4
		dtjd = 5
		dtje = 6
		dtjf = 7
		dtjg = 8
		dtjh = 9
		dtji = 10
		dtjj = 11
		dtjk = 12
		dtjl = 13
		dtjm = 14
		dtjn = 15

class Animator2D:
	class gse(IntEnum):
		dtjy = 0
		dtjz = 1
		dtka = 2

