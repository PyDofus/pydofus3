from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel

class AleColorKey(MyBaseModel):
	color: AleColor
	time: float_nan

