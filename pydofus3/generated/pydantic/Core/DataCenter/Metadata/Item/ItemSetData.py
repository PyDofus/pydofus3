from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Effect.Instance.EffectInstanceDice import EffectInstanceDice
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import WrappedList
from pydofus3.not_generated.i18n import i18n

class ItemSetData(D2oData):
	bundle_name: ClassVar[str] = "itemsetsdataroot"

	id: int
	items: list[int]
	nameId: i18n
	bonusIsSecret: bool
	isCosmetic: bool
	effects: list[WrappedList[EffectInstanceDice]]

