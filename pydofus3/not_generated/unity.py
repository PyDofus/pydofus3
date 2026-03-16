from enum import IntFlag

from pydantic import BaseModel

from pydofus3.not_generated.base import OpenAPIIntEnum


class Vector2Int(BaseModel):
    x: int
    y: int

class Color32(BaseModel):
    r: int
    g: int
    b: int
    a: int

class Vector3(BaseModel):
    x: float
    y: float
    z: float

class Vector2(BaseModel):
    x: float
    y: float

class float2(BaseModel):
    x: float
    y: float

class Color(BaseModel):
    r: float
    g: float
    b: float
    a: float

class Quaternion(BaseModel):
    x: float
    y: float
    z: float
    w: float


class Vector4(BaseModel):
    X: float
    Y: float
    Z: float
    W: float

class Rect(BaseModel):
    x: float
    y: float
    width: float
    height: float

class Material(BaseModel):
    m_FileID: int
    m_PathID: int

class ParticleSystem(BaseModel):
    m_FileID: int
    m_PathID: int

class BlendMode(OpenAPIIntEnum):
    Zero = 0
    One = 1
    DstColor = 2
    SrcColor = 3
    OneMinusDstColor = 4
    SrcAlpha = 5
    OneMinusSrcColor = 6
    DstAlpha = 7
    OneMinusDstAlpha = 8
    SrcAlphaSaturate = 9
    OneMinusSrcAlpha = 10


class BlendOp(OpenAPIIntEnum):
    Add = 0
    Subtract = 1
    ReverseSubtract = 2
    Min = 3
    Max = 4
    LogicalClear = 5
    LogicalSet = 6
    LogicalCopy = 7
    LogicalCopyInverted = 8
    LogicalNoop = 9
    LogicalInvert = 10
    LogicalAnd = 11
    LogicalNand = 12
    LogicalOr = 13
    LogicalNor = 14
    LogicalXor = 15
    LogicalEquivalence = 16
    LogicalAndReverse = 17
    LogicalAndInverted = 18
    LogicalOrReverse = 19
    LogicalOrInverted = 20
    Multiply = 21
    Screen = 22
    Overlay = 23
    Darken = 24
    Lighten = 25
    ColorDodge = 26
    ColorBurn = 27
    HardLight = 28
    SoftLight = 29
    Difference = 30
    Exclusion = 31
    HSLHue = 32
    HSLSaturation = 33
    HSLColor = 34
    HSLLuminosity = 35

class SortingCriteria(IntFlag):
    None_ = 0
    SortingLayer = 1
    RenderQueue = 2
    BackToFront = 4
    QuantizedFrontToBack = 8
    OptimizeStateChanges = 16
    CommonTransparent = 23
    CanvasOrder = 32
    CommonOpaque = 59
    RendererPriority = 64

class RenderPassEvent(OpenAPIIntEnum):
    BeforeRendering = 0
    BeforeRenderingShadows = 50
    AfterRenderingShadows = 100
    BeforeRenderingPrePasses = 150
    AfterRenderingPrePasses = 200
    BeforeRenderingGbuffer = 210
    AfterRenderingGbuffer = 220
    BeforeRenderingDeferredLights = 230
    AfterRenderingDeferredLights = 240
    BeforeRenderingOpaques = 250
    AfterRenderingOpaques = 300
    BeforeRenderingSkybox = 350
    AfterRenderingSkybox = 400
    BeforeRenderingTransparents = 450
    AfterRenderingTransparents = 500
    BeforeRenderingPostProcessing = 550
    AfterRenderingPostProcessing = 600
    AfterRendering = 1000

class ScriptableRendererFeature(BaseModel):
    m_Active: bool
