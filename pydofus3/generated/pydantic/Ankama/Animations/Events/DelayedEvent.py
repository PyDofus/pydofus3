from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[hel, int], Field(union_mode='left_to_right')]

	class hel(OpenAPIIntEnum):
		ecqy = 0
		ecqz = 1
		ecra = 2
		ecrb = 3
		ecrc = 4

