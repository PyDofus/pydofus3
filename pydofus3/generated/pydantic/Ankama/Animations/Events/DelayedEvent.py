from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[hbg, int], Field(union_mode='left_to_right')]

	class hbg(OpenAPIIntEnum):
		ebgr = 0
		ebgs = 1
		ebgt = 2
		ebgu = 3
		ebgv = 4

