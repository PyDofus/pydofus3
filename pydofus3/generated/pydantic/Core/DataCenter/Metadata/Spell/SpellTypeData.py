from pydofus3.generated.pydantic.Core.DataCenter.Interfaces.IAdminSelectionEntryType import IAdminSelectionEntryType
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.i18n import i18n

class SpellTypeData(IAdminSelectionEntryType, D2oData):
	bundle_name: ClassVar[str] = "spelltypesdataroot"

	id: int
	longNameId: i18n
	shortNameId: i18n

