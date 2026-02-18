from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class EmoticonData(D2oData):
	bundle_name: ClassVar[str] = "emoticonsdataroot"

	id: int
	nameId: i18n
	shortcutId: i18n
	order: int
	animName: str
	persistancy: bool
	persistantAnimName: str
	eightDirections: bool
	aura: bool
	cooldown: int
	duration: int
	weight: int
	spellLevelId: int
	scale: int
	allowOnMount: bool
	criterion: str

