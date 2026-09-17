from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellStateEffectsData import SpellStateEffectsData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class SpellStateData(D2oData):
	bundle_name: ClassVar[str] = "spellstatesdataroot"

	id: int
	nameId: i18n
	descriptionId: int
	preventsSpellCast: bool
	preventsFight: bool
	isSilent: bool
	cantBeMoved: bool
	cantBePushed: bool
	cantDealDamage: bool
	invulnerable: bool
	cantSwitchPosition: bool
	incurable: bool
	effects: list[SpellStateEffectsData]
	icon: str
	iconVisibilityMask: int
	invulnerableMelee: bool
	invulnerableRange: bool
	cantTackle: bool
	cantBeTackled: bool
	displayTurnRemaining: bool
	isMainState: bool
	spellLevelId: int

