from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.ShaderAnimationCurveType import ShaderAnimationCurveType
from pydofus3.generated.pydantic.AleCore.Parameters.Shader.IShaderParameters import IShaderParameters
from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class ShaderRotationParameters(IShaderParameters):
	animationCurveType: Annotated[Union[ShaderAnimationCurveType, int], Field(union_mode='left_to_right')]
	rotationCenter: AleVector2
	frequency: float_nan
	linkFrequencyToWind: bool
	amplitude: float_nan
	linkAmplitudeToWind: bool
	offset: float_nan
	isOffsetLinkedToMapNoiseModifier: bool
	timeOffset: float_nan
	isTimeOffsetRandom: bool
	shouldSmooth: bool
	shouldApplyNoise: bool
	noiseTexID: int
	noiseStrength: float_nan
	linkNoiseStrengthToWind: bool
	noiseSpeed: float_nan
	linkNoiseSpeedToWind: bool
	noiseOffset: AleVector2
	isNoiseOffsetRandom: bool

