from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Material

class CustomScreenPassSettings(MyBaseModel):
	screenPassMaterial: Material
	screenPassShaderIndex: int
	textureScaleDownFactor: int

