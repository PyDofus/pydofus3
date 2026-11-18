from enum import IntEnum
from enum import IntFlag

class ElementDragger:
	class AxisLock(IntEnum):
		None_ = 0
		Horizontal = 1
		Vertical = 2

class KeyUsages(IntFlag):
	None_ = 0
	Left = 0
	Right = 0
	Up = 0
	Down = 0
	Submit = 0
	Cancel = 0
	NavigationOnly = 0
	All = 0

