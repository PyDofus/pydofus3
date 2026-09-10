from pydofus3.generated.pydantic.AleCore.Data.UnityClient.AtlasDictionary import AtlasDictionary
from pydofus3.not_generated.base import MyBaseModel

class ElementAtlas(MyBaseModel):
	width: int
	height: int
	idsToRects: AtlasDictionary

