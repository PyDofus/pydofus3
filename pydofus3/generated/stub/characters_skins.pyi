from UnityPy.classes.PPtr import PPtr
from UnityPy.classes.generated import MonoBehaviour
from typing import Union
from UnityPy.classes.generated import Texture2D

class AnimTransform:
    rX: float
    uX: float
    rY: float
    uY: float
    tX: float
    tY: float

class AnimationGeometryVertex:
    pos: Vector3f
    uv: Vector2f
    multiplicativeColor: int
    additiveColor: int

class DisplayListEntry:
    symbolId: int
    entries: int
    transform: AnimTransform

class SkinAsset(MonoBehaviour):
    m_values: list[SkinAssetPart]
    m_keys: list[str]
    triangles: list[int]
    vertices: list[AnimationGeometryVertex]
    referencedSymbols: list[str]
    emptyCustomisations: list[str]
    textures: list[PPtr[Texture2D]]

class SkinAssetPart:
    name: str
    DisplayListEntry: list[DisplayListEntry]
    skinChunks: list[SkinChunk]

class SkinChunk:
    startVertexIndex: int
    indexCount: int
    startIndexIndex: int
    vertexCount: int
    textureIndex: int
    maskState: int

class Vector2f:
    x: float
    y: float

class Vector3f:
    x: float
    y: float
    z: float
