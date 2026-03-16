from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import Material

class OutlinePostPassSettings(MyBaseModel):
	addOutlinesMaterial: Material
	shaderAddOutlinesPassIndex: int
	textureScaleDownFactor: int

