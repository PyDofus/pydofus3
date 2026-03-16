from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Interactive.SignData import SignData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class SignsData(D2oData):
	bundle_name: ClassVar[str] = "signsdataroot"

	signs: list[SignData]

