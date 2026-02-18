from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Monster.MonsterBonusCharacteristicsData import MonsterBonusCharacteristicsData
from pydofus3.not_generated.base import MyBaseModel


class MonsterGradeData(MyBaseModel):
	bonusCharacteristics: MonsterBonusCharacteristicsData
	grade: int
	monsterId: int
	level: int
	lifePoints: int
	actionPoints: int
	movementPoints: int
	vitality: int
	paDodge: int
	pmDodge: int
	wisdom: int
	earthResistance: int
	airResistance: int
	fireResistance: int
	waterResistance: int
	neutralResistance: int
	gradeXp: int
	damageReflect: int
	strength: int
	intelligence: int
	chance: int
	agility: int
	startingSpellId: int
	bonusRange: int

