from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxGradient import AleMinMaxGradient
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemTrailTextureMode import AleParticleSystemTrailTextureMode
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan

class ParticlesTrailsParameters(MyBaseModel):
	trailsRatio: float_nan
	trailsLifetime: AleMinMaxCurve
	trailsMinVertexDistance: float_nan
	trailsWorldSpace: bool
	trailsDieWithParticles: bool
	trailsTextureMode: AleParticleSystemTrailTextureMode
	trailsSizeAffectsWidth: bool
	trailsSizeAffectsLifetime: bool
	trailsInheritParticleColor: bool
	trailsColorOverLifetime: AleMinMaxGradient
	trailsWidthOverTrail: AleMinMaxCurve
	trailsColorOverTrail: AleMinMaxGradient

