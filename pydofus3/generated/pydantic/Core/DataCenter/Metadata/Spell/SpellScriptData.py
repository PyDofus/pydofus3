from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Enums.SpellScriptType import SpellScriptType
from pydofus3.not_generated.base import D2oData
from typing import ClassVar

from pydofus3.not_generated.base import MyBaseModel

from typing import Union, Annotated

class SpellScriptData(D2oData):
	bundle_name: ClassVar[str] = "spellscriptsdataroot"

	rawParams: str
	type: Annotated[Union[SpellScriptType, int], Field(union_mode='left_to_right')]

