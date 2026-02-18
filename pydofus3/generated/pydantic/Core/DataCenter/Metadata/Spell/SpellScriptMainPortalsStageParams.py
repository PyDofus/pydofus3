from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Spell.SpellScriptGfxSequenceParams import SpellScriptGfxSequenceParams
from pydofus3.not_generated.base import MyBaseModel


class SpellScriptMainPortalsStageParams(MyBaseModel):
	sequences: list[SpellScriptGfxSequenceParams]

