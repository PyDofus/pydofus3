from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.AleGradient import AleGradient
from pydofus3.not_generated.base import MyBaseModel

class AleMinMaxGradient(MyBaseModel):
	colorMin: AleColor
	colorMax: AleColor
	gradientMin: AleGradient
	gradientMax: AleGradient
	mode: int

