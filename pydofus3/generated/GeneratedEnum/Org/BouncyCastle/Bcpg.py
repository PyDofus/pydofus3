from enum import IntEnum

class CompressionAlgorithmTag(IntEnum):
	Uncompressed = 0
	Zip = 1
	ZLib = 2
	BZip2 = 3

class HashAlgorithmTag(IntEnum):
	MD5 = 1
	Sha1 = 2
	RipeMD160 = 3
	DoubleSha = 4
	MD2 = 5
	Tiger192 = 6
	Haval5pass160 = 7
	Sha256 = 8
	Sha384 = 9
	Sha512 = 10
	Sha224 = 11

class PacketTag(IntEnum):
	Reserved = 0
	PublicKeyEncryptedSession = 1
	Signature = 2
	SymmetricKeyEncryptedSessionKey = 3
	OnePassSignature = 4
	SecretKey = 5
	PublicKey = 6
	SecretSubkey = 7
	CompressedData = 8
	SymmetricKeyEncrypted = 9
	Marker = 10
	LiteralData = 11
	Trust = 12
	UserId = 13
	PublicSubkey = 14
	UserAttribute = 17
	SymmetricEncryptedIntegrityProtected = 18
	ModificationDetectionCode = 19
	Experimental1 = 60
	Experimental2 = 61
	Experimental3 = 62
	Experimental4 = 63

class PublicKeyAlgorithmTag(IntEnum):
	RsaGeneral = 1
	RsaEncrypt = 2
	RsaSign = 3
	ElGamalEncrypt = 16
	Dsa = 17
	EC = 18
	ECDH = 18
	ECDsa = 19
	ElGamalGeneral = 20
	DiffieHellman = 21
	EdDsa = 22
	Experimental_1 = 100
	Experimental_2 = 101
	Experimental_3 = 102
	Experimental_4 = 103
	Experimental_5 = 104
	Experimental_6 = 105
	Experimental_7 = 106
	Experimental_8 = 107
	Experimental_9 = 108
	Experimental_10 = 109
	Experimental_11 = 110

class RevocationKeyTag(IntEnum):
	ClassSensitive = 64
	ClassDefault = 128

class RevocationReasonTag(IntEnum):
	NoReason = 0
	KeySuperseded = 1
	KeyCompromised = 2
	KeyRetired = 3
	UserNoLongerValid = 32

class SignatureSubpacketTag(IntEnum):
	CreationTime = 2
	ExpireTime = 3
	Exportable = 4
	TrustSig = 5
	RegExp = 6
	Revocable = 7
	KeyExpireTime = 9
	Placeholder = 10
	PreferredSymmetricAlgorithms = 11
	RevocationKey = 12
	IssuerKeyId = 16
	NotationData = 20
	PreferredHashAlgorithms = 21
	PreferredCompressionAlgorithms = 22
	KeyServerPreferences = 23
	PreferredKeyServer = 24
	PrimaryUserId = 25
	PolicyUrl = 26
	KeyFlags = 27
	SignerUserId = 28
	RevocationReason = 29
	Features = 30
	SignatureTarget = 31
	EmbeddedSignature = 32

class SymmetricKeyAlgorithmTag(IntEnum):
	Null = 0
	Idea = 1
	TripleDes = 2
	Cast5 = 3
	Blowfish = 4
	Safer = 5
	Des = 6
	Aes128 = 7
	Aes192 = 8
	Aes256 = 9
	Twofish = 10
	Camellia128 = 11
	Camellia192 = 12
	Camellia256 = 13

class UserAttributeSubpacketTag(IntEnum):
	ImageAttribute = 1

