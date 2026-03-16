from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class ShaderCustomFramerateParameters(MyBaseModel):
	TYPE: ClassVar[str] = "Custom Framerate"
	framerate: float_nan

