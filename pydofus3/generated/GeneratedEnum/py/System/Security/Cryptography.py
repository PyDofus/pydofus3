from enum import IntFlag

# System.Security.Cryptography.AsnDecodeStatus
class AsnDecodeStatus(IntFlag):
    NotDecoded = -1
    Ok = 0
    BadAsn = 1
    BadTag = 2
    BadLength = 3
    InformationNotAvailable = 4

# System.Security.Cryptography.CipherMode
class CipherMode(IntFlag):
    CBC = 1
    ECB = 2
    OFB = 3
    CFB = 4
    CTS = 5

# System.Security.Cryptography.CryptoStreamMode
class CryptoStreamMode(IntFlag):
    Read = 0
    Write = 1

# System.Security.Cryptography.CspProviderFlags
class CspProviderFlags(IntFlag):
    NoFlags = 0
    UseMachineKeyStore = 1
    UseDefaultKeyContainer = 2
    UseNonExportableKey = 4
    UseExistingKey = 8
    UseArchivableKey = 16
    UseUserProtectedKey = 32
    NoPrompt = 64
    CreateEphemeralKey = 128

# System.Security.Cryptography.DerSequenceReader
class DerSequenceReader(IntFlag):
    Boolean = 1
    Integer = 2
    BitString = 3
    OctetString = 4
    Null = 5
    ObjectIdentifier = 6
    UTF8String = 12
    Sequence = 16
    Set = 17
    PrintableString = 19
    T61String = 20
    IA5String = 22
    UTCTime = 23
    GeneralizedTime = 24
    BMPString = 30

# System.Security.Cryptography.OidGroup
class OidGroup(IntFlag):
    All = 0
    HashAlgorithm = 1
    EncryptionAlgorithm = 2
    PublicKeyAlgorithm = 3
    SignatureAlgorithm = 4
    Attribute = 5
    ExtensionOrAttribute = 6
    EnhancedKeyUsage = 7
    Policy = 8
    Template = 9
    KeyDerivationFunction = 10

# System.Security.Cryptography.PaddingMode
class PaddingMode(IntFlag):
    NONE = 1
    PKCS7 = 2
    Zeros = 3
    ANSIX923 = 4
    ISO10126 = 5

# System.Security.Cryptography.RijndaelManagedTransformMode
class RijndaelManagedTransformMode(IntFlag):
    Encrypt = 0
    Decrypt = 1

