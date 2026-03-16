from enum import IntEnum

class RequestedCertificate:
	class Choice(IntEnum):
		Certificate = -1
		PublicKeyCertificate = 0
		AttributeCertificate = 1

