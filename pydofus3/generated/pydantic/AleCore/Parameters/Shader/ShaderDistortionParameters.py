from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.UVModes import UVModes
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union
from typing import ClassVar

class ShaderDistortionParameters(MyBaseModel):
	TYPE: ClassVar[str] = "Distortion"
	noiseTexID: int
	noiseTexUVMode: Annotated[Union[UVModes, int], Field(union_mode='left_to_right')]
	noiseTexTiling: AleVector2
	tile: float_nan
	noiseTexOffset: AleVector2
	isDistortionNoiseTexOffsetRandom: bool
	direction: AleVector2
	directionSpeedMultiplier: float_nan
	isDirectionSpeedMultiplierRandom: bool
	directionSpeedMultiplierRandomRatio: float_nan
	strength: float_nan
	distortionDirection: AleVector2
	linkToWind: bool
	maskTexID: int

