from enum import IntEnum

class BaseZaapSelectionUI:
	class SortCriteria(IntEnum):
		Spawn = 0
		AreaName = 1
		SubAreaName = 2
		Coordinates = 3
		Level = 4

	class TabIdentifier(IntEnum):
		Tab1 = 0
		Tab2 = 1
		Tab3 = 2

