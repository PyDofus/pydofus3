from enum import IntFlag

# Org.BouncyCastle.OpenSsl.PemUtilities
class PemUtilities(IntFlag):
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

# Org.BouncyCastle.OpenSsl.PemUtilities
class PemUtilities(IntFlag):
    CBC = 0
    CFB = 1
    ECB = 2
    OFB = 3

