from pydofus3.generated.pydantic.AleCore.Data.AleAlphaKey import AleAlphaKey
from pydofus3.generated.pydantic.AleCore.Data.AleColorKey import AleColorKey
from pydofus3.not_generated.base import MyBaseModel

class AleGradient(MyBaseModel):
	colorKeys: list[AleColorKey]
	alphaKeys: list[AleAlphaKey]

