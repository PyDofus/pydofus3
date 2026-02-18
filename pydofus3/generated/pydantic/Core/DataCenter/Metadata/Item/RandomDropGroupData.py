from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Item.RandomDropItemData import RandomDropItemData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class RandomDropGroupData(D2oData):
	bundle_name: ClassVar[str] = "randomdropgroupsdataroot"

	id: int
	randomDropItems: list[RandomDropItemData]
	displayChances: bool

