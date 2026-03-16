from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class AlignmentRankGiftsData(D2oData):
	bundle_name: ClassVar[str] = "alignmentranksgiftsdataroot"

	id: int
	gifts: list[int]

