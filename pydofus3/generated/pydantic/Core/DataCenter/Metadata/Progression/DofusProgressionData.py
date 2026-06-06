from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Progression.DofusProgressionRequiredStepData import DofusProgressionRequiredStepData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Progression.DofusProgressionStepData import DofusProgressionStepData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class DofusProgressionData(D2oData):
	bundle_name: ClassVar[str] = "dofusprogressionsdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	gfxId: str
	backgroundColor: str
	minLevel: int
	maxLevel: int
	prerequisites: list[DofusProgressionRequiredStepData]
	steps: list[DofusProgressionStepData]
	order: int
	isPrimordial: bool
	isEvent: bool

