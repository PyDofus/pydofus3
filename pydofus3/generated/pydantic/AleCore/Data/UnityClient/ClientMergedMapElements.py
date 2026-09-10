from pydofus3.generated.pydantic.AleCore.Data.UnityClient.ClientMapElement import ClientMapElement
from pydofus3.not_generated.base import MyBaseModel

class ClientMergedMapElements(MyBaseModel):
	mapElements: list[ClientMapElement]
	materialIndex: int
	shaderVariantIndex: int
	isStagingTarget: bool
	stagingId: str
	uniqueMaterialInstance: bool
	displayOrder: int
	hasWind: bool
	hasWave: bool
	hasAtlasVertex: bool

