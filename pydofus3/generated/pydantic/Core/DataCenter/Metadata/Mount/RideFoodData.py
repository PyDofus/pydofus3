from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class RideFoodData(D2oData):
	bundle_name: ClassVar[str] = "ridefoodsdataroot"

	gid: int
	typeId: int
	familyId: int

