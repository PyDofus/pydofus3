from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.Instance.EffectInstanceDice import EffectInstanceDice
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class AlterationData(D2oData):
	bundle_name: ClassVar[str] = "alterationsdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	categoryId: int
	iconId: int
	isVisible: bool
	criterions: str
	isWebDisplay: bool
	possibleEffects: list[EffectInstanceDice]

