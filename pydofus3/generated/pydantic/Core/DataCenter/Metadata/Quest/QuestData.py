from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class QuestData(D2oData):
	bundle_name: ClassVar[str] = "questsdataroot"

	id: int
	nameId: i18n
	categoryId: int
	repeatType: int
	repeatLimit: int
	isDungeonQuest: bool
	levelMin: int
	levelMax: int
	stepIds: list[int]
	isPartyQuest: bool
	startCriterion: str
	followable: bool
	isEvent: bool

