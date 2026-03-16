from pydofus3.generated.pydantic.Core.DataCenter.Metadata.World.MapInformationFlags import MapInformationFlags
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class MapInformationData(D2oData):
	bundle_name: ClassVar[str] = "mapsinformationdataroot"

	m_flags: MapInformationFlags
	id: int
	posX: int
	posY: int
	nameId: i18n
	subAreaId: int
	worldMap: int
	tacticalModeTemplateId: int

