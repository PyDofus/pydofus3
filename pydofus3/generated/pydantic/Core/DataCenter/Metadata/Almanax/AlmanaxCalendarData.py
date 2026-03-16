from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class AlmanaxCalendarData(D2oData):
	bundle_name: ClassVar[str] = "almanaxcalendarsdataroot"

	id: int
	nameId: i18n
	descId: i18n
	npcId: int
	categoryId: int
	bonusesIds: list[int]
	dates: list[str]
	objectiveId: int
	meridiaDescriptionId: i18n
	meridiaEffectId: i18n
	rubrikabraxId: i18n
	meridiaIllustrationId: int
	celebrationNameId: i18n
	celebrationDescriptionId: i18n

