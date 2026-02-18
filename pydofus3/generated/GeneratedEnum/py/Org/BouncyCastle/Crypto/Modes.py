from enum import IntFlag

# Org.BouncyCastle.Crypto.Modes.ChaCha20Poly1305
class ChaCha20Poly1305(IntFlag):
    Uninitialized = 0
    EncInit = 1
    EncAad = 2
    EncData = 3
    EncFinal = 4
    DecInit = 5
    DecAad = 6
    DecData = 7
    DecFinal = 8

# Org.BouncyCastle.Crypto.Modes.EaxBlockCipher
class EaxBlockCipher(IntFlag):
    N = 0
    H = 1
    C = 2

