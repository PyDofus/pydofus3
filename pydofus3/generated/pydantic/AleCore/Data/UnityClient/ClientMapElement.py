from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Utils.ObjectDisplayBehaviour import ObjectDisplayBehaviour
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union

class ClientMapElement(MyBaseModel):
	position: AleVector2
	rotation: float_nan
	scale: AleVector2
	color: AleColor
	gfxId: int
	displayBehaviour: Annotated[Union[ObjectDisplayBehaviour, int], Field(union_mode='left_to_right')]

