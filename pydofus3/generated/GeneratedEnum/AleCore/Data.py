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
	TranslationFeature = 8
	RotationFeature = 16
	ScaleFeature = 32
	DistortionFeature = 64
	RefractionFeature = 128
	DissolveFeature = 256
	EmissiveFeature = 512
	WindSensitiveFeature = 1024
	Animator2D = 2048
	FlashBlendModeNone = 4096
	FlashBlendModeMultiply = 8192
	FlashBlendModeScreen = 16384
	FlashBlendModeInvert = 32768
	HighlightFeature = 65536
	WindEnabled = 131072
	EnableOutline = 262144
	UseMapNoiseModifier = 524288
	WavesEnabled = 1048576
	WaveSensitiveFeature = 2097152
	HasGroupedFeatured = 8388608
	TextureOffsetFeature = 288230376151711744

class UVModes(IntEnum):
	Normal = 0
	ScreenSpace = 1
	WorldSpace = 2

