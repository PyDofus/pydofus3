from enum import IntFlag

# Core.DataCenter.Metadata.Spell.GfxAnimationEndPolicy
class GfxAnimationEndPolicy(IntFlag):
    Unknown = 0
    SameAsSequence = 1
    Beginning = 2
    Shot = 3
    End = 4

# Core.DataCenter.Metadata.Spell.ParallelExecutionEndPolicy
class ParallelExecutionEndPolicy(IntFlag):
    Unknown = 0
    WaitForFirstOne = 1
    WaitForAll = 2
    DontWait = 3

# Core.DataCenter.Metadata.Spell.ProjectileDirectionType
class ProjectileDirectionType(IntFlag):
    Unknown = -1
    Normal = 0
    Random = 1
    Oriented = 2

# Core.DataCenter.Metadata.Spell.ProjectileStrata
class ProjectileStrata(IntFlag):
    Background = 0
    Front = 1
    Highest = 2

# Core.DataCenter.Metadata.Spell.SpellFlags
class SpellFlags(IntFlag):
    VerboseCast = 1
    BypassSummoningLimit = 2
    CanAlwaysTriggerSpells = 4
    HideCastConditions = 8

# Core.DataCenter.Metadata.Spell.SpellLevelFlags
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

# Core.DataCenter.Metadata.Spell.SpellScriptGfxType
class SpellScriptGfxType(IntFlag):
    Unknown = 0
    Caster = 1
    Target = 2
    Projectile = 3
    Trail = 4
    Mark = 5
    Cast = 6
    Staging = 7

# Core.DataCenter.Metadata.Spell.SpellZoneDescr
class SpellZoneDescr(IntFlag):
    Param1 = 0
    Param2 = 1
    DamageDecreaseStepPercent = 2
    MaxDamageDecreaseApplyCount = 3
    IsStopAtTarget = 4
    IncludeCarried = 5
    ForcedDirection = 6
    OnlyAffectIfInSightLine = 7

