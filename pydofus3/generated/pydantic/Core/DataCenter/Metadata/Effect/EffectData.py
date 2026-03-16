from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class EffectData(D2oData):
	bundle_name: ClassVar[str] = "effectsdataroot"

	id: int
	descriptionId: i18n
	iconId: int
	characteristic: int
	category: int
	characteristicOperator: str
	showInTooltip: bool
	useDice: bool
	forceMinMax: bool
	boost: bool
	active: bool
	oppositeId: int
	theoreticalDescriptionId: i18n
	theoreticalPattern: int
	showInSet: bool
	bonusType: int
	useInFight: bool
	effectPriority: int
	effectPowerRate: float_nan
	elementId: int
	isInPercent: bool
	hideValueInTooltip: bool
	textIconReferenceId: int
	effectTriggerDuration: int
	actionFiltersId: list[int]

