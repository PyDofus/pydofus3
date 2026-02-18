from enum import IntFlag

# UnityEngine.TerrainUtils.TerrainMapStatusCode
class TerrainMapStatusCode(IntFlag):
    OK = 0
    Overlapping = 1
    SizeMismatch = 4
    EdgeAlignmentMismatch = 8

