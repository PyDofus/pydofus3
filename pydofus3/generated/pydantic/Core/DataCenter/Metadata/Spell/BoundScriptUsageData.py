from pydofus3.not_generated.base import MyBaseModel


class BoundScriptUsageData(MyBaseModel):
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

