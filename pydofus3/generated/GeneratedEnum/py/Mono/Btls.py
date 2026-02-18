from enum import IntFlag

# Mono.Btls.MonoBtlsBioMono
class MonoBtlsBioMono(IntFlag):
    Flush = 1

# Mono.Btls.MonoBtlsSslError
class MonoBtlsSslError(IntFlag):
    NONE = 0
    Ssl = 1
    WantRead = 2
    WantWrite = 3
    WantX509Lookup = 4
    Syscall = 5
    ZeroReturn = 6
    WantConnect = 7
    WantAccept = 8
    WantChannelIdLookup = 9
    PendingSession = 11
    PendingCertificate = 12
    WantPrivateKeyOperation = 13

# Mono.Btls.MonoBtlsSslRenegotiateMode
class MonoBtlsSslRenegotiateMode(IntFlag):
    NEVER = 0
    ONCE = 1
    FREELY = 2
    IGNORE = 3

# Mono.Btls.MonoBtlsX509Error
class MonoBtlsX509Error(IntFlag):
    OK = 0
    UNABLE_TO_GET_ISSUER_CERT = 2
    UNABLE_TO_GET_CRL = 3
    UNABLE_TO_DECRYPT_CERT_SIGNATURE = 4
    UNABLE_TO_DECRYPT_CRL_SIGNATURE = 5
    UNABLE_TO_DECODE_ISSUER_PUBLIC_KEY = 6
    CERT_SIGNATURE_FAILURE = 7
    CRL_SIGNATURE_FAILURE = 8
    CERT_NOT_YET_VALID = 9
    CERT_HAS_EXPIRED = 10
    CRL_NOT_YET_VALID = 11
    CRL_HAS_EXPIRED = 12
    ERROR_IN_CERT_NOT_BEFORE_FIELD = 13
    ERROR_IN_CERT_NOT_AFTER_FIELD = 14
    ERROR_IN_CRL_LAST_UPDATE_FIELD = 15
    ERROR_IN_CRL_NEXT_UPDATE_FIELD = 16
    OUT_OF_MEM = 17
    DEPTH_ZERO_SELF_SIGNED_CERT = 18
    SELF_SIGNED_CERT_IN_CHAIN = 19
    UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 20
    UNABLE_TO_VERIFY_LEAF_SIGNATURE = 21
    CERT_CHAIN_TOO_LONG = 22
    CERT_REVOKED = 23
    INVALID_CA = 24
    PATH_LENGTH_EXCEEDED = 25
    INVALID_PURPOSE = 26
    CERT_UNTRUSTED = 27
    CERT_REJECTED = 28
    SUBJECT_ISSUER_MISMATCH = 29
    AKID_SKID_MISMATCH = 30
    AKID_ISSUER_SERIAL_MISMATCH = 31
    KEYUSAGE_NO_CERTSIGN = 32
    UNABLE_TO_GET_CRL_ISSUER = 33
    UNHANDLED_CRITICAL_EXTENSION = 34
    KEYUSAGE_NO_CRL_SIGN = 35
    UNHANDLED_CRITICAL_CRL_EXTENSION = 36
    INVALID_NON_CA = 37
    PROXY_PATH_LENGTH_EXCEEDED = 38
    KEYUSAGE_NO_DIGITAL_SIGNATURE = 39
    PROXY_CERTIFICATES_NOT_ALLOWED = 40
    INVALID_EXTENSION = 41
    INVALID_POLICY_EXTENSION = 42
    NO_EXPLICIT_POLICY = 43
    DIFFERENT_CRL_SCOPE = 44
    UNSUPPORTED_EXTENSION_FEATURE = 45
    UNNESTED_RESOURCE = 46
    PERMITTED_VIOLATION = 47
    EXCLUDED_VIOLATION = 48
    SUBTREE_MINMAX = 49
    UNSUPPORTED_CONSTRAINT_TYPE = 51
    UNSUPPORTED_CONSTRAINT_SYNTAX = 52
    UNSUPPORTED_NAME_SYNTAX = 53
    CRL_PATH_VALIDATION_ERROR = 54
    SUITE_B_INVALID_VERSION = 56
    SUITE_B_INVALID_ALGORITHM = 57
    SUITE_B_INVALID_CURVE = 58
    SUITE_B_INVALID_SIGNATURE_ALGORITHM = 59
    SUITE_B_LOS_NOT_ALLOWED = 60
    SUITE_B_CANNOT_SIGN_P_384_WITH_P_256 = 61
    HOSTNAME_MISMATCH = 62
    EMAIL_MISMATCH = 63
    IP_ADDRESS_MISMATCH = 64
    APPLICATION_VERIFICATION = 50

# Mono.Btls.MonoBtlsX509FileType
class MonoBtlsX509FileType(IntFlag):
    PEM = 1
    ASN1 = 2
    DEFAULT = 3

# Mono.Btls.MonoBtlsX509Format
class MonoBtlsX509Format(IntFlag):
    DER = 1
    PEM = 2

# Mono.Btls.MonoBtlsX509LookupType
class MonoBtlsX509LookupType(IntFlag):
    UNKNOWN = 0
    FILE = 1
    HASH_DIR = 2
    MONO = 3

# Mono.Btls.MonoBtlsX509NameEntryType
class MonoBtlsX509NameEntryType(IntFlag):
    Unknown = 0
    CountryName = 1
    OrganizationName = 2
    OrganizationalUnitName = 3
    CommonName = 4
    LocalityName = 5
    StateOrProvinceName = 6
    StreetAddress = 7
    SerialNumber = 8
    DomainComponent = 9
    UserId = 10
    Email = 11
    DnQualifier = 12
    Title = 13
    Surname = 14
    GivenName = 15
    Initial = 16

# Mono.Btls.MonoBtlsX509StoreType
class MonoBtlsX509StoreType(IntFlag):
    Custom = 0
    MachineTrustedRoots = 1
    MachineIntermediateCA = 2
    MachineUntrusted = 3
    UserTrustedRoots = 4
    UserIntermediateCA = 5
    UserUntrusted = 6

# Mono.Btls.MonoBtlsX509TrustKind
class MonoBtlsX509TrustKind(IntFlag):
    DEFAULT = 0
    TRUST_CLIENT = 1
    TRUST_SERVER = 2
    TRUST_ALL = 4
    REJECT_CLIENT = 32
    REJECT_SERVER = 64
    REJECT_ALL = 128

