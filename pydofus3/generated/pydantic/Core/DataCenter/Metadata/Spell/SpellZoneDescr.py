from pydantic import Field
from pydofus3.generated.pydantic.Metadata.Enums.SpellZoneShape import SpellZoneShape
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union
from typing import ClassVar

class SpellZoneDescr(MyBaseModel):
	DefaultParam1: ClassVar[int] = 1
	DefaultParam2: ClassVar[int] = 0
	DefaultDamageDecreaseStepPercent: ClassVar[int] = 10
	DefaultMaxDamageDecreaseApplyCount: ClassVar[int] = 4
	DefaultForcedDirection: ClassVar[int] = 255
	DefaultIncludeCarried: ClassVar[int] = 0
	DefaultIsStopAtTarget: ClassVar[int] = 0
	DefaultOnlyAffectIfInSightLine: ClassVar[int] = 0
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

	class SpellZoneParameter(OpenAPIIntEnum):
		Param1 = 0
		Param2 = 1
		DamageDecreaseStepPercent = 2
		MaxDamageDecreaseApplyCount = 3
		IsStopAtTarget = 4
		IncludeCarried = 5
		ForcedDirection = 6
		OnlyAffectIfInSightLine = 7

	class SpellZoneParamOrder(MyBaseModel):
		slots: list[Annotated[Union[SpellZoneDescr.SpellZoneParameter, int], Field(union_mode='left_to_right')]]
		slotsCount: int
		defaultParam2: int
		isCustom: bool
		isPoint: bool

	class SpellZoneFormat(MyBaseModel):
		pass

