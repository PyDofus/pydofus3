from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Interfaces.IAdminSelectionEntryType import IAdminSelectionEntryType
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Item.ItemData import ItemData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.i18n import i18n
from typing import Union, Annotated

class ItemTypeData(IAdminSelectionEntryType, D2oData):
	bundle_name: ClassVar[str] = "itemtypesdataroot"

	id: int
	nameId: i18n
	superTypeId: int
	categoryId: Annotated[Union[ItemData.ItemCategoryEnum, int], Field(union_mode='left_to_right')]
	isInEncyclopedia: bool
	rawZone: str
	craftXpRatio: int
	evolutiveTypeId: int

