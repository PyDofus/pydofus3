from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.Instance.EffectInstanceDice import EffectInstanceDice
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class MountData(D2oData):
	bundle_name: ClassVar[str] = "mountsdataroot"

	id: int
	familyId: int
	nameId: i18n
	look: str
	certificateId: int
	effects: list[EffectInstanceDice]

