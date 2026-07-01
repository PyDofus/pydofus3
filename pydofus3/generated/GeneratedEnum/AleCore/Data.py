from enum import IntEnum
from enum import IntFlag

class AleParticleSystemEmitFromBox(IntEnum):
	Volume = 0
	Shell = 1
	Edge = 2

class AleParticleSystemEmitFromCone(IntEnum):
	Base = 0
	Volume = 1

class AleParticleSystemSimulationSpace(IntEnum):
	Local = 0
	World = 1
	Custom = 2

class AleParticleSystemSimulationSpaceRestricted(IntEnum):
	Local = 0
	World = 1
	Custom = 2

class AleParticleSystemSubEmitterProperties(IntFlag):
	InheritNothing = 0
	InheritColor = 1
	InheritSize = 2
	InheritRotation = 4
	InheritLifetime = 8
	InheritDuration = 16
	InheritEverything = 31

class AleParticleSystemSubEmitterType(IntEnum):
	Birth = 0
	Death = 1

class EffectShape(IntEnum):
	Circle = 0
	Rectangle = 1

class EffectsSortingLayer(IntEnum):
	MapBackground = 0
	PaintBackground = 1
	BackEffect = 2
	IsometricBackground = 3
	BackgroundEffect = 4
	IsometricForeground = 5
	ForegroundEffect = 6
	PaintForeground = 7
	FrontEffect = 8
	Default = 9
	UI = 10

class ShaderAnimationCurveType(IntEnum):
	PingPong = 0
	Loop = 1
	Fixed = 2

class ShaderVariantBitfield(IntFlag):
	None_ = 0
	CustomFramerate = 1
	AlphaClip = 2
	ColorAnimationFeature = 4
	TranslationFeature = 64
	RotationFeature = 1024
	ScaleFeature = 16384
	DistortionFeature = 262144
	RefractionFeature = 8388608
	DissolveFeature = 134217728
	EmissiveFeature = 8589934592
	WindSensitiveFeature = 68719476736
	Animator2D = 1099511627776
	FlashBlendModeNone = 8796093022208
	FlashBlendModeMultiply = 17592186044416
	FlashBlendModeScreen = 35184372088832
	FlashBlendModeInvert = 70368744177664
	HighlightFeature = 140737488355328
	WindEnabled = 281474976710656
	EnableOutline = 562949953421312
	UseMapNoiseModifier = 4503599627370496
	WavesEnabled = 72057594037927936
	WaveSensitiveFeature = 144115188075855872
	TextureOffsetFeature = 288230376151711744

class UVModes(IntEnum):
	Normal = 0
	ScreenSpace = 1
	WorldSpace = 2

