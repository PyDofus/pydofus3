from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Npc.NestedAnimFunNpcData import NestedAnimFunNpcData
from pydofus3.generated.pydantic.Core.DataCenter.Types.AnimFunData import AnimFunData

class AnimFunNpcData(AnimFunData):
	subAnimFunData: list[NestedAnimFunNpcData]

