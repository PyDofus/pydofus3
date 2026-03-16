from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Ride.BreedingRelationData import BreedingRelationData
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Ride.ParentsRelationData import ParentsRelationData
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

class RidesData(D2oData):
	bundle_name: ClassVar[str] = "ridesdataroot"

	id: int
	nameId: int
	colorId: int
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

