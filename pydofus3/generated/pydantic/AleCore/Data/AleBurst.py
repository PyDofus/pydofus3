from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel

class AleBurst(MyBaseModel):
	time: float_nan
	count: AleMinMaxCurve
	cycleCount: int
	repeatInterval: float_nan
	probability: float_nan

