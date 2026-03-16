from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Material
from pydofus3.not_generated.unity import Vector2

class AdjustmentsPassSettings(MyBaseModel):
	adjustmentsMaterial: Material
	remapIn: Vector2
	shouldThreshold: bool
	threshold: float_nan

