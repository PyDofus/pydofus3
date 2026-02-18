from enum import IntFlag

# AleCore.Services.ShaderFrequencyTypeEnum
class ShaderFrequencyTypeEnum(IntFlag):
    Translation = 0
    TranslationNoise = 1
    Rotation = 2
    RotationNoise = 3
    Scale = 4
    ScaleNoise = 5
    ColorAnimation = 6
    ColorAnimationNoise = 7
    Dissolve = 8

