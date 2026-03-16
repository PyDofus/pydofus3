from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Progression.FeatureImage import FeatureImage
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class FeatureDescriptionData(D2oData):
	bundle_name: ClassVar[str] = "featuredescriptionsdataroot"

	id: int
	nameId: i18n
	descriptionId: i18n
	priority: int
	parentId: int
	children: list[int]
	criterion: str
	images: list[FeatureImage]

