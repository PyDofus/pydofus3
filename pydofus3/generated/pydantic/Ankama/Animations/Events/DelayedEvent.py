from pydantic import Field
from pydofus3.not_generated.base import MyBaseModel
from pydofus3.not_generated.base import OpenAPIIntEnum
from typing import Annotated, Union

class DelayedEvent(MyBaseModel):
	type: Annotated[Union[hbz, int], Field(union_mode='left_to_right')]

	class hbz(OpenAPIIntEnum):
		eaqq = 0
		eaqr = 1
		eaqs = 2
		eaqt = 3
		eaqu = 4

