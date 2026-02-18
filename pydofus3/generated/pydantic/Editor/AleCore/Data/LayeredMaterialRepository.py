from pydofus3.generated.pydantic.Editor.AleCore.Data.MaterialRepository import MaterialRepository
from pydofus3.not_generated.base import MyBaseModel


class LayeredMaterialRepository(MyBaseModel):
	background: MaterialRepository
	sortable: MaterialRepository
	foreground: MaterialRepository

