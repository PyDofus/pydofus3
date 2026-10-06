from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[hbv, int], Field(union_mode='left_to_right')]

	class hbv(OpenAPIIntEnum):
		ebij = 0
		ebik = 1
		ebil = 2
		ebim = 3
		ebin = 4

