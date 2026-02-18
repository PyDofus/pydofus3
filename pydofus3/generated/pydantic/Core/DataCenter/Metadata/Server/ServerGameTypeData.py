from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class ServerGameTypeData(D2oData):
	bundle_name: ClassVar[str] = "servergametypesdataroot"

	id: int
	selectableByPlayer: bool
	nameId: i18n
	rulesId: i18n
	descriptionId: i18n

