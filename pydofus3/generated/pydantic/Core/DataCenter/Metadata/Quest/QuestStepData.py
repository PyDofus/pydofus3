from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.i18n import i18n

class QuestStepData(D2oData):
	bundle_name: ClassVar[str] = "queststepsdataroot"

	id: int
	questId: int
	nameId: i18n
	descriptionId: i18n
	dialogId: int
	optimalLevel: int
	duration: float_nan
	objectiveIds: list[int]
	rewardsIds: list[int]

