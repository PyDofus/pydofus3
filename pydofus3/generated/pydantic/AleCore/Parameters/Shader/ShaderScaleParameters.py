from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.ShaderAnimationCurveType import ShaderAnimationCurveType
from pydofus3.generated.pydantic.AleCore.Parameters.Shader.IShaderParameters import IShaderParameters
from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class ShaderScaleParameters(IShaderParameters):
	animationCurveType: Annotated[Union[ShaderAnimationCurveType, int], Field(union_mode='left_to_right')]
	axes: AleVector2
	pivot: AleVector2
	frequency: float_nan
	linkFrequencyToWind: bool
	amplitude: float_nan
	linkAmplitudeToWind: bool
	offset: float_nan
	timeOffset: float_nan
	isTimeOffsetRandom: bool
	shouldSmooth: bool
	shouldApplyNoise: bool
	noiseTexID: int
	noiseStrength: AleVector2
	noiseStrengthMultiplier: float_nan
	linkNoiseStrengthToWind: bool
	noiseOffset: AleVector2
	noiseSpeed: float_nan
	linkNoiseSpeedToWind: bool

