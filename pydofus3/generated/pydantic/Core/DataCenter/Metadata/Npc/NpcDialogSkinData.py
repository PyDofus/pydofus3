from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class NpcDialogSkinData(D2oData):
	bundle_name: ClassVar[str] = "npcdialogskinsdataroot"

	id: int
	gfxId: int
	buttonsColorTypes: int
	backgroundColor: str
	isBold: bool
	fontColor: str
	borderColor: str
	hasHalo: bool
	headerGfxId: int
	headerColor: str
	headerFontColor: str
	headerDecorationGfxId: int
	headerDecorationColor: str
	headerOrnamentGfxId: int
	headerOrnamentColor: str

