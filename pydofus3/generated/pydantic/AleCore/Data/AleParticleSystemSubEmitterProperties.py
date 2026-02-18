from typing import Annotated
from pydofus3.not_generated.base import FlagBaseModel


class AleParticleSystemSubEmitterProperties(FlagBaseModel):
	InheritNothing : Annotated[bool,0]
	InheritEverything : Annotated[bool,31]
	InheritColor : Annotated[bool,1]
	InheritSize : Annotated[bool,2]
	InheritRotation : Annotated[bool,4]
	InheritLifetime : Annotated[bool,8]
	InheritDuration : Annotated[bool,16]

