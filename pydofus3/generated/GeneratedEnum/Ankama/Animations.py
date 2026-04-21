from enum import IntEnum
from enum import IntFlag

class Animation:
	class gsd(IntFlag):
		dtrt = 0
		dtru = 1
		dtrv = 2
		dtrw = 4
		dtrx = 8
		dtry = 16
		dtrz = 32
		dtsa = 64
		dtsb = 128

	class gse(IntEnum):
		dtsc = 0
		dtsd = 1
		dtse = 2
		dtsf = 4
		dtsg = 8
		dtsh = 16
		dtsi = 32
		dtsj = 64
		dtsk = 128

	class gsf(IntFlag):
		dtsl = 0
		dtsm = 1
		dtsn = 2
		dtso = 4

	class gsg(IntEnum):
		dtsp = 0
		dtsq = 1
		dtsr = 2
		dtss = 3
		dtst = 4
		dtsu = 5
		dtsv = 6
		dtsw = 7
		dtsx = 8
		dtsy = 9
		dtsz = 10
		dtta = 11
		dttb = 12
		dttc = 13
		dttd = 14
		dtte = 15

class Animator2D:
	class gsi(IntEnum):
		dttp = 0
		dttq = 1
		dttr = 2

