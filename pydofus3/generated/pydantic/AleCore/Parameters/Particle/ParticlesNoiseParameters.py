from pydofus3.generated.pydantic.AleCore.Data.AleConstantOrCurve import AleConstantOrCurve
from pydofus3.generated.pydantic.AleCore.Data.AleCurve import AleCurve
from pydofus3.generated.pydantic.AleCore.Data.AleCurveHideMode import AleCurveHideMode
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurveHideMode import AleMinMaxCurveHideMode
from pydofus3.generated.pydantic.AleCore.Data.AleParticleSystemNoiseQuality import AleParticleSystemNoiseQuality
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel

class ParticlesNoiseParameters(MyBaseModel):
	isNoiseStrengthSeparateAxes: bool
	noiseStrength3DMode: int
	noiseStrength: AleMinMaxCurve
	noiseStrengthX: AleMinMaxCurveHideMode
	noiseStrengthY: AleMinMaxCurveHideMode
	noiseStrengthZ: AleMinMaxCurveHideMode
	noiseFrequency: float_nan
	noiseScrollSpeed: AleConstantOrCurve
	noiseDamping: bool
	noiseQuality: AleParticleSystemNoiseQuality
	noiseRemapEnabled: bool
	noiseRemap3DMode: int
	noiseRemapCurve: AleCurve
	noiseRemapCurveX: AleCurveHideMode
	noiseRemapCurveY: AleCurveHideMode
	noiseRemapCurveZ: AleCurveHideMode
	noisePositionAmount: AleMinMaxCurve
	noiseRotationAmount: AleMinMaxCurve
	noiseSizeAmount: AleMinMaxCurve

