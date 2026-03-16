from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Item.ItemData import ItemData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import Annotated, Union
from typing import ClassVar

class ItemTypeData(D2oData):
	bundle_name: ClassVar[str] = "itemtypesdataroot"

	id: int
	nameId: i18n
	superTypeId: int
	categoryId: Annotated[Union[ItemData.ItemCategoryEnum, int], Field(union_mode='left_to_right')]
	isInEncyclopedia: bool
	rawZone: str
	craftXpRatio: int
	evolutiveTypeId: int

