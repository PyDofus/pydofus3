from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class ArenaLeagueData(D2oData):
	bundle_name: ClassVar[str] = "arenaleaguesdataroot"

	id: int
	nameId: i18n
	ornamentId: int
	icon: str
	illus: str
	isLastLeague: bool
	lowRatingBound: int
	highRatingBound: int

