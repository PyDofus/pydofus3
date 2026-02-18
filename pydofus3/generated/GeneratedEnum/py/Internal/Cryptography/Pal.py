from enum import IntFlag

# Internal.Cryptography.Pal.GeneralNameType
class GeneralNameType(IntFlag):
    OtherName = 0
    Rfc822Name = 1
    Email = 1
    DnsName = 2
    X400Address = 3
    DirectoryName = 4
    EdiPartyName = 5
    UniformResourceIdentifier = 6
    IPAddress = 7
    RegisteredId = 8

