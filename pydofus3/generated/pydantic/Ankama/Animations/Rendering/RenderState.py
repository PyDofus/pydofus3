from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Animation import Animation
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.FlashFilters import FlashFilters
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Vector4
from typing import Annotated, Union

class RenderState(MyBaseModel):
	m00: float_nan
	m01: float_nan
	m03: float_nan
	m10: float_nan
	m11: float_nan
	m13: float_nan
	multiplicativeColor: int
	additiveColor: int
	spriteIndex: int
	customisationIndex: int
	childrenRecursiveCount: int
	alpha: int
	maskFlags: Animation.gsf
	blendMode: Annotated[Union[Animation.gsg, int], Field(union_mode='left_to_right')]
	colorMatrix: list[Vector4]
	flashFilters: FlashFilters

