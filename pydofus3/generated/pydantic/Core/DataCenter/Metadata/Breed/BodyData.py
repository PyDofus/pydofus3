from typing import ClassVar

from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n


class BodyData(D2oData):
    bundle_name: ClassVar[str] = "bodiesdataroot"

    id: int
    skins: str
    assetId: str
    breed: int
    gender: int
    label: str
    order: int
    payable: int
    availableAtCreation: int
    nameId: i18n
