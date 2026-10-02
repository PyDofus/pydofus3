from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.EffectsSortingLayer import EffectsSortingLayer
from pydofus3.generated.pydantic.AleCore.Parameters.TransformParameters import TransformParameters
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union

class ScreenAreaEffectParameters(MyBaseModel):
	transform: TransformParameters
	layer: Annotated[Union[EffectsSortingLayer, int], Field(union_mode='left_to_right')]
	renderOrder: int
	cellID: int
	mapID: int

