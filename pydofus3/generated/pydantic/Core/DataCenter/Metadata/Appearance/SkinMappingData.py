from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class SkinMappingData(D2oData):
	bundle_name: ClassVar[str] = "skinmappingsdataroot"

	id: int
	lowDefId: int

