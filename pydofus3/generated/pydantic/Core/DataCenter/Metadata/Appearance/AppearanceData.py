from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class AppearanceData(D2oData):
	bundle_name: ClassVar[str] = "appearancesdataroot"

	id: int
	type: int
	data: str
	usePlayerLook: bool

