from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemRenderMode import AleParticleSystemRenderMode
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemRenderSpace import AleParticleSystemRenderSpace
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemSortMode import AleParticleSystemSortMode
from pydofus3.generated.pydantic.AleCore.Data.AleVector3 import AleVector3
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan

class ParticlesRendererParameters(MyBaseModel):
	renderMode: AleParticleSystemRenderMode
	cameraVelocityScale: float_nan
	velocityScale: float_nan
	lengthScale: float_nan
	freeformStretching: bool
	rotateWithStretchDirection: bool
	sortMode: AleParticleSystemSortMode
	sortingFudge: float_nan
	minParticleSize: float_nan
	maxParticleSize: float_nan
	renderAlignment: AleParticleSystemRenderSpace
	flip: AleVector3
	allowRoll: bool
	pivot: AleVector3

