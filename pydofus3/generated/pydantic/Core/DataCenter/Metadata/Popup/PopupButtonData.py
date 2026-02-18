from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class PopupButtonData(MyBaseModel):
	id: int
	popupId: int
	type: int
	textId: i18n
	actionType: int
	actionValue: str

