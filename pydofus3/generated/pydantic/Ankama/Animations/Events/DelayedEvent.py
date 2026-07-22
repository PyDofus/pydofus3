from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[hch, int], Field(union_mode='left_to_right')]

	class hch(OpenAPIIntEnum):
		ebim = 0
		ebin = 1
		ebio = 2
		ebip = 3
		ebiq = 4

