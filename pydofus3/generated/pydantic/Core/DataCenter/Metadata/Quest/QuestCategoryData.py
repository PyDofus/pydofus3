from pydofus3.generated.pydantic.Core.DataCenter.Interfaces.IAdminSelectionEntryType import IAdminSelectionEntryType
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.i18n import i18n

class QuestCategoryData(IAdminSelectionEntryType, D2oData):
	bundle_name: ClassVar[str] = "questcategoriesdataroot"

	id: int
	nameId: i18n
	order: int
	questIds: list[int]

