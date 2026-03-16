from pydofus3.generated.pydantic.Core.DataCenter.Metadata.Quest.Objective.QuestObjectiveParametersData import QuestObjectiveParametersData
from pydofus3.not_generated.base import D2oData
from pydofus3.not_generated.base import MyBaseModel
from typing import ClassVar

class QuestObjectiveData(D2oData):
	bundle_name: ClassVar[str] = "questobjectivesdataroot"

	id: int
	stepId: int
	typeId: int
	dialogId: int
	parameters: QuestObjectiveParametersData
	coords: SerializableNullVector2
	mapId: int

	class SerializableNullVector2(MyBaseModel):
		x: int
		y: int

