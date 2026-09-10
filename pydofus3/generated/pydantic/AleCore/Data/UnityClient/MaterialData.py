from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ElementAtlas import ElementAtlas
from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ShaderData import ShaderData
from pydofus3.not_generated.base import MyBaseModel

class MaterialData(MyBaseModel):
	atlas1x: ElementAtlas
	atlas2x: ElementAtlas
	atlas4x: ElementAtlas
	shaderData: list[ShaderData]

