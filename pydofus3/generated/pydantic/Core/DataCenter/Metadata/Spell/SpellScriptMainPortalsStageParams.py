from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellScriptGfxSequenceParams import SpellScriptGfxSequenceParams
from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class SpellScriptMainPortalsStageParams(MyBaseModel):
	DefaultSequences: ClassVar[list[SpellScriptGfxSequenceParams]] = None
	sequences: list[SpellScriptGfxSequenceParams]

