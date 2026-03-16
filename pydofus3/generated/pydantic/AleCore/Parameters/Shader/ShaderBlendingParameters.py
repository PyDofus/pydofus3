from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class ShaderBlendingParameters(MyBaseModel):
	TYPE: ClassVar[str] = "Blending"
	sourceFactor: int
	blendOperation: int
	destinationFactor: int

