from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Popup.PopupButtonData import PopupButtonData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class PopupInformationData(D2oData):
	bundle_name: ClassVar[str] = "popupsinformationdataroot"

	id: int
	parentId: int
	titleId: i18n
	headerId: str
	descriptionId: i18n
	illuName: str
	buttons: list[PopupButtonData]
	criterion: str
	cacheType: int
	autoTrigger: bool

