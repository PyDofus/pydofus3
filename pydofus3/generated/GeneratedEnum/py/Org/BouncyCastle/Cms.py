from enum import IntFlag

# Org.BouncyCastle.Cms.CmsAttributeTableParameter
class CmsAttributeTableParameter(IntFlag):
    ContentType = 0
    Digest = 1
    Signature = 2
    DigestAlgorithmIdentifier = 3

