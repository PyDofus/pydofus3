from pydofus3.generated.pydantic.Core.DataCenter.Metadata.InfiniteDreams.DropData import DropData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class InfiniteDreamDropPoolData(D2oData):
	bundle_name: ClassVar[str] = "infinitedreamdroppoolsdataroot"

	id: int
	drops: list[DropData]

