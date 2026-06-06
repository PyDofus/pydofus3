from pydofus3.generated.pydantic.Ankama.Animations.Rendering.AnimationGeometryVertex import AnimationGeometryVertex
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.CustomBounds import CustomBounds
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from pydofus3.not_generated.unity import Color
from pydofus3.not_generated.unity import Material
from pydofus3.not_generated.unity import ScriptableRendererFeature
from pydofus3.not_generated.unity import Vector2
from typing import ClassVar

class FlashFilterRenderFeature(ScriptableRendererFeature):
	settings: FilterSettings

	class FilterSettings(MyBaseModel):
		animator2DMaterial: Material
		compositeMaterial: Material
		blurMaterial: Material
		shadowGlowMaterial: Material
		stencilMaterial: Material
		currentZoom: float_nan

	class SourceSymbolData(MyBaseModel):
		subMeshIndex: int
		bounds: CustomBounds
		textureId: int

	class FilterRenderRequest[T](MyBaseModel):
		sourceSymbolData: FlashFilterRenderFeature.SourceSymbolData
		filterSettings: T
		destinationTextureId: int
		zoomScale: float_nan
		materialColor: Color

	class StencilRenderRequest(MyBaseModel):
		compositeSubMeshIndex: int
		compositeSubMeshCount: int
		stencilSubMeshIndex: int
		materialListIndex: int
		stencilBounds: CustomBounds
		zoomScale: float_nan
		flipped: bool
		destinationTextureId: int

	class EffectResultBuffered(MyBaseModel):
		verts: list[AnimationGeometryVertex]
		indices: list[int]
		textureRequestId: int
		bounds: CustomBounds

	class ResultTextureRequest(MyBaseModel):
		id: int
		width: int
		height: int
		textureTaken: bool

	class gsa(OpenAPIIntEnum):
		dtpm = 0
		dtpn = 1
		dtpo = 2
		dtpp = 3
		dtpq = 4

	class FlashFilterPass(MyBaseModel):
		class FinalBlitVertex(MyBaseModel):
			pos: Vector2
			uv: Vector2

		class gsb(MyBaseModel):
			dtpr: ClassVar[str] = "FlashFilterPass"
			dtps: ClassVar[str] = "FilterActions.Composite"
			dtpt: ClassVar[str] = "FilterActions.Blur"
			dtpu: ClassVar[str] = "FilterActions.GlowDropShadow"
			dtpv: ClassVar[str] = "FilterActions.Stencil"
			dtpw: ClassVar[str] = "FilterActions.ColorMatrix"
			dtpx: ClassVar[str] = "CompositeMeshToTarget"
			dtpy: ClassVar[str] = "Copy Bounds"
			dtpz: ClassVar[str] = "Apply Mask"
			dtqa: ClassVar[str] = "Glow"
			dtqb: ClassVar[str] = "DropShadow"
			dtqc: ClassVar[str] = "Blur"
			dtqd: ClassVar[str] = "ColorMatrix"

