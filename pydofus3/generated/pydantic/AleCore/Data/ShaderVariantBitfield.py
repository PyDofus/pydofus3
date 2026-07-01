from pydofus3.not_generated.base import FlagBaseModel
from typing import Annotated

class ShaderVariantBitfield(FlagBaseModel):
	None_ : Annotated[bool,0]
	CustomFramerate : Annotated[bool,1]
	AlphaClip : Annotated[bool,2]
	ColorAnimationFeature : Annotated[bool,4]
	TranslationFeature : Annotated[bool,64]
	RotationFeature : Annotated[bool,1024]
	ScaleFeature : Annotated[bool,16384]
	DistortionFeature : Annotated[bool,262144]
	RefractionFeature : Annotated[bool,8388608]
	DissolveFeature : Annotated[bool,134217728]
	EmissiveFeature : Annotated[bool,8589934592]
	WindSensitiveFeature : Annotated[bool,68719476736]
	Animator2D : Annotated[bool,1099511627776]
	FlashBlendModeNone : Annotated[bool,8796093022208]
	FlashBlendModeMultiply : Annotated[bool,17592186044416]
	FlashBlendModeScreen : Annotated[bool,35184372088832]
	FlashBlendModeInvert : Annotated[bool,70368744177664]
	HighlightFeature : Annotated[bool,140737488355328]
	WindEnabled : Annotated[bool,281474976710656]
	EnableOutline : Annotated[bool,562949953421312]
	UseMapNoiseModifier : Annotated[bool,4503599627370496]
	WavesEnabled : Annotated[bool,72057594037927936]
	WaveSensitiveFeature : Annotated[bool,144115188075855872]
	TextureOffsetFeature : Annotated[bool,288230376151711744]

