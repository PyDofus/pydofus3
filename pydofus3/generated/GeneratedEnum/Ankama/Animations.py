from enum import IntEnum
from enum import IntFlag

class Animation:
	class hds(IntFlag):
		eclj = 0
		eclk = 1
		ecll = 2
		eclm = 4
		ecln = 8
		eclo = 16
		eclp = 32
		eclq = 64
		eclr = 128

	class hdt(IntEnum):
		ecls = 0
		eclt = 1
		eclu = 2
		eclv = 4
		eclw = 8
		eclx = 16
		ecly = 32
		eclz = 64
		ecma = 128

	class hdu(IntFlag):
		ecmb = 0
		ecmc = 1
		ecmd = 2
		ecme = 4

	class hdv(IntEnum):
		ecmf = 0
		ecmg = 1
		ecmh = 2
		ecmi = 3
		ecmj = 4
		ecmk = 5
		ecml = 6
		ecmm = 7
		ecmn = 8
		ecmo = 9
		ecmp = 10
		ecmq = 11
		ecmr = 12
		ecms = 13
		ecmt = 14
		ecmu = 15

class Animator2D:
	class hdx(IntEnum):
		ecnf = 0
		ecng = 1
		ecnh = 2

