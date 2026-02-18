from enum import IntFlag

# Org.BouncyCastle.Asn1.IsisMtt.X509.DeclarationOfMajority
class DeclarationOfMajority(IntFlag):
    NotYoungerThan = 0
    FullAgeAtCountry = 1
    DateOfBirth = 2

