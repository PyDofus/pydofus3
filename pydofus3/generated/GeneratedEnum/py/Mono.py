from enum import IntFlag

# Mono.CertificateImportFlags
class CertificateImportFlags(IntFlag):
    NONE = 0
    DisableNativeBackend = 1
    DisableAutomaticFallback = 2

