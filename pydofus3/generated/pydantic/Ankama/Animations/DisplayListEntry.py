from pydofus3.generated.pydantic.Ankama.Animations.Rendering.AnimTransform import AnimTransform
from pydofus3.not_generated.base import MyBaseModel

class DisplayListEntry(MyBaseModel):
	symbolId: int
	entries: int
	transform: AnimTransform

