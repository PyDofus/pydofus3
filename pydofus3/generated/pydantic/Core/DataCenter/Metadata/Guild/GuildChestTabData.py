from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class GuildChestTabData(D2oData):
	bundle_name: ClassVar[str] = "guildchesttabsdataroot"

	tabId: int
	nameId: i18n
	index: int
	gfxId: int
	serverType: int
	cost: int
	seniority: int
	openRight: int
	dropRight: int
	takeRight: int

