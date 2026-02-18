from enum import IntFlag

# UnityEngine.ResourceManagement.Util.BundleSource
class BundleSource(IntFlag):
    NONE = 0
    Local = 1
    Cache = 2
    Download = 4

