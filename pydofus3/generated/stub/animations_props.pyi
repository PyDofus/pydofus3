from UnityPy.classes.PPtr import PPtr
from UnityPy.classes.generated import MonoBehaviour
from typing import Union
from UnityPy.classes.generated import TextAsset, Texture2D

class AnimTransform:
    rX: float
    uX: float
    rY: float
    uY: float
    tX: float
    tY: float

class AnimatedObjectDefinition(MonoBehaviour):
    defaultAnimationName: str
    defaultAnimationLoops: int
    defaultFrameRate: int
    maxNodeCount: int
    exposedNodeNames: list[str]
    maskableNodes: list[MaskableNode]
    boneAsset: PPtr[SkinAsset]
    graphics: list[SkinAssetPartPair]
    animations: list[Animation]
    blankAnimations: list[str]

class Animation:
    name: str
    data: PPtr[TextAsset]
    dataBytes: list[int]
    bounds: Rectf

class AnimationGeometryVertex:
    pos: Vector3f
    uv: Vector2f
    multiplicativeColor: int
    additiveColor: int

class DisplayListEntry:
    symbolId: int
    entries: int
    transform: AnimTransform

class MaskableNode:
    name: str
    graphicSymbolId: str

class Rectf:
    x: float
    y: float
    width: float
    height: float

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

class SkinAssetPartPair:
    asset: PPtr[SkinAsset]
    part: SkinAssetPart

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
