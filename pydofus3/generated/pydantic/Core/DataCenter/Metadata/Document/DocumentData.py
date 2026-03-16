from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class DocumentData(D2oData):
	bundle_name: ClassVar[str] = "documentsdataroot"

	PageFeed: ClassVar[str] = "<pagefeed/>"
	id: int
	typeId: int
	showTitle: bool
	showBackgroundImage: bool
	titleId: i18n
	authorId: i18n
	subTitleId: i18n
	contentId: i18n
	contentCSS: str
	clientProperties: str

