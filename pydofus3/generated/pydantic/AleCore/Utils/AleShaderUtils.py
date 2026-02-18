from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import OpenAPIIntEnum

from pydofus3.not_generated.unity import BlendMode
from pydofus3.not_generated.unity import BlendOp

class AleShaderUtils(MyBaseModel):
	pass
	class AleBlending(MyBaseModel):
		sourceFactor: BlendMode
		blendOperation: BlendOp
		destinationFactor: BlendMode
	class BlendingPatterns(OpenAPIIntEnum):
		Normal = 0
		Addition = 1
		LumiereVive = 2
		Incrustation = 3
		Produit = 4
		Assombrir = 5
		Soustraction = 6
	class RenderingLayerMask(OpenAPIIntEnum):
		DEFAULT = 1
		REFRACTION = 2
		INLINE = 4
		OUTLINE = 8
		WAVE = 16
	class ShaderTypeEnum(OpenAPIIntEnum):
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

