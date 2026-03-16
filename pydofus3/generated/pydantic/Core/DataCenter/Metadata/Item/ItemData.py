from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.Instance.EffectInstanceDice import EffectInstanceDice
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Item.ItemFlags import ItemFlags
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import OpenAPIIntEnum
from pydofus3.not_generated.base import WrappedList
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class ItemData(D2oData):
	bundle_name: ClassVar[str] = "itemsdataroot"

	m_flags: ItemFlags
	id: int
	nameId: i18n
	typeId: int
	descriptionId: i18n
	iconId: int
	level: int
	realWeight: int
	price: float_nan
	itemSetId: int
	criterions: str
	criterionsTarget: str
	appearanceId: int
	isColorable: bool
	recipeSlots: int
	recipeIds: list[int]
	dropMonsterIds: list[int]
	dropTemporisMonsterIds: list[int]
	possibleEffects: list[EffectInstanceDice]
	evolutiveEffectIds: list[int]
	favoriteSubAreas: list[int]
	favoriteSubAreasBonus: int
	craftXpRatio: int
	craftVisibleCriterion: str
	craftConditionalCriterion: str
	craftFeasibleCriterion: str
	visibilityCriterion: str
	recyclingNuggets: float_nan
	favoriteRecyclingSubareas: list[int]
	resourcesBySubarea: list[WrappedList[int]]
	importantNoticeId: i18n

	class ItemCategoryEnum(OpenAPIIntEnum):
		None_ = -2
		All = -1
		Equipment = 0
		Consumables = 1
		Resources = 2
		Quest = 3
		Other = 4
		Cosmetics = 5
		Favorites = 6
		Box1 = 7
		Box2 = 8
		Box3 = 9
		Box4 = 10
		Box5 = 11
		Box6 = 12
		Box7 = 13
		Box8 = 14
		Titles = 15
		Ornaments = 16
		Auras = 17
		EcaflipCard = 238

