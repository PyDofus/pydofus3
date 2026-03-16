from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class RideGaugesData(D2oData):
	bundle_name: ClassVar[str] = "ridegaugesdataroot"

	id: int
	maxValue: int
	minMood: int
	maxMood: int

