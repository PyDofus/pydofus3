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
