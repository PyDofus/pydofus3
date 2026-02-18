from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class CreatureBoneOverrideData(D2oData):
	bundle_name: ClassVar[str] = "creaturebonesoverridesdataroot"

	boneId: int
	creatureBoneId: int

