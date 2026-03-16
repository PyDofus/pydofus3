from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurveHideMode import AleMinMaxCurveHideMode
from pydofus3.not_generated.base import MyBaseModel

class ParticlesRotationOverLifetimeParameters(MyBaseModel):
	isRotationOverLifetimeSeparateAxes: bool
	rotationOverLifetime3DMode: int
	angularVelocity: AleMinMaxCurve
	angularVelocityX: AleMinMaxCurveHideMode
	angularVelocityY: AleMinMaxCurveHideMode
	angularVelocityZ: AleMinMaxCurveHideMode

