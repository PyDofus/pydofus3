from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class ActivitySuggestionCategoryData(D2oData):
	bundle_name: ClassVar[str] = "activitysuggestioncategoriesdataroot"

	id: int
	nameId: i18n
	parentId: int

