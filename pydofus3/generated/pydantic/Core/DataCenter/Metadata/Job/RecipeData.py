from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from pydofus3.not_generated.i18n import i18n

class RecipeData(D2oData):
	bundle_name: ClassVar[str] = "recipesdataroot"

	resultId: int
	resultNameId: i18n
	resultTypeId: int
	resultLevel: int
	ingredientIds: list[int]
	quantities: list[int]
	jobId: int
	skillId: int

