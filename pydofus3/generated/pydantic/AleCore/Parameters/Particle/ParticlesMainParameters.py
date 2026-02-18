from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleConstantOr2Constants import AleConstantOr2Constants
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurveHideMode import AleMinMaxCurveHideMode
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxGradient import AleMinMaxGradient
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemSimulationSpace import AleParticleSystemSimulationSpace
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class ParticlesMainParameters(MyBaseModel):
	duration: float_nan
	looping: bool
	prewarm: bool
	startDelay: AleConstantOr2Constants
	startLifetime: AleMinMaxCurve
	startSpeed: AleMinMaxCurve
	is3DStartSize: bool
	startSize3DMode: int
	startSize: AleMinMaxCurve
	startSizeX: AleMinMaxCurveHideMode
	startSizeY: AleMinMaxCurveHideMode
	startSizeZ: AleMinMaxCurveHideMode
	is3DStartRotation: bool
	startRotation3DMode: int
	startRotation: AleMinMaxCurve
	startRotationX: AleMinMaxCurveHideMode
	startRotationY: AleMinMaxCurveHideMode
	startRotationZ: AleMinMaxCurveHideMode
	flipRotation: float_nan
	startColor: AleMinMaxGradient
	gravityModifier: AleMinMaxCurve
	simulationSpace: Annotated[Union[AleParticleSystemSimulationSpace, int], Field(union_mode='left_to_right')]
	simulationSpeed: float_nan
	useAutoRandomSeed: bool
	randomSeed: int
	stopped: bool

