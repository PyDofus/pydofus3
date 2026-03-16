from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class AlignmentTitleData(D2oData):
	bundle_name: ClassVar[str] = "alignmenttitlesdataroot"

	sideId: int
	namesId: list[str]
	shortsId: list[str]

