from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[hbi, int], Field(union_mode='left_to_right')]

	class hbi(OpenAPIIntEnum):
		eaxn = 0
		eaxo = 1
		eaxp = 2
		eaxq = 3
		eaxr = 4

