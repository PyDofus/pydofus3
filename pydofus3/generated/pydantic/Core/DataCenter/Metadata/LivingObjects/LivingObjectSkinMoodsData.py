from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import WrappedList

class LivingObjectSkinMoodsData(D2oData):
	bundle_name: ClassVar[str] = "livingobjectskinsmoodsdataroot"

	skinId: int
	moods: list[WrappedList[int]]

