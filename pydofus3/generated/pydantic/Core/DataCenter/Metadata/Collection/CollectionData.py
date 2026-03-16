from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Collection.CollectableData import CollectableData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class CollectionData(D2oData):
	bundle_name: ClassVar[str] = "collectionsdataroot"

	typeId: int
	name: str
	criterion: str
	collectables: list[CollectableData]

