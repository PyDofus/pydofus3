from enum import IntEnum
from enum import IntFlag

class GfxAnimationEndPolicy(IntEnum):
	Unknown = 0
	SameAsSequence = 1
	Beginning = 2
	Shot = 3
	End = 4

class ParallelExecutionEndPolicy(IntEnum):
	Unknown = 0
	WaitForFirstOne = 1
	WaitForAll = 2
	DontWait = 3

class ProjectileDirectionType(IntEnum):
	Unknown = -1
	Normal = 0
	Random = 1
	Oriented = 2

class ProjectileStrata(IntEnum):
	Background = 0
	Front = 1
	Highest = 2

class SpellFlags(IntFlag):
	VerboseCast = 1
	BypassSummoningLimit = 2
	CanAlwaysTriggerSpells = 4
	HideCastConditions = 8

class SpellLevelFlags(IntFlag):
	CastInLine = 1
	CastInDiagonal = 2
	CastTestLos = 4
	NeedFreeCell = 8
	NeedTakenCell = 16
	NeedFreeTrapCell = 32
	RangeCanBeBoosted = 64
	HideEffects = 128
	Hidden = 256
	PlayAnimation = 512
	NeedVisibleEntity = 1024
	NeedCellWithoutPortal = 2048
	PortalProjectionForbidden = 4096
	ProportionalDiagonal = 8192

class SpellScriptGfxType(IntEnum):
	Unknown = 0
	Caster = 1
	Target = 2
	Projectile = 3
	Trail = 4
	Mark = 5
	Cast = 6
	Staging = 7

class SpellZoneDescr:
	class SpellZoneParameter(IntEnum):
		Param1 = 0
		Param2 = 1
		DamageDecreaseStepPercent = 2
		MaxDamageDecreaseApplyCount = 3
		IsStopAtTarget = 4
		IncludeCarried = 5
		ForcedDirection = 6
		OnlyAffectIfInSightLine = 7

