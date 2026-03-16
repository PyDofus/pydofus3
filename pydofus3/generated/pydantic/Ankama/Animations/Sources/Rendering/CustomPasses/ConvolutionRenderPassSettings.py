from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Material
from pydofus3.not_generated.unity import Vector2

class ConvolutionRenderPassSettings(MyBaseModel):
	convolutionMaterial: Material
	nbPasses: int
	kernelSize: float_nan
	direction: Vector2
	secondPassMat: Material

