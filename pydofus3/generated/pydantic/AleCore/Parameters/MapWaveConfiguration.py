from pydofus3.generated.pydantic.AleCore.Parameters.WaveParameters import WaveParameters
from pydofus3.not_generated.base import MyBaseModel

class MapWaveConfiguration(MyBaseModel):
	waveParameters: WaveParameters

