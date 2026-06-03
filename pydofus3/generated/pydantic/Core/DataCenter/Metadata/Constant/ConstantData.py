from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class ConstantData(D2oData):
	bundle_name: ClassVar[str] = "constantsdataroot"

	id: int
	value: str

