from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[gsw, int], Field(union_mode='left_to_right')]

	class gsw(OpenAPIIntEnum):
		dubw = 0
		dubx = 1
		duby = 2
		dubz = 3
		duca = 4

