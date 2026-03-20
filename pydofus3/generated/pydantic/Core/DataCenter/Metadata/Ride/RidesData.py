from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Ride.BreedingRelationData import BreedingRelationData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Ride.ParentsRelationData import ParentsRelationData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.i18n import i18n
from typing import ClassVar

class RidesData(D2oData):
	bundle_name: ClassVar[str] = "ridesdataroot"

	id: int
	nameId: i18n
	colorId: i18n
	speciesId: int
	generation: int
	geneticWeight: int
	linkedItemGid: int
	extractionRewardQuantity: int
	senileExtractionRewardQuantity: int
	breedingTokenRewardQuantity: int
	breedingExperienceRewardQuantity: int
	parents: list[ParentsRelationData]
	children: list[BreedingRelationData]

