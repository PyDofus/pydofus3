from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.ActionId import ActionId
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.EffectInstanceFlags import EffectInstanceFlags
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellZoneDescr import SpellZoneDescr
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class EffectInstanceData(MyBaseModel):
	m_flags: EffectInstanceFlags
	effectUid: int
	baseEffectId: int
	effectId: Annotated[Union[ActionId, int], Field(union_mode='left_to_right')]
	order: int
	targetId: int
	targetMask: str
	duration: int
	random: float_nan
	group: int
	modificator: int
	dispellable: int
	delay: int
	triggers: str
	effectElement: int
	spellId: int
	effectTriggerDuration: int
	zoneDescr: SpellZoneDescr

	class UndefinedValues(OpenAPIIntEnum):
		UndefinedCategory = -2
		UndefinedShow = -1

