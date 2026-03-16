from enum import IntEnum

class AngularUnit(IntEnum):
	Radians = 0
	Degrees = 1
	Turns = 2

class ArcEndCap(IntEnum):
	None_ = 0
	Round = 1

class DashSnapping(IntEnum):
	Off = 0
	Tiling = 1
	EndToEnd = 2

class DashSpace(IntEnum):
	FixedCount = -2
	Relative = -1
	Meters = 0

class DashType(IntEnum):
	Basic = 0
	Angled = 1
	Rounded = 2

class DetailLevel(IntEnum):
	Minimal = 0
	Low = 1
	Medium = 2
	High = 3
	Extreme = 4

class Disc:
	class DiscColorMode(IntEnum):
		Single = 0
		Radial = 1
		Angular = 2
		Bilinear = 3

class DiscGeometry(IntEnum):
	Flat2D = 0
	Billboard = 1

class DiscType(IntEnum):
	Disc = 0
	Pie = 1
	Ring = 2
	Arc = 3

class FillSpace(IntEnum):
	Local = 0
	World = 1

class FillType(IntEnum):
	LinearGradient = 0
	RadialGradient = 1

class IMDrawer:
	class DrawType(IntEnum):
		Shape = 0
		Text = 1

class Line:
	class LineColorMode(IntEnum):
		Single = 0
		Double = 1

class LineEndCap(IntEnum):
	None_ = 0
	Square = 1
	Round = 2

class LineGeometry(IntEnum):
	Flat2D = 0
	Billboard = 1
	Volumetric3D = 2

class MeshUpdateMode(IntEnum):
	UseAsset = 0
	UseAssetCopy = 1
	SelfGenerated = 2

class PolygonTriangulation(IntEnum):
	FastConvexOnly = 0
	EarClipping = 1

class PolylineGeometry(IntEnum):
	Flat2D = 0
	Billboard = 1

class PolylineJoins(IntEnum):
	Simple = 0
	Miter = 1
	Round = 2
	Bevel = 3

class Quad:
	class QuadColorMode(IntEnum):
		Single = 0
		Horizontal = 1
		Vertical = 2
		PerCorner = 3

class Rectangle:
	class RectangleType(IntEnum):
		HardSolid = 0
		RoundedSolid = 1
		HardBorder = 2
		RoundedBorder = 3

	class RectangleCornerRadiusMode(IntEnum):
		Uniform = 0
		PerCorner = 1

class RectPivot(IntEnum):
	Corner = 0
	Center = 1

class RegularPolygonGeometry(IntEnum):
	Flat2D = 0
	Billboard = 1

class RenderPipeline(IntEnum):
	Legacy = 0
	URP = 1
	HDRP = 2

class ScaleMode(IntEnum):
	Uniform = 0
	Coordinate = 1

class ShapesBlendMode(IntEnum):
	Opaque = 0
	Transparent = 1
	Additive = 2
	Multiplicative = 3
	Screen = 4
	Subtractive = 5
	LinearBurn = 6
	Lighten = 7
	Darken = 8
	ColorDodge = 9
	ColorBurn = 10

class ShapesConfig:
	class FragOutputPrecision(IntEnum):
		fixed4 = 0
		half4 = 1
		float4 = 2

	class LocalAAQuality(IntEnum):
		Off = 0
		Medium = 1
		High = 2

	class QuadInterpolationQuality(IntEnum):
		Low = 0
		Medium = 1
		High2D = 2
		High = 3

class ShapesMeshGen:
	class ReflexState(IntEnum):
		Unknown = 0
		Reflex = 1
		Convex = 2

class TextAlign(IntEnum):
	TopLeft = 0
	Top = 1
	TopRight = 2
	Left = 3
	Center = 4
	Right = 5
	BottomLeft = 6
	Bottom = 7
	BottomRight = 8

class TextureFillMode(IntEnum):
	StretchToFill = 0
	ScaleToFit = 1
	ScaleAndCropToFill = 2

class TextureSizeMode(IntEnum):
	Width = 0
	Height = 1
	LongestSide = 2
	ShortestSide = 3
	PixelsPerMeter = 4
	Radius = 5

class ThicknessSpace(IntEnum):
	Meters = 0
	Pixels = 1
	Noots = 2

class Triangle:
	class TriangleColorMode(IntEnum):
		Single = 0
		PerCorner = 1

