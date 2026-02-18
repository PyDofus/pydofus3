from pydofus3.generated.pydantic.AleCore.Data.AleConstantOrCurve import AleConstantOrCurve
from pydofus3.generated.pydantic.Editor.AleCore.Data.Staging.IStagingEffect import IStagingEffect

class PlayFmodEventStagingEffect(IStagingEffect):
	UpdatePosition: System.Action[AleCore.Data.AleVector2]
	fmodEvent: str
	xPosition: AleConstantOrCurve
	yPosition: AleConstantOrCurve

