from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxGradient import AleMinMaxGradient
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.ParticlesStagingEffect import ParticlesStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar

class ParticleMainStagingEffect(ParticlesStagingEffect):
	startColor: StagingEvolutiveVar[AleMinMaxGradient]

