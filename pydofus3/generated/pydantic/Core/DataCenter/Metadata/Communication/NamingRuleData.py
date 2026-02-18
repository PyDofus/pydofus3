from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel


class NamingRuleData(D2oData):
	bundle_name: ClassVar[str] = "namingrulesdataroot"

	id: int
	minLength: int
	maxLength: int
	regexp: str

