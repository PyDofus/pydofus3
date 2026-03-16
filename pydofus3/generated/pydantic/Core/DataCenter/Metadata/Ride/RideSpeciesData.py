from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class RideSpeciesData(D2oData):
	bundle_name: ClassVar[str] = "ridespeciesdataroot"

	id: int
	nameId: int
	extractionRewardGid: int

