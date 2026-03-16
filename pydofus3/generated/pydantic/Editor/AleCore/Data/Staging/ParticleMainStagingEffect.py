from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxGradient import AleMinMaxGradient
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.ParticlesStagingEffect import ParticlesStagingEffect
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.StagingEvolutiveVar import StagingEvolutiveVar
from typing import ClassVar

class ParticleMainStagingEffect(ParticlesStagingEffect):
	TYPE: ClassVar[str] = "Particle Main"
	startColor: StagingEvolutiveVar[AleMinMaxGradient]

