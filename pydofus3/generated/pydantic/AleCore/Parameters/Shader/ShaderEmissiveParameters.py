from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class ShaderEmissiveParameters(MyBaseModel):
	TYPE: ClassVar[str] = "Emissive"
	emissiveTexID: int
	color: AleColor
	factor: float_nan
	isFactorLinkedToMapNoiseModifier: bool
	isAnimated: bool
	displayUseEmissiveAnimationPerParticle: bool
	useEmissiveAnimationPerParticle: bool
	animationOffsetPerParticle: AleMinMaxCurve
	frequency: float_nan
	timeOffset: float_nan
	isTimeOffsetRandom: bool
	curveMin: float_nan
	curveMax: float_nan
	curveClampMin: float_nan
	curveClampMax: float_nan
	isFrequencyNoised: bool
	frequencyNoiseTexID: int
	noiseStrength: float_nan
	noiseSpeed: float_nan
	areAreasDelayed: bool

