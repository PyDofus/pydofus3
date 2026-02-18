from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Utils.ObjectDisplayBehaviour import ObjectDisplayBehaviour
from pydofus3.generated.pydantic.Editor.AleCore.Data.ElementType import ElementType
from pydofus3.generated.pydantic.Editor.AleCore.Data.Transform2D import Transform2D
from pydofus3.not_generated.base import MyBaseModel

from typing import Union, Annotated

class ClientAnimatedElementTransform(MyBaseModel):
	gfxId: int
	cellId: int
	playAnimation: bool
	playAnimStatic: bool
	playerGuildCustomisable: bool
	isStagingTarget: bool
	stagingId: str
	minDelay: int
	maxDelay: int
	requiresServerUpdate: bool
	transform: Transform2D
	type: Annotated[Union[ElementType, int], Field(union_mode='left_to_right')]
	color: AleColor
	innerCellRenderOrder: int
	displayBehaviour: Annotated[Union[ObjectDisplayBehaviour, int], Field(union_mode='left_to_right')]

