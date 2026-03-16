from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class SpellBombWallData(D2oData):
	bundle_name: ClassVar[str] = "spellbombwallsdataroot"

	id: int
	spellId: int
	color: int
	linear: bool
	minHop: int
	maxHop: int

