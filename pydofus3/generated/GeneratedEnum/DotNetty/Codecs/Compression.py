from enum import IntEnum

class JZlib:
	class WrapperType(IntEnum):
		NONE = 0
		ZLIB = 1
		GZIP = 2
		ANY = 3

class ZlibWrapper(IntEnum):
	Zlib = 0
	Gzip = 1
	None_ = 2
	ZlibOrNone = 3

