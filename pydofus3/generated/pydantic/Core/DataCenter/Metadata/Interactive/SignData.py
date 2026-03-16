from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.i18n import i18n

class SignData(MyBaseModel):
	id: int
	skillParams: str
	skillId: int
	textKey: i18n
	skillVisibleCriterion: str

