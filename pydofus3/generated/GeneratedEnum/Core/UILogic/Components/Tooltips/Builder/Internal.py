from enum import IntEnum
from enum import IntFlag

class TooltipBuilderFlags(IntFlag):
	None_ = 0
	BringToFront = 1
	AutoHide = 2
	KeepOnZoom = 4
	ScreenCollision = 8
	InsertLayer = 16
	IgnoreHideAll = 32
	All = 4294967295

class TooltipPositioning:
	class Location(IntEnum):
		TopLeft = 0
		TopCenter = 1
		TopRight = 2
		CenterLeft = 3
		Center = 4
		CenterRight = 5
		BottomLeft = 6
		BottomCenter = 7
		BottomRight = 8

