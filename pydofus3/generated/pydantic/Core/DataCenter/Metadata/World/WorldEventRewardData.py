from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import float_nan

class WorldEventRewardData(D2oData):
	bundle_name: ClassVar[str] = "worldeventsrewardsdataroot"

	worldEventRewardId: int
	objects: str
	emotes: str
	spells: str
	titles: str
	ornaments: str
	rankingConditions: str
	criterions: str
	experience: float_nan
	kamas: float_nan
	gameaction: int
	guildPoints: int
	isForTeam: bool
	order: int
	class ItemAndQuantity(MyBaseModel):
		itemId: int
		quantity: int

