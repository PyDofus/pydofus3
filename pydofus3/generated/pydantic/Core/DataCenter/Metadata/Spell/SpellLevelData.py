from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.Instance.EffectInstanceDice import EffectInstanceDice
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.PreviewSpellZoneDescr import PreviewSpellZoneDescr
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellLevelFlags import SpellLevelFlags
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class SpellLevelData(D2oData):
	bundle_name: ClassVar[str] = "spelllevelsdataroot"

	m_flags: SpellLevelFlags
	id: int
	spellId: int
	grade: int
	spellBreed: int
	apCost: int
	minRange: int
	range: int
	criticalHitProbability: int
	maxStack: int
	maxCastPerTurn: int
	maxCastPerTarget: int
	maxGlobalCastPerTurn: int
	maxGlobalCastPerTarget: int
	minCastInterval: int
	initialCooldown: int
	globalCooldown: int
	minPlayerLevel: int
	statesCriterion: str
	effects: list[EffectInstanceDice]
	criticalEffect: list[EffectInstanceDice]
	previewZones: list[PreviewSpellZoneDescr]

