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

	class gsd(OpenAPIIntEnum):
		dtuh = 0
		dtui = 1
		dtuj = 2
		dtuk = 3
		dtul = 4

	class FlashFilterPass(MyBaseModel):
		class FinalBlitVertex(MyBaseModel):
			pos: Vector2
			uv: Vector2

		class gse(MyBaseModel):
			dtum: ClassVar[str] = "FlashFilterPass"
			dtun: ClassVar[str] = "FilterActions.Composite"
			dtuo: ClassVar[str] = "FilterActions.Blur"
			dtup: ClassVar[str] = "FilterActions.GlowDropShadow"
			dtuq: ClassVar[str] = "FilterActions.Stencil"
			dtur: ClassVar[str] = "FilterActions.ColorMatrix"
			dtus: ClassVar[str] = "CompositeMeshToTarget"
			dtut: ClassVar[str] = "Copy Bounds"
			dtuu: ClassVar[str] = "Apply Mask"
			dtuv: ClassVar[str] = "Glow"
			dtuw: ClassVar[str] = "DropShadow"
			dtux: ClassVar[str] = "Blur"
			dtuy: ClassVar[str] = "ColorMatrix"

