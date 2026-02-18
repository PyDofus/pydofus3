from __future__ import annotations
from typing import TypedDict, Any, Union

class PPtr(TypedDict):
    m_FileID: int
    m_PathID: int

class MonoBehaviour(TypedDict):
    m_Enabled: int
    m_GameObject: PPtr
    m_Name: str
    m_Script: PPtr
class Texture2D(TypedDict):
    pass

class AnimTransform(TypedDict):
    rX: float
    uX: float
    rY: float
    uY: float
    tX: float
    tY: float

class AnimationGeometryVertex(TypedDict):
    pos: Vector3f
    uv: Vector2f
    multiplicativeColor: int
    additiveColor: int

class DisplayListEntry(TypedDict):
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
    textures: list[PPtr]

class SkinAssetPart(TypedDict):
    name: str
    DisplayListEntry: list[DisplayListEntry]
    skinChunks: list[SkinChunk]

class SkinChunk(TypedDict):
    startVertexIndex: int
    indexCount: int
    startIndexIndex: int
    vertexCount: int
    textureIndex: int
    maskState: int

class Vector2f(TypedDict):
    x: float
    y: float

class Vector3f(TypedDict):
    x: float
    y: float
    z: float
