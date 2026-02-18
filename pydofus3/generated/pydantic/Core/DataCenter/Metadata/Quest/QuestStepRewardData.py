from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import WrappedList
from pydofus3.not_generated.base import float_nan

class QuestStepRewardData(D2oData):
	bundle_name: ClassVar[str] = "queststeprewardsdataroot"

	id: int
	stepId: int
	levelMin: int
	levelMax: int
	kamasRatio: float_nan
	experienceRatio: float_nan
	kamasScaleWithPlayerLevel: bool
	itemsReward: list[WrappedList[int]]
	emotesReward: list[int]
	jobsReward: list[int]
	spellsReward: list[int]
	titlesReward: list[int]

