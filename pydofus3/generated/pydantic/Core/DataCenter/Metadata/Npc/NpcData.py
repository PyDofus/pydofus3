from pydofus3.generated.pydantic.Core.DataCenter.Interfaces.IAdminSelectionEntry import IAdminSelectionEntry
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Npc.AnimFunNpcData import AnimFunNpcData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Npc.NpcDialogData import NpcDialogData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import WrappedList
from pydofus3.not_generated.i18n import i18n

class NpcData(IAdminSelectionEntry, D2oData):
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

