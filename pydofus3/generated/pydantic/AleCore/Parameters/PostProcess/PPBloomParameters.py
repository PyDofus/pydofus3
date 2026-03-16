from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class PPBloomParameters(MyBaseModel):
	TYPE: ClassVar[str] = "Bloom"
	threshold: float_nan
	intensity: float_nan
	scatter: float_nan
	color: AleColor

