from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Utils.ObjectDisplayBehaviour import ObjectDisplayBehaviour
from pydofus3.generated.pydantic.Editor.AleCore.Data.Transform2D import Transform2D
from pydofus3.not_generated.base import MyBaseModel

from typing import Union, Annotated

class ClientElementTransform(MyBaseModel):
	gfxId: int
	color: AleColor
	transform: Transform2D
	materialIndex: int
	displayBehaviour: Annotated[Union[ObjectDisplayBehaviour, int], Field(union_mode='left_to_right')]

