from pydofus3.generated.pydantic.Ankama.Animations.Rendering.IApplyMaterialSortOrder import IApplyMaterialSortOrder
from pydofus3.not_generated.base import MyBaseModel

class BackgroundObject(MyBaseModel):
	id: int
	applyMaterialSortOrder: IApplyMaterialSortOrder
	requiresAutoPosition: bool

