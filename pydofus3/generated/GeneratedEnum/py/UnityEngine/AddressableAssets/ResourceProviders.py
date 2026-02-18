from enum import IntFlag

# UnityEngine.AddressableAssets.ResourceProviders.ContentCatalogProvider
class ContentCatalogProvider(IntFlag):
    Remote = 0
    Cache = 1
    Local = 2
    Count = 3

