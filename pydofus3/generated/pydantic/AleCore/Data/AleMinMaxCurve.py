from pydofus3.generated.pydantic.AleCore.Data.AleAnimationCurve import AleAnimationCurve
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel

class AleMinMaxCurve(MyBaseModel):
	constantMin: float_nan
	constantMax: float_nan
	curveMin: AleAnimationCurve
	curveMax: AleAnimationCurve
	mode: int

