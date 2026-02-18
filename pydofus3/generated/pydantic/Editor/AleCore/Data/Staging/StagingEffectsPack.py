from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.IStagingEffect import IStagingEffect
from pydofus3.not_generated.base import MyBaseModel


class StagingEffectsPack(MyBaseModel):
	targets: list[str]
	stagingEffects: list[IStagingEffect]

