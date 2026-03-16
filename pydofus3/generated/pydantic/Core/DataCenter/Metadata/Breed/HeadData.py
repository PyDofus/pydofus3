from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class HeadData(D2oData):
	bundle_name: ClassVar[str] = "headsdataroot"

	id: int
	skins: str
	assetId: str
	breed: int
	gender: int
	label: str
	order: int
	payable: bool
	availableAtCreation: bool
	nameId: i18n

	class SortHeadsByOrder(MyBaseModel):
		pass

