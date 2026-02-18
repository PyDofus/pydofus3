from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.EffectInstanceData import EffectInstanceData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.IDataCenter import IDataCenter
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Mount.MountAncestorData import MountAncestorData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Mount.MountBehaviorData import MountBehaviorData
from typing import Any
from typing import Iterable

class MountInstance(IDataCenter):
	name: str
	description: str
	entityLook: Any
	colors: Iterable[int]
	sex: bool
	level: int
	ownerId: int
	experience: int
	experienceForLevel: int
	experienceForNextLevel: int
	xpRatio: int
	maxPods: int
	isRideable: bool
	isWild: bool
	borning: bool
	energy: int
	energyMax: int
	stamina: int
	staminaMax: int
	maturity: int
	maturityForAdult: int
	serenity: int
	serenityMax: int
	aggressivityMax: int
	love: int
	loveMax: int
	fecondationTime: int
	isFecondationReady: bool
	reproductionCount: int
	reproductionCountMax: int
	boostLimiter: int
	boostMax: int
	harnessGID: int
	useHarnessColors: bool
	effectList: list[EffectInstanceData]
	ancestor: MountAncestorData
	ability: list[MountBehaviorData]

