from enum import IntFlag

# UnityEngine.Tilemaps.TileAnimationFlags
class TileAnimationFlags(IntFlag):
    NONE = 0
    LoopOnce = 1
    PauseAnimation = 2
    UpdatePhysics = 4
    UnscaledTime = 8
    SyncAnimation = 16

# UnityEngine.Tilemaps.TileFlags
class TileFlags(IntFlag):
    NONE = 0
    LockColor = 1
    LockTransform = 2
    InstantiateGameObjectRuntimeOnly = 4
    KeepGameObjectRuntimeOnly = 8
    LockAll = 3

