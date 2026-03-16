from pydofus3.generated.pydantic.Metadata.Appearance.SkinSlotsRulesInfoData import SkinSlotsRulesInfoData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class SkinSlotRuleData(D2oData):
	bundle_name: ClassVar[str] = "skinslotsrulesdataroot"

	skinId: int
	slotRulesList: list[SkinSlotsRulesInfoData]

