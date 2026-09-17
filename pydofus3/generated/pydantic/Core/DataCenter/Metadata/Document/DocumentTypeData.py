from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class DocumentTypeData(D2oData):
	bundle_name: ClassVar[str] = "documenttypesdataroot"

	id: int
	behaviorTypeId: int
	icon: str
	clientProperties: str

