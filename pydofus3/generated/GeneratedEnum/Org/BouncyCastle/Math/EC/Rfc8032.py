from enum import IntEnum

class Ed25519:
	class Algorithm(IntEnum):
		Ed25519 = 0
		Ed25519ctx = 1
		Ed25519ph = 2

class Ed448:
	class Algorithm(IntEnum):
		Ed448 = 0
		Ed448ph = 1

