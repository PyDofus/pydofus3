from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import WrappedList
from typing import ClassVar

class LivingObjectSkinMoodsData(D2oData):
	bundle_name: ClassVar[str] = "livingobjectskinsmoodsdataroot"

	skinId: int
	moods: list[WrappedList[int]]

