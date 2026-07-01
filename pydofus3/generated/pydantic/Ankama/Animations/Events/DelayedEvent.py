from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[hby, int], Field(union_mode='left_to_right')]

	class hby(OpenAPIIntEnum):
		eazd = 0
		eaze = 1
		eazf = 2
		eazg = 3
		eazh = 4

