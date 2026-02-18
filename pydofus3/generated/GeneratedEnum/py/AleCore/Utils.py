from enum import IntFlag

# AleCore.Utils.AleShaderUtils
class AleShaderUtils(IntFlag):
    DEFAULT = 1
    REFRACTION = 2
    INLINE = 4
    OUTLINE = 8
    WAVE = 16

# AleCore.Utils.AleShaderUtils
class AleShaderUtils(IntFlag):
    All = 0
    Blending = 1
    CustomFramerate = 2
    DepthAlphaClip = 3
    Distortion = 4
    Refraction = 5
    Wind = 6
    ColorAnimation = 7
    TextureOffset = 8
    Translation = 9
    Rotation = 10
    Scale = 11
    Dissolve = 12
    Emissive = 13
    Wave = 14

# AleCore.Utils.AleShaderUtils
class AleShaderUtils(IntFlag):
    Normal = 0
    Addition = 1
    LumiereVive = 2
    Incrustation = 3
    Produit = 4
    Assombrir = 5
    Soustraction = 6

# AleCore.Utils.FilmGrainType
class FilmGrainType(IntFlag):
    Thin1 = 0
    Thin2 = 1
    Medium1 = 2
    Medium2 = 3
    Medium3 = 4
    Medium4 = 5
    Medium5 = 6
    Medium6 = 7
    Large1 = 8
    Large2 = 9

# AleCore.Utils.ObjectDisplayBehaviour
class ObjectDisplayBehaviour(IntFlag):
    ALWAYS_DISPLAY = 0
    HIDE_IF_IGNORE_EFFECTS = 1
    HIDE_IF_EFFECTS = 2

# AleCore.Utils.OutlineTestDiff
class OutlineTestDiff(IntFlag):
    CROSS_2_SIDES = 0
    CROSS_FROM_CENTER = 1
    CROSS_AROUND = 2
    OUTLINE_MASK = 3

# AleCore.Utils.OutlineType
class OutlineType(IntFlag):
    INLINE = 0
    OUTLINE = 1
    HIGHLIGHT = 2

# AleCore.Utils.TextureOffsetType
class TextureOffsetType(IntFlag):
    DIRECTION = 0
    FLOWMAP = 1

# AleCore.Utils.WindSensitiveTypeTest
class WindSensitiveTypeTest(IntFlag):
    MANUAL = 0
    NOISE_FIXED = 1
    NOISE_DYNAMIC = 2

