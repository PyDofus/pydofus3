from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[hcl, int], Field(union_mode='left_to_right')]

	class hcl(OpenAPIIntEnum):
		ebbd = 0
		ebbe = 1
		ebbf = 2
		ebbg = 3
		ebbh = 4

