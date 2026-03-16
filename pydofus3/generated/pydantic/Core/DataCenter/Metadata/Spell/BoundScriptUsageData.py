from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class BoundScriptUsageData(MyBaseModel):
	SerialSequenceGroup: ClassVar[int] = 0
	id: int
	order: int
	scriptId: int
	spellLevels: list[int]
	criterion: str
	casterMask: str
	targetMask: str
	targetZone: str
	activationMask: str
	activationZone: str
	random: int
	randomGroup: int
	sequenceGroup: int
	isTargetTreatedAsCaster: bool
	areTargetsAffectedConcurrently: bool

