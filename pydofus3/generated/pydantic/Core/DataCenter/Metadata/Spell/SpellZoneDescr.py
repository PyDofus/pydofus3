from pydantic import Field
from pydofus3.generated.pydantic.Metadata.Enums.SpellZoneShape import SpellZoneShape
from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import OpenAPIIntEnum

from typing import Union, Annotated

class SpellZoneDescr(MyBaseModel):
	cellIds: list[int]
	shape: Annotated[Union[SpellZoneShape, int], Field(union_mode='left_to_right')]
	param1: int
	param2: int
	damageDecreaseStepPercent: int
	maxDamageDecreaseApplyCount: int
	isStopAtTarget: bool
	forcedDirection: bool
	includeCarried: bool
	onlyAffectIfInSightLine: bool
	class SpellZoneFormat(MyBaseModel):
		pass
	class SpellZoneParamOrder(MyBaseModel):
		slots: list[Annotated[Union['SpellZoneDescr.SpellZoneParameter', int], Field(union_mode='left_to_right')]]
		slotsCount: int
		defaultParam2: int
		isCustom: bool
		isPoint: bool
	class SpellZoneParameter(OpenAPIIntEnum):
		Param1 = 0
		Param2 = 1
		DamageDecreaseStepPercent = 2
		MaxDamageDecreaseApplyCount = 3
		IsStopAtTarget = 4
		IncludeCarried = 5
		ForcedDirection = 6
		OnlyAffectIfInSightLine = 7

