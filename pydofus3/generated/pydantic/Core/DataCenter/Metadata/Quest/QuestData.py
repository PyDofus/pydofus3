from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Quest.NpcMapIdPairData import NpcMapIdPairData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Quest.QuestType import QuestType
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import Annotated, Union
from typing import ClassVar

class QuestData(D2oData):
	bundle_name: ClassVar[str] = "questsdataroot"

	id: int
	nameId: i18n
	categoryId: int
	repeatType: int
	type: Annotated[Union[QuestType, int], Field(union_mode='left_to_right')]
	repeatLimit: int
	isDungeonQuest: bool
	levelMin: int
	levelMax: int
	stepIds: list[int]
	isPartyQuest: bool
	startCriterion: str
	followable: bool
	isEvent: bool
	startPosition: list[NpcMapIdPairData]

