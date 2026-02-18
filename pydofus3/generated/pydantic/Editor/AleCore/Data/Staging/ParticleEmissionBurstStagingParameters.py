from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan

class ParticleEmissionBurstStagingParameters(MyBaseModel):
	burstIndex: int
	time: StagingEvolutiveVar[float_nan]
	count: StagingEvolutiveVar[AleMinMaxCurve]
	cycles: StagingEvolutiveVar[int]
	interval: StagingEvolutiveVar[float_nan]
	probability: StagingEvolutiveVar[float_nan]

