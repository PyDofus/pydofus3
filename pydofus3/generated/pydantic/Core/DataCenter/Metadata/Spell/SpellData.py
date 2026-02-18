from pydofus3.generated.pydantic.Core.DataCenter.Interfaces.IAdminSelectionEntry import IAdminSelectionEntry
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.BoundScriptUsageData import BoundScriptUsageData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellFlags import SpellFlags
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellZoneDescr import SpellZoneDescr
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.i18n import i18n

class SpellData(IAdminSelectionEntry, D2oData):
	bundle_name: ClassVar[str] = "spellsdataroot"

	m_flags: SpellFlags
	id: int
	nameId: i18n
	descriptionId: i18n
	typeId: int
	order: int
	scriptParams: str
	scriptParamsCritical: str
	scriptId: int
	scriptIdCritical: int
	iconId: int
	spellLevels: list[int]
	boundScriptUsageData: list[BoundScriptUsageData]
	criticalHitBoundScriptUsageData: list[BoundScriptUsageData]
	basePreviewZoneDescr: SpellZoneDescr
	adminName: str

