from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[gsp, int], Field(union_mode='left_to_right')]

	class gsp(OpenAPIIntEnum):
		dtnk = 0
		dtnl = 1
		dtnm = 2
		dtnn = 3
		dtno = 4

