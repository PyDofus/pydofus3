from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.AnimatedObjectDefinition import AnimatedObjectDefinition
from pydofus3.generated.pydantic.Ankama.Animations.CustomisationSlot import CustomisationSlot
from pydofus3.generated.pydantic.Ankama.Animations.SkinAsset import SkinAsset
from pydofus3.generated.pydantic.gso import gso
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from pydofus3.not_generated.unity import Color
from typing import Annotated, Union
from typing import ClassVar

class Animator2D(MyBaseModel):
	DefaultShader: ClassVar[str] = "Custom/DofusMainShader"
	definition: AnimatedObjectDefinition
	customisationSlots: dict[str, CustomisationSlot]
	renderingMethod: Annotated[Union[gso, int], Field(union_mode='left_to_right')]
	colorModifier: Color
	sortingLayerIdInternal: int
	sortingOrderInternal: int
	overriddenFrameRate: int
	skin: SkinAsset
	filtersQuality: float_nan

	class gsl(OpenAPIIntEnum):
		dtyk = 0
		dtyl = 1
		dtym = 2

