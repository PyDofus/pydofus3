from enum import IntEnum

class AleShaderUtils:
	class ShaderFeatureTypeEnum(IntEnum):
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

	class BlendingPatterns(IntEnum):
		Normal = 0
		Addition = 1
		LumiereVive = 2
		Incrustation = 3
		Produit = 4
		Assombrir = 5
		Soustraction = 6

class FilmGrainType(IntEnum):
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

class ObjectDisplayBehaviour(IntEnum):
	ALWAYS_DISPLAY = 0
	HIDE_IF_IGNORE_EFFECTS = 1
	HIDE_IF_EFFECTS = 2

class OutlineTestDiff(IntEnum):
	CROSS_2_SIDES = 0
	CROSS_FROM_CENTER = 1
	CROSS_AROUND = 2
	OUTLINE_MASK = 3

class OutlineType(IntEnum):
	INLINE = 0
	OUTLINE = 1
	HIGHLIGHT = 2

class TextureOffsetType(IntEnum):
	DIRECTION = 0
	FLOWMAP = 1

class WindSensitiveTypeTest(IntEnum):
	MANUAL = 0
	NOISE_FIXED = 1
	NOISE_DYNAMIC = 2

