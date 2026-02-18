from pydantic import Field
from pydofus3.generated.pydantic.AleCore.Data.AleColor import AleColor
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.generated.pydantic.AleCore.Data.AleVector2 import AleVector2
from pydofus3.generated.pydantic.AleCore.Data.ShaderAnimationCurveType import ShaderAnimationCurveType
from pydofus3.generated.pydantic.AleCore.Parameters.Shader.IShaderParameters import IShaderParameters
from pydofus3.not_generated.base import float_nan
from typing import Union, Annotated

class ShaderDissolveParameters(IShaderParameters):
	dissolveTexID: int
	dissolveTexTiling: AleVector2
	dissolveTexOffset: AleVector2
	isDissolveTexOffsetRandom: bool
	dissolveTexSpeed: AleVector2
	texSpeedMultiplier: float_nan
	isTexSpeedMultiplierRandom: bool
	texSpeedMultiplierRandomRatio: float_nan
	dissolveMaskID: int
	alphaClip: float_nan
	alphaClipFadeWidth: float_nan
	burnWidth: float_nan
	isBurnWidthLinkedToMapNoiseModifier: bool
	burnColor: AleColor
	isBurnColorLinkedToMapNoiseModifier: bool
	burnColorModifier: AleColor
	burnColorPower: float_nan
	isBurnColorPowerLinkedToMapNoiseModifier: bool
	isBurnFaded: bool
	displayUseDissolvePerParticle: bool
	useDissolvePerParticle: bool
	alphaClipPerParticle: AleMinMaxCurve
	isAnimated: bool
	animationCurveType: Annotated[Union[ShaderAnimationCurveType, int], Field(union_mode='left_to_right')]
	frequency: float_nan
	curveMin: float_nan
	curveMax: float_nan
	shouldSmooth: bool
	shouldApplyNoise: bool
	noiseTexID: int
	noiseStrength: float_nan
	noiseSpeed: float_nan

