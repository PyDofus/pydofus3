from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.i18n import i18n

class GuildRaidsVariablesData(MyBaseModel):
	id: int
	raidId: int
	icon: str
	nameId: i18n
	descriptionId: i18n

