from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.ShaderAnimationCurveType import ShaderAnimationCurveType
from pydofus3.generated.pydantic.AleCore.Parameters.Shader.IShaderParameters import IShaderParameters
from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class ShaderColorAnimationParameters(IShaderParameters):
	animationCurveType: Annotated[Union[ShaderAnimationCurveType, int], Field(union_mode='left_to_right')]
	finalColor: AleColor
	isFinalColorLinkedToMapNoiseModifier: bool
	finalColorModifier: AleColor
	frequency: float_nan
	linkFrequencyToWind: bool
	timeOffset: float_nan
	isTimeOffsetRandom: bool
	shouldSmooth: bool
	shouldApplyNoise: bool
	noiseTexID: int
	noiseOffset: AleVector2
	isNoiseOffsetRandom: bool
	noiseStrength: float_nan
	linkNoiseStrengthToWind: bool
	noiseSpeed: float_nan
	linkNoiseSpeedToWind: bool

