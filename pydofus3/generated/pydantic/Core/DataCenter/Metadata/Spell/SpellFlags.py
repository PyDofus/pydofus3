from pydofus3.not_generated.base import FlagBaseModel
from typing import Annotated

class SpellFlags(FlagBaseModel):
	VerboseCast : Annotated[bool,1]
	BypassSummoningLimit : Annotated[bool,2]
	CanAlwaysTriggerSpells : Annotated[bool,4]
	HideCastConditions : Annotated[bool,8]

