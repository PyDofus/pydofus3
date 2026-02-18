from enum import IntFlag

# System.Net.Security.AuthenticationLevel
class AuthenticationLevel(IntFlag):
    NONE = 0
    MutualAuthRequested = 1
    MutualAuthRequired = 2

# System.Net.Security.EncryptionPolicy
class EncryptionPolicy(IntFlag):
    RequireEncryption = 0
    AllowNoEncryption = 1
    NoEncryption = 2

# System.Net.Security.SslPolicyErrors
class SslPolicyErrors(IntFlag):
    NONE = 0
    RemoteCertificateNotAvailable = 1
    RemoteCertificateNameMismatch = 2
    RemoteCertificateChainErrors = 4

