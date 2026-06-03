from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import ClassVar

class ShaderConstants(MyBaseModel):
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

