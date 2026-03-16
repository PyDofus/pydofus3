from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class ShaderWaveParameters(MyBaseModel):
	TYPE: ClassVar[str] = "Wave"
	waveTexID: int

