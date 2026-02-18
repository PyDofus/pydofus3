from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class SpellBombData(D2oData):
	bundle_name: ClassVar[str] = "spellbombsdataroot"

	id: int
	chainReactionSpellId: int
	explodSpellId: int
	wallId: int
	instantSpellId: int
	comboCoeff: int

