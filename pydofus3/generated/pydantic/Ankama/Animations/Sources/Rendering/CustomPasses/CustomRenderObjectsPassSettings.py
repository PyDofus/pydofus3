from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.ShaderConstants import ShaderConstants
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.unity import SortingCriteria
from typing import Annotated, Union

class CustomRenderObjectsPassSettings(MyBaseModel):
	shaderPassIndex: int
	sortingCriteria: SortingCriteria
	renderingLayerMask: Annotated[Union[ShaderConstants.RenderingLayerIDs, int], Field(union_mode='left_to_right')]
	shaderTagIds: list[str]

