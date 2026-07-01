from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.AnimatedObjectDefinition import AnimatedObjectDefinition
from pydofus3.generated.pydantic.Ankama.Animations.CustomisationSlot import CustomisationSlot
from pydofus3.generated.pydantic.Ankama.Animations.SkinAsset import SkinAsset
from pydofus3.generated.pydantic.hbq import hbq
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from pydofus3.not_generated.unity import Color
from typing import Annotated, Union

class Animator2D(MyBaseModel):
	definition: AnimatedObjectDefinition
	customisationSlots: dict[str, CustomisationSlot]
	renderingMethod: Annotated[Union[hbq, int], Field(union_mode='left_to_right')]
	colorModifier: Color
	sortingLayerIdInternal: int
	sortingOrderInternal: int
	overriddenFrameRate: int
	skin: SkinAsset
	filtersQuality: float_nan

	class hbn(OpenAPIIntEnum):
		eavr = 0
		eavs = 1
		eavt = 2

