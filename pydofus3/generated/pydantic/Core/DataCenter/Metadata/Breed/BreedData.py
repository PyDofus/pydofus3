from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Breed.BreedRoleByBreedData import BreedRoleByBreedData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.base import WrappedList
from pydofus3.not_generated.i18n import i18n

class BreedData(D2oData):
	bundle_name: ClassVar[str] = "breedsdataroot"

	id: int
	shortNameId: i18n
	descriptionId: i18n
	gameplayDescriptionId: i18n
	maleLook: str
	femaleLook: str
	creatureBonesId: int
	statsPointsForStrength: list[WrappedList[int]]
	statsPointsForIntelligence: list[WrappedList[int]]
	statsPointsForChance: list[WrappedList[int]]
	statsPointsForAgility: list[WrappedList[int]]
	statsPointsForVitality: list[WrappedList[int]]
	statsPointsForWisdom: list[WrappedList[int]]
	breedSpellsId: list[int]
	breedRoles: list[BreedRoleByBreedData]
	maleColors: list[int]
	femaleColors: list[int]
	complexity: int
	sortIndex: int

