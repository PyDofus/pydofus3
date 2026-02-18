from enum import IntFlag

# UnityEngine.AddressableAssets.Addressables
class Addressables(IntFlag):
    NONE = 0
    UseFirst = 0
    Union = 1
    Intersection = 2

# UnityEngine.AddressableAssets.AddressablesPlatform
class AddressablesPlatform(IntFlag):
    Unknown = 0
    Windows = 1
    OSX = 2
    Linux = 3
    PS4 = 4
    Switch = 5
    XboxOne = 6
    WebGL = 7
    iOS = 8
    Android = 9
    WindowsUniversal = 10

# UnityEngine.AddressableAssets.InvalidKeyException
class InvalidKeyException(IntFlag):
    StandardMessage = 0
    NoMergeMode = 1
    MultipleTypesRequested = 2
    NoLocation = 3
    TypeMismatch = 4
    MultipleTypeMismatch = 5
    MergeModeBase = 6
    UnionAvailableForKeys = 7
    UnionAvailableForKeysWithoutOther = 8
    IntersectionAvailable = 9
    KeyAvailableAsType = 10

