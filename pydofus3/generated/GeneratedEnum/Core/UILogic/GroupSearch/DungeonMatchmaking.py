from enum import IntEnum

class DungeonMatchmaking:
	class SortingCriteria(IntEnum):
		None_ = -1
		Name = 0
		Anomaly = 1
		Level = 2
		Keys = 3

	class TimerType(IntEnum):
		None_ = 0
		Classic = 1
		Party = 2
		Random = 3

	class Section(IntEnum):
		Classic = 0
		Random = 1

	class DungeonAccessError(IntEnum):
		None_ = 0
		Level = 1
		HasAccess = 2
		Criterion = 3

