from pydofus3.not_generated.base import FlagBaseModel
from typing import Annotated

class EffectInstanceFlags(FlagBaseModel):
	VisibleInTooltip : Annotated[bool,1]
	VisibleInBuffUi : Annotated[bool,2]
	VisibleInFightLog : Annotated[bool,4]
	VisibleOnTerrain : Annotated[bool,8]
	ForClientOnly : Annotated[bool,16]
	Trigger : Annotated[bool,32]

