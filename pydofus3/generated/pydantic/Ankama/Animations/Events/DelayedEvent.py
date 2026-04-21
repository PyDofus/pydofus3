from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[gst, int], Field(union_mode='left_to_right')]

	class gst(OpenAPIIntEnum):
		dtxb = 0
		dtxc = 1
		dtxd = 2
		dtxe = 3
		dtxf = 4

