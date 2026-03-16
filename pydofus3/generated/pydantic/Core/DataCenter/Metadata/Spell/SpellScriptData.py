from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Enums.SpellScriptType import SpellScriptType
from pydofus3.not_generated.base import D2oData
from typing import Annotated, Union
from typing import ClassVar

class SpellScriptData(D2oData):
	bundle_name: ClassVar[str] = "spellscriptsdataroot"

	rawParams: str
	type: Annotated[Union[SpellScriptType, int], Field(union_mode='left_to_right')]

