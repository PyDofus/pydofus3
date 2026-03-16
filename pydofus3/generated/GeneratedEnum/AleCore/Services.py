from enum import IntEnum

class ShaderFrequencyTypeEnum(IntEnum):
	Translation = 0
	TranslationNoise = 1
	Rotation = 2
	RotationNoise = 3
	Scale = 4
	ScaleNoise = 5
	ColorAnimation = 6
	ColorAnimationNoise = 7
	Dissolve = 8

