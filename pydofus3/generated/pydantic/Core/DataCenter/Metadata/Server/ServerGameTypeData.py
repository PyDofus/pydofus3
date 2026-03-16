from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class ServerGameTypeData(D2oData):
	bundle_name: ClassVar[str] = "servergametypesdataroot"

	id: int
	selectableByPlayer: bool
	nameId: i18n
	rulesId: i18n
	descriptionId: i18n

