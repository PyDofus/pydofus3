from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class RideFoodData(D2oData):
	bundle_name: ClassVar[str] = "ridefoodsdataroot"

	gid: int
	typeId: int
	familyId: int

