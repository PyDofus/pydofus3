from enum import IntEnum

class PemUtilities:
	class PemBaseAlg(IntEnum):
		AES_128 = 0
		AES_192 = 1
		AES_256 = 2
		BF = 3
		DES = 4
		DES_EDE = 5
		DES_EDE3 = 6
		RC2 = 7
		RC2_40 = 8
		RC2_64 = 9

	class PemMode(IntEnum):
		CBC = 0
		CFB = 1
		ECB = 2
		OFB = 3

