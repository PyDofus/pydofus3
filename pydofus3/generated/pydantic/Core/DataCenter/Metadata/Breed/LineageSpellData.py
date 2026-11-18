from pydofus3.not_generated.base import MyBaseModel

class LineageSpellData(MyBaseModel):
	id: int
	lineageId: int
	lineageLevel: int
	spellLevelId: int
	keptForHigherLevels: bool
	isStartingSpell: bool

