from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.BlurFilter import BlurFilter
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.ColorMatrixFilter import ColorMatrixFilter
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.DropShadowFilter import DropShadowFilter
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.GlowFilter import GlowFilter
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class FlashFilters(MyBaseModel):
	filterOrder: list[Annotated[Union[FilterType, int], Field(union_mode='left_to_right')]]
	blurFilters: list[BlurFilter]
	glowFilters: list[GlowFilter]
	dropShadowFilters: list[DropShadowFilter]
	colorMatrices: list[ColorMatrixFilter]

	class FilterType(OpenAPIIntEnum):
		Blur = 0
		Glow = 1
		DropShadow = 2
		ColorMatrix = 3

