from pydantic import Field
from pydofus3.generated.pydantic.Ankama.Animations.Rendering.FlashMaskState import FlashMaskState
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union

class SkinChunk(MyBaseModel):
	startVertexIndex: int
	indexCount: int
	startIndexIndex: int
	vertexCount: int
	textureIndex: int
	maskState: Annotated[Union[FlashMaskState, int], Field(union_mode='left_to_right')]

