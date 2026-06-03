from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class AuctionHouseData(D2oData):
	bundle_name: ClassVar[str] = "auctionhousesdataroot"

	id: int
	typeId: int
	allowedQuantities: list[int]

