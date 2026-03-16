from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.ParticlesStagingEffect import ParticlesStagingEffect
from typing import ClassVar

class ParticlesStopStagingEffect(ParticlesStagingEffect):
	TYPE: ClassVar[str] = "Particle Stop"
	clear: bool

