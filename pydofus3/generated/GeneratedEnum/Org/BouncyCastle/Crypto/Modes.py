from enum import IntEnum

class ChaCha20Poly1305:
	class State(IntEnum):
		Uninitialized = 0
		EncInit = 1
		EncAad = 2
		EncData = 3
		EncFinal = 4
		DecInit = 5
		DecAad = 6
		DecData = 7
		DecFinal = 8

class EaxBlockCipher:
	class Tag(IntEnum):
		N = 0
		H = 1
		C = 2

