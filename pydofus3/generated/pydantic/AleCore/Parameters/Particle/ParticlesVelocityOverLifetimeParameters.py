from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurveHideMode import AleMinMaxCurveHideMode
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemSimulationSpaceRestricted import AleParticleSystemSimulationSpaceRestricted
from pydofus3.not_generated.base import MyBaseModel

from typing import Union, Annotated

class ParticlesVelocityOverLifetimeParameters(MyBaseModel):
	linearVelocityMode: int
	linearX: AleMinMaxCurveHideMode
	linearY: AleMinMaxCurveHideMode
	linearZ: AleMinMaxCurveHideMode
	systemSimulationSimulationSpaceRestricted: Annotated[Union[AleParticleSystemSimulationSpaceRestricted, int], Field(union_mode='left_to_right')]
	orbitalVelocityMode: int
	orbitalX: AleMinMaxCurveHideMode
	orbitalY: AleMinMaxCurveHideMode
	orbitalZ: AleMinMaxCurveHideMode
	offsetVelocityMode: int
	orbitalOffsetX: AleMinMaxCurveHideMode
	orbitalOffsetY: AleMinMaxCurveHideMode
	orbitalOffsetZ: AleMinMaxCurveHideMode
	radial: AleMinMaxCurve
	speedModifier: AleMinMaxCurve

