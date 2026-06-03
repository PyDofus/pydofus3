from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Animation import Animation
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.FlashMaskState import FlashMaskState
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Color
from pydofus3.not_generated.unity import Vector4
from typing import Annotated, Union

class MaterialDescriptor(MyBaseModel):
	textureRequestId: int
	maskFlags: Annotated[Union[FlashMaskState, int], Field(union_mode='left_to_right')]
	maskRef: int
	blendMode: Annotated[Union[Animation.hat, int], Field(union_mode='left_to_right')]
	colorMatrix: list[Vector4]
	renderQueue: int
	customisationColors: list[Color]
	rootColor: Color

