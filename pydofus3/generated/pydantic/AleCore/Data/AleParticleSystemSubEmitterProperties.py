from pydofus3.not_generated.base import FlagBaseModel
from typing import Annotated

class AleParticleSystemSubEmitterProperties(FlagBaseModel):
	InheritNothing : Annotated[bool,0]
	InheritColor : Annotated[bool,1]
	InheritSize : Annotated[bool,2]
	InheritRotation : Annotated[bool,4]
	InheritLifetime : Annotated[bool,8]
	InheritDuration : Annotated[bool,16]
	InheritEverything : Annotated[bool,31]

