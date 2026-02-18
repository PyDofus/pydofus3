from enum import IntFlag

# Org.BouncyCastle.Asn1.IsisMtt.Ocsp.RequestedCertificate
class RequestedCertificate(IntFlag):
    Certificate = -1
    PublicKeyCertificate = 0
    AttributeCertificate = 1

