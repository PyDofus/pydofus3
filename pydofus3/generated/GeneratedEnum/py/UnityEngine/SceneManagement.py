from enum import IntFlag

# UnityEngine.SceneManagement.LoadSceneMode
class LoadSceneMode(IntFlag):
    Single = 0
    Additive = 1

# UnityEngine.SceneManagement.LocalPhysicsMode
class LocalPhysicsMode(IntFlag):
    NONE = 0
    Physics2D = 1
    Physics3D = 2

# UnityEngine.SceneManagement.UnloadSceneOptions
class UnloadSceneOptions(IntFlag):
    NONE = 0
    UnloadAllEmbeddedSceneObjects = 1

