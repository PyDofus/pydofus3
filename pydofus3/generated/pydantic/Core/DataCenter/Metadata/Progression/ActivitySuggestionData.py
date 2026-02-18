from typing import ClassVar

from pydofus3.not_generated.base import D2oData, float_nan
from pydofus3.not_generated.i18n import i18n


class ActivitySuggestionData(D2oData):
    bundle_name: ClassVar[str] = "activitysuggestionsdataroot"

    id: int
    nameId: i18n
    descriptionId: i18n
    categoryId: int
    level: int
    mapId: int
    isLarge: bool
    startDate: float_nan
    endDate: float_nan
    icon: str
    iconCategoryId: int
