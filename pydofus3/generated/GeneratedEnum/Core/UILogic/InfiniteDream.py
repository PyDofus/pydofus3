from enum import IntEnum
from enum import IntFlag

class InfiniteDreamBestiary:
	class SortType(IntEnum):
		none = 0
		name = 1
		rank = 2
		initiative = 3

	class CellType(IntEnum):
		None_ = 0
		Mov = 1
		NoLos = 2
		Red = 3
		Blue = 4

class InfiniteDreamDropTable:
	class SortType(IntEnum):
		None_ = 0
		Percent = 1
		Name = 2

class InfiniteDreamMapInfo:
	class AvailableRoomType(IntEnum):
		NotAvailable = 0
		Current = 1
		Completed = 2
		Available = 3

class InfiniteDreamTrackingUi:
	class InfiniteDreamWidgetSettings(IntFlag):
		OpacityLow = 2
		OpacityMedium = 4
		OpacityHigh = 8
		OwnerVisible = 16
		Default = 24
		OwnerNotVisible = 32

