from typing import ClassVar

from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n


class IdleData(D2oData):
    bundle_name: ClassVar[str] = "idlesdataroot"

    nameId: i18n
    animationKey: str
    known: int
    iconIdMale: str
    iconIdFemale: str
    order: int
    criterion: str
    breed: int
