from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Constant.ServerValueData import ServerValueData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class ConstantData(D2oData):
	bundle_name: ClassVar[str] = "constantsdataroot"

	id: int
	defaultValue: str
	valueByServer: list[ServerValueData]

