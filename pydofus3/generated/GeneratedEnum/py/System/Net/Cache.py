from enum import IntFlag

# System.Net.Cache.RequestCacheLevel
class RequestCacheLevel(IntFlag):
    Default = 0
    BypassCache = 1
    CacheOnly = 2
    CacheIfAvailable = 3
    Revalidate = 4
    Reload = 5
    NoCacheNoStore = 6

