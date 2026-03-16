from pydantic import Field
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.ParallelExecutionEndPolicy import ParallelExecutionEndPolicy
from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellScriptGfxUsageParams import SpellScriptGfxUsageParams
from pydofus3.not_generated.base import MyBaseModel
from typing import Annotated, Union
from typing import ClassVar

class SpellScriptGfxSequenceParams(MyBaseModel):
	DefaultEndPolicy: ClassVar[Annotated[Union[ParallelExecutionEndPolicy, int], Field(union_mode='left_to_right')]] = Annotated[Union[ParallelExecutionEndPolicy, int], Field(union_mode='left_to_right')].WaitForAll
	DefaultGfxs: ClassVar[list[SpellScriptGfxUsageParams]] = None
	endPolicy: Annotated[Union[ParallelExecutionEndPolicy, int], Field(union_mode='left_to_right')]
	gfxs: list[SpellScriptGfxUsageParams]

