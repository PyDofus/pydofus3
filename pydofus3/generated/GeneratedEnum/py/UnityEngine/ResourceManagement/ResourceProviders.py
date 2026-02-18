from enum import IntFlag

# UnityEngine.ResourceManagement.ResourceProviders.AssetBundleResource
class AssetBundleResource(IntFlag):
    NONE = 0
    Local = 1
    Web = 2

# UnityEngine.ResourceManagement.ResourceProviders.AssetLoadMode
class AssetLoadMode(IntFlag):
    RequestedAssetAndDependencies = 0
    AllPackedAssetsAndDependencies = 1

# UnityEngine.ResourceManagement.ResourceProviders.ProviderBehaviourFlags
class ProviderBehaviourFlags(IntFlag):
    NONE = 0
    CanProvideWithFailedDependencies = 1

# UnityEngine.ResourceManagement.ResourceProviders.SceneReleaseMode
class SceneReleaseMode(IntFlag):
    ReleaseSceneWhenSceneUnloaded = 0
    OnlyReleaseSceneOnHandleRelease = 1

