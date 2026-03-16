from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from pydofus3.not_generated.unity import BlendMode
from typing import ClassVar

class ShaderConstants(MyBaseModel):
	Color: ClassVar[str] = "_Color"
	ApplyAlphaStencilKeyword: ClassVar[str] = "APPLY_ALPHA_STENCIL"
	DefaultAnimator2DBlendSourceFactorAlpha: ClassVar[BlendMode] = BlendMode.OneMinusDstAlpha
	DefaultAnimator2DBlendDestinationFactorAlpha: ClassVar[BlendMode] = BlendMode.One
	HighlightCoef: ClassVar[str] = "_HighlightCoef"
	HighlightAdd: ClassVar[str] = "_HighlightAdd"

	class OutlineTestDiff(OpenAPIIntEnum):
		CROSS_2_SIDES = 0
		CROSS_FROM_CENTER = 1
		CROSS_AROUND = 2
		OUTLINE_MASK = 3

	class RenderingLayerIDs(OpenAPIIntEnum):
		DEFAULT = 1
		REFRACTION = 2
		INLINE = 4
		OUTLINE = 8
		WAVE = 16

