from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Monster.MonsterDropCoefficientData import MonsterDropCoefficientData
from pydofus3.not_generated.base import float_nan
from pydofus3.not_generated.base import MyBaseModel

class MonsterDropData(MyBaseModel):
	dropId: int
	monsterId: int
	objectId: int
	percentDropForGrade1: float_nan
	percentDropForGrade2: float_nan
	percentDropForGrade3: float_nan
	percentDropForGrade4: float_nan
	percentDropForGrade5: float_nan
	count: int
	criterions: str
	hasCriterions: bool
	hiddenIfInvalidCriterions: bool
	specificDropCoefficient: list[MonsterDropCoefficientData]
	disableDropModificator: bool

