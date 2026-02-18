from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class ChoiceOptionData(MyBaseModel):
	id: int
	descriptionId: i18n
	rewardType: int
	rewardValue: str
	gfxId: int

