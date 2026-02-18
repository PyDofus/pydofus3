from enum import IntFlag

# Mono.Security.X509.X509ChainStatusFlags
class X509ChainStatusFlags(IntFlag):
    InvalidBasicConstraints = 1024
    NoError = 0
    NotSignatureValid = 8
    NotTimeNested = 2
    NotTimeValid = 1
    PartialChain = 65536
    UntrustedRoot = 32

