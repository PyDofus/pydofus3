from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Ride.PaddockTierData import PaddockTierData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class PaddockGaugesData(D2oData):
	bundle_name: ClassVar[str] = "paddockgaugesdataroot"

	id: int
	name: str
	tierMaxValues: list[PaddockTierData]
	m_tierMaxValuesDictionary: dict[int, int]

