from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class SpellStateData(D2oData):
	bundle_name: ClassVar[str] = "spellstatesdataroot"

	id: int
	nameId: i18n
	preventsSpellCast: bool
	preventsFight: bool
	isSilent: bool
	cantBeMoved: bool
	cantBePushed: bool
	cantDealDamage: bool
	invulnerable: bool
	cantSwitchPosition: bool
	incurable: bool
	effectsIds: list[int]
	icon: str
	iconVisibilityMask: int
	invulnerableMelee: bool
	invulnerableRange: bool
	cantTackle: bool
	cantBeTackled: bool
	displayTurnRemaining: bool
	isMainState: bool

