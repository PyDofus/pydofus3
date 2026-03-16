from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class SkillData(D2oData):
	bundle_name: ClassVar[str] = "skillsdataroot"

	id: int
	nameId: i18n
	parentJobId: int
	isForgemagus: bool
	modifiableItemTypeIds: list[int]
	gatheredRessourceItem: int
	craftableItemIds: list[int]
	range: int
	useRangeInClient: bool
	useAnimation: str
	cursor: int
	elementActionId: int
	availableInHouse: bool
	clientDisplay: bool
	levelMin: int
	allowMarking: bool

