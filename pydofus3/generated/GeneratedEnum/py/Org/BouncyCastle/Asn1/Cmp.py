from enum import IntFlag

# Org.BouncyCastle.Asn1.Cmp.PkiStatus
class PkiStatus(IntFlag):
    Granted = 0
    GrantedWithMods = 1
    Rejection = 2
    Waiting = 3
    RevocationWarning = 4
    RevocationNotification = 5
    KeyUpdateWarning = 6

