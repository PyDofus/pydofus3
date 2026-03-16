from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellZoneDescr import SpellZoneDescr
from pydofus3.not_generated.base import MyBaseModel

class PreviewSpellZoneDescr(MyBaseModel):
	id: int
	displayZoneDescr: SpellZoneDescr
	isPreviewZoneHidden: bool
	casterMask: str
	activationZoneDescr: SpellZoneDescr
	activationMask: str

