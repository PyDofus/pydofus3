from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class ServerPopulationData(D2oData):
	bundle_name: ClassVar[str] = "serverpopulationsdataroot"

	id: int
	nameId: i18n
	weight: int

