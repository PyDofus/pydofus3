from typing import Annotated
from pydofus3.not_generated.base import FlagBaseModel


class SpellFlags(FlagBaseModel):
	VerboseCast : Annotated[bool,1]
	BypassSummoningLimit : Annotated[bool,2]
	CanAlwaysTriggerSpells : Annotated[bool,4]
	HideCastConditions : Annotated[bool,8]

