from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class GuildMissionObjectiveData(D2oData):
	bundle_name: ClassVar[str] = "guildmissionobjectivesdataroot"

	id: int
	superCategoryId: int
	missionId: int
	order: int
	activationCriterion: str
	alterationId: int
	areaId: int
	subareaId: int
	mapId: int
	descriptionId: i18n
	monsterId: int
	inDungeon: bool
	quantity: int
	familyId: int
	familyMonsters: list[int]
	minLevel: int
	intensity: int
	stage: int
	seedId: int
	objectId: int
	quests: list[int]

