from enum import IntFlag

# Org.BouncyCastle.Math.EC.Rfc8032.Ed25519
class Ed25519(IntFlag):
    Ed25519 = 0
    Ed25519ctx = 1
    Ed25519ph = 2

# Org.BouncyCastle.Math.EC.Rfc8032.Ed448
class Ed448(IntFlag):
    Ed448 = 0
    Ed448ph = 1

