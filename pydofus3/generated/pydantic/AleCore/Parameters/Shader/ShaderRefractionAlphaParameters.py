from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.UVModes import UVModes
from pydofus3.generated.pydantic.AleCore.Parameters.Shader.IShaderParameters import IShaderParameters
from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class ShaderRefractionAlphaParameters(IShaderParameters):
	noiseTexID: int
	noiseTexUVMode: Annotated[Union[UVModes, int], Field(union_mode='left_to_right')]
	noiseTexTiling: AleVector2
	tile: float_nan
	noiseTexOffset: AleVector2
	direction: AleVector2
	directionSpeedMultiplier: float_nan
	isDirectionSpeedMultiplierRandom: bool
	directionSpeedMultiplierRandomRatio: float_nan
	strength: float_nan
	maskTexID: int
	color: AleColor
	alphaMultiplier: float_nan

