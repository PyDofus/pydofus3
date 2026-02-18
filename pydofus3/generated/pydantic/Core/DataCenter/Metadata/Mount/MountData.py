from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.Instance.EffectInstanceDice import EffectInstanceDice
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class MountData(D2oData):
	bundle_name: ClassVar[str] = "mountsdataroot"

	id: int
	familyId: int
	nameId: i18n
	look: str
	certificateId: int
	effects: list[EffectInstanceDice]

