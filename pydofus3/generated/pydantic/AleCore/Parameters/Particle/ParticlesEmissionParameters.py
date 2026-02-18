from pydofus3.generated.pydantic.AleCore.Data.AleBurst import AleBurst
from pydofus3.generated.pydantic.AleCore.Data.AleMinMaxCurve import AleMinMaxCurve
from pydofus3.not_generated.base import MyBaseModel


class ParticlesEmissionParameters(MyBaseModel):
	rateOverTime: AleMinMaxCurve
	bursts: list[AleBurst]
	class Notify(MyBaseModel):
		pass

