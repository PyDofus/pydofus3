from typing import ClassVar

from pydofus3.not_generated.base import D2oData, MyBaseModel
from pydofus3.not_generated.i18n import i18n


class HeadData(D2oData):
    bundle_name: ClassVar[str] = "headsdataroot"

    id: int
    skins: str
    assetId: str
    breed: int
    gender: int
    label: str
    order: int
    payable: bool
    availableAtCreation: bool
    nameId: i18n

    class SortHeadsByOrder(MyBaseModel):
        pass
