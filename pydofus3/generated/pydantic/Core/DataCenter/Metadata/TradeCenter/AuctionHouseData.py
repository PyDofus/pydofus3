from typing import ClassVar

from pydofus3.not_generated.base import D2oData


class AuctionHouseData(D2oData):
    bundle_name: ClassVar[str] = "auctionhousesdataroot"

    id: int
    typeId: int
