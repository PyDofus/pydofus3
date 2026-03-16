from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Color32

class GlowFilter(MyBaseModel):
	glowColor: Color32
	blurX: float_nan
	blurY: float_nan
	strength: float_nan
	inner: bool
	knockout: bool
	compositeSource: bool
	numPasses: int

