from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemSubEmitterProperties import AleParticleSystemSubEmitterProperties
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemSubEmitterType import AleParticleSystemSubEmitterType
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union

class ParticlesSubEmittersParameters(MyBaseModel):
	parentId: str
	type: Annotated[Union[AleParticleSystemSubEmitterType, int], Field(union_mode='left_to_right')]
	properties: AleParticleSystemSubEmitterProperties
	emitProbability: float_nan

