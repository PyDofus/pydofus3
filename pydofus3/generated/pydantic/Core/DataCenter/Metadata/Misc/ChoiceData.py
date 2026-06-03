from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Misc.ChoiceOptionData import ChoiceOptionData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class ChoiceData(D2oData):
	bundle_name: ClassVar[str] = "choicesdataroot"

	id: int
	choiceNameId: i18n
	parentId: int
	duration: int
	options: list[ChoiceOptionData]

