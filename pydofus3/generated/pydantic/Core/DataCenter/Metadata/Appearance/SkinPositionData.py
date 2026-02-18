from pydofus3.generated.pydantic.Core.DataCenter.Types.TransformData import TransformData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class SkinPositionData(D2oData):
	bundle_name: ClassVar[str] = "skinpositionsdataroot"

	id: int
	transformation: list[TransformData]
	clip: list[str]
	skin: list[int]

