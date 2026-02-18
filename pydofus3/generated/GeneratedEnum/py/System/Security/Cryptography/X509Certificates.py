from enum import IntFlag

# System.Security.Cryptography.X509Certificates.OpenFlags
class OpenFlags(IntFlag):
    ReadOnly = 0
    ReadWrite = 1
    MaxAllowed = 2
    OpenExistingOnly = 4
    IncludeArchived = 8

# System.Security.Cryptography.X509Certificates.StoreLocation
class StoreLocation(IntFlag):
    CurrentUser = 1
    LocalMachine = 2

# System.Security.Cryptography.X509Certificates.StoreName
class StoreName(IntFlag):
    AddressBook = 1
    AuthRoot = 2
    CertificateAuthority = 3
    Disallowed = 4
    My = 5
    Root = 6
    TrustedPeople = 7
    TrustedPublisher = 8

# System.Security.Cryptography.X509Certificates.X500DistinguishedNameFlags
class X500DistinguishedNameFlags(IntFlag):
    NONE = 0
    Reversed = 1
    UseSemicolons = 16
    DoNotUsePlusSign = 32
    DoNotUseQuotes = 64
    UseCommas = 128
    UseNewLines = 256
    UseUTF8Encoding = 4096
    UseT61Encoding = 8192
    ForceUTF8Encoding = 16384

# System.Security.Cryptography.X509Certificates.X509ChainStatusFlags
class X509ChainStatusFlags(IntFlag):
    NoError = 0
    NotTimeValid = 1
    NotTimeNested = 2
    Revoked = 4
    NotSignatureValid = 8
    NotValidForUsage = 16
    UntrustedRoot = 32
    RevocationStatusUnknown = 64
    Cyclic = 128
    InvalidExtension = 256
    InvalidPolicyConstraints = 512
    InvalidBasicConstraints = 1024
    InvalidNameConstraints = 2048
    HasNotSupportedNameConstraint = 4096
    HasNotDefinedNameConstraint = 8192
    HasNotPermittedNameConstraint = 16384
    HasExcludedNameConstraint = 32768
    PartialChain = 65536
    CtlNotTimeValid = 131072
    CtlNotSignatureValid = 262144
    CtlNotValidForUsage = 524288
    OfflineRevocation = 16777216
    NoIssuanceChainPolicy = 33554432
    ExplicitDistrust = 67108864
    HasNotSupportedCriticalExtension = 134217728
    HasWeakSignature = 1048576

# System.Security.Cryptography.X509Certificates.X509ContentType
class X509ContentType(IntFlag):
    Unknown = 0
    Cert = 1
    SerializedCert = 2
    Pfx = 3
    Pkcs12 = 3
    SerializedStore = 4
    Pkcs7 = 5
    Authenticode = 6

# System.Security.Cryptography.X509Certificates.X509FindType
class X509FindType(IntFlag):
    FindByThumbprint = 0
    FindBySubjectName = 1
    FindBySubjectDistinguishedName = 2
    FindByIssuerName = 3
    FindByIssuerDistinguishedName = 4
    FindBySerialNumber = 5
    FindByTimeValid = 6
    FindByTimeNotYetValid = 7
    FindByTimeExpired = 8
    FindByTemplateName = 9
    FindByApplicationPolicy = 10
    FindByCertificatePolicy = 11
    FindByExtension = 12
    FindByKeyUsage = 13
    FindBySubjectKeyIdentifier = 14

# System.Security.Cryptography.X509Certificates.X509KeyStorageFlags
class X509KeyStorageFlags(IntFlag):
    DefaultKeySet = 0
    UserKeySet = 1
    MachineKeySet = 2
    Exportable = 4
    UserProtected = 8
    PersistKeySet = 16
    EphemeralKeySet = 32

# System.Security.Cryptography.X509Certificates.X509KeyUsageFlags
class X509KeyUsageFlags(IntFlag):
    NONE = 0
    EncipherOnly = 1
    CrlSign = 2
    KeyCertSign = 4
    KeyAgreement = 8
    DataEncipherment = 16
    KeyEncipherment = 32
    NonRepudiation = 64
    DigitalSignature = 128
    DecipherOnly = 32768

# System.Security.Cryptography.X509Certificates.X509NameType
class X509NameType(IntFlag):
    SimpleName = 0
    EmailName = 1
    UpnName = 2
    DnsName = 3
    DnsFromAlternativeName = 4
    UrlName = 5

# System.Security.Cryptography.X509Certificates.X509RevocationFlag
class X509RevocationFlag(IntFlag):
    EndCertificateOnly = 0
    EntireChain = 1
    ExcludeRoot = 2

# System.Security.Cryptography.X509Certificates.X509RevocationMode
class X509RevocationMode(IntFlag):
    NoCheck = 0
    Online = 1
    Offline = 2

# System.Security.Cryptography.X509Certificates.X509SubjectKeyIdentifierHashAlgorithm
class X509SubjectKeyIdentifierHashAlgorithm(IntFlag):
    Sha1 = 0
    ShortSha1 = 1
    CapiSha1 = 2

# System.Security.Cryptography.X509Certificates.X509VerificationFlags
class X509VerificationFlags(IntFlag):
    NoFlag = 0
    IgnoreNotTimeValid = 1
    IgnoreCtlNotTimeValid = 2
    IgnoreNotTimeNested = 4
    IgnoreInvalidBasicConstraints = 8
    AllowUnknownCertificateAuthority = 16
    IgnoreWrongUsage = 32
    IgnoreInvalidName = 64
    IgnoreInvalidPolicy = 128
    IgnoreEndRevocationUnknown = 256
    IgnoreCtlSignerRevocationUnknown = 512
    IgnoreCertificateAuthorityRevocationUnknown = 1024
    IgnoreRootRevocationUnknown = 2048
    AllFlags = 4095

