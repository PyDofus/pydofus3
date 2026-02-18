from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Appearance.SlotRuleData import SlotRuleData
from pydofus3.generated.pydantic.Metadata.Enums.SkinSlotRuleType import SkinSlotRuleType
from pydofus3.not_generated.base import MyBaseModel

from typing import Union, Annotated

class SkinSlotsRulesInfoData(MyBaseModel):
	slotRuleType: Annotated[Union[SkinSlotRuleType, int], Field(union_mode='left_to_right')]
	slotRuleInfo: int
	slotsRules: list[SlotRuleData]

