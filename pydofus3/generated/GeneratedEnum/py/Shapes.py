from enum import IntFlag

# Shapes.AngularUnit
class AngularUnit(IntFlag):
    Radians = 0
    Degrees = 1
    Turns = 2

# Shapes.ArcEndCap
class ArcEndCap(IntFlag):
    NONE = 0
    Round = 1

# Shapes.DashSnapping
class DashSnapping(IntFlag):
    Off = 0
    Tiling = 1
    EndToEnd = 2

# Shapes.DashSpace
class DashSpace(IntFlag):
    FixedCount = -2
    Relative = -1
    Meters = 0

# Shapes.DashType
class DashType(IntFlag):
    Basic = 0
    Angled = 1
    Rounded = 2

# Shapes.DetailLevel
class DetailLevel(IntFlag):
    Minimal = 0
    Low = 1
    Medium = 2
    High = 3
    Extreme = 4

# Shapes.Disc
class Disc(IntFlag):
    Single = 0
    Radial = 1
    Angular = 2
    Bilinear = 3

# Shapes.DiscGeometry
class DiscGeometry(IntFlag):
    Flat2D = 0
    Billboard = 1

# Shapes.DiscType
class DiscType(IntFlag):
    Disc = 0
    Pie = 1
    Ring = 2
    Arc = 3

# Shapes.FillSpace
class FillSpace(IntFlag):
    Local = 0
    World = 1

# Shapes.FillType
class FillType(IntFlag):
    LinearGradient = 0
    RadialGradient = 1

# Shapes.IMDrawer
class IMDrawer(IntFlag):
    Shape = 0
    Text = 1

# Shapes.Line
class Line(IntFlag):
    Single = 0
    Double = 1

# Shapes.LineEndCap
class LineEndCap(IntFlag):
    NONE = 0
    Square = 1
    Round = 2

# Shapes.LineGeometry
class LineGeometry(IntFlag):
    Flat2D = 0
    Billboard = 1
    Volumetric3D = 2

# Shapes.MeshUpdateMode
class MeshUpdateMode(IntFlag):
    UseAsset = 0
    UseAssetCopy = 1
    SelfGenerated = 2

# Shapes.PolygonTriangulation
class PolygonTriangulation(IntFlag):
    FastConvexOnly = 0
    EarClipping = 1

# Shapes.PolylineGeometry
class PolylineGeometry(IntFlag):
    Flat2D = 0
    Billboard = 1

# Shapes.PolylineJoins
class PolylineJoins(IntFlag):
    Simple = 0
    Miter = 1
    Round = 2
    Bevel = 3

# Shapes.Quad
class Quad(IntFlag):
    Single = 0
    Horizontal = 1
    Vertical = 2
    PerCorner = 3

# Shapes.RectPivot
class RectPivot(IntFlag):
    Corner = 0
    Center = 1

# Shapes.Rectangle
class Rectangle(IntFlag):
    HardSolid = 0
    RoundedSolid = 1
    HardBorder = 2
    RoundedBorder = 3

# Shapes.Rectangle
class Rectangle(IntFlag):
    Uniform = 0
    PerCorner = 1

# Shapes.RegularPolygonGeometry
class RegularPolygonGeometry(IntFlag):
    Flat2D = 0
    Billboard = 1

# Shapes.RenderPipeline
class RenderPipeline(IntFlag):
    Legacy = 0
    URP = 1
    HDRP = 2

# Shapes.ScaleMode
class ScaleMode(IntFlag):
    Uniform = 0
    Coordinate = 1

# Shapes.ShapesBlendMode
class ShapesBlendMode(IntFlag):
    Opaque = 0
    Transparent = 1
    Additive = 2
    ColorDodge = 9
    Screen = 4
    Lighten = 7
    LinearBurn = 6
    ColorBurn = 10
    Multiplicative = 3
    Darken = 8
    Subtractive = 5

# Shapes.ShapesConfig
class ShapesConfig(IntFlag):
    fixed4 = 0
    half4 = 1
    float4 = 2

# Shapes.ShapesConfig
class ShapesConfig(IntFlag):
    Off = 0
    Medium = 1
    High = 2

# Shapes.ShapesConfig
class ShapesConfig(IntFlag):
    Low = 0
    Medium = 1
    High2D = 2
    High = 3

# Shapes.ShapesMeshGen
class ShapesMeshGen(IntFlag):
    Unknown = 0
    Reflex = 1
    Convex = 2

# Shapes.TextAlign
class TextAlign(IntFlag):
    TopLeft = 0
    Top = 1
    TopRight = 2
    Left = 3
    Center = 4
    Right = 5
    BottomLeft = 6
    Bottom = 7
    BottomRight = 8

# Shapes.TextureFillMode
class TextureFillMode(IntFlag):
    StretchToFill = 0
    ScaleToFit = 1
    ScaleAndCropToFill = 2

# Shapes.TextureSizeMode
class TextureSizeMode(IntFlag):
    Width = 0
    Height = 1
    LongestSide = 2
    ShortestSide = 3
    PixelsPerMeter = 4
    Radius = 5

# Shapes.ThicknessSpace
class ThicknessSpace(IntFlag):
    Meters = 0
    Pixels = 1
    Noots = 2

# Shapes.Triangle
class Triangle(IntFlag):
    Single = 0
    PerCorner = 1

