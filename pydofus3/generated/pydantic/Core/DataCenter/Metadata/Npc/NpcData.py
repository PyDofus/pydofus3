from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Npc.AnimFunNpcData import AnimFunNpcData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Npc.NpcDialogData import NpcDialogData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import WrappedList
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class NpcData(D2oData):
	bundle_name: ClassVar[str] = "npcsdataroot"

	id: int
	nameId: i18n
	dialogMessages: list[WrappedList[int]]
	dialogReplies: list[WrappedList[int]]
	actions: list[int]
	gender: int
	look: str
	animFunList: list[AnimFunNpcData]
	fastAnimsFun: bool
	tooltipVisible: bool
	dialogData: list[NpcDialogData]
	defaultSkinId: int

