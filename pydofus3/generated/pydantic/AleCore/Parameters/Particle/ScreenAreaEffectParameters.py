from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.EffectShape import EffectShape
from pydofus3.generated.pydantic.AleCore.Data.EffectsSortingLayer import EffectsSortingLayer
from pydofus3.generated.pydantic.AleCore.Parameters.TransformParameters import TransformParameters
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union

class ScreenAreaEffectParameters(MyBaseModel):
	transform: TransformParameters
	shape: Annotated[Union[EffectShape, int], Field(union_mode='left_to_right')]
	mask: bool
	layer: Annotated[Union[EffectsSortingLayer, int], Field(union_mode='left_to_right')]
	renderOrder: int
	placeEffectOnCell: bool
	cellID: int
	mapID: int
	weight: int
	isRenderedAfterTransparents: bool

