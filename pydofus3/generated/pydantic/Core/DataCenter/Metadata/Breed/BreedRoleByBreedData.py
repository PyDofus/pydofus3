from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.i18n import i18n

class BreedRoleByBreedData(MyBaseModel):
	roleId: int
	descriptionId: i18n
	value: int
	order: int

