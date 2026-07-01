from enum import IntEnum

class AnswerType(IntEnum):
	None_ = 0
	RepeatedQuest = 1
	Quest = 2
	QuestBack = 3
	QuestBackRepeated = 4
	QuestBackMain = 5
	QuestBackPrimordial = 6
	QuestBackInitiation = 7
	QuestBackEventMain = 8
	QuestBackEvent = 9
	QuestBackEventRepeatable = 10
	Fight = 11
	EventRepeatableQuest = 12
	EventQuest = 13
	EventMainQuest = 14
	MainQuest = 15
	PrimordialQuest = 16
	IntroductionQuest = 17

class AreaChartElement:
	class AxisLabelMode(IntEnum):
		Auto = 0
		Time = 1
		Date = 2

class BaseGridView:
	class ScrollBehaviorType(IntEnum):
		KeepCurrentScrollPosition = 0
		ScrollToBeginning = 1

class BaseProgressBar[TValue, TValueUxmlAttributeType]:
	class GaugeSizeEnum(IntEnum):
		large = 0
		small = 1

	class GaugeOrientationEnum(IntEnum):
		horizontal = 0
		vertical = 1

	class GaugeColorEnum(IntEnum):
		custom = 0
		primary = 1
		green = 2
		red = 3
		orange = 4
		grey = 5
		purple = 6
		pink = 7
		yellow = 8
		blue = 9

class DofusChatTextField:
	class TextCase(IntEnum):
		None_ = 0
		Title = 1
		Upper = 2

class DofusLabel:
	class TextCase(IntEnum):
		None_ = 0
		Title = 1
		Upper = 2

class MagneticDragWindow:
	class DragWindowOrientation(IntEnum):
		LeftToRight = 0
		RightToLeft = 1
		TopToBottom = 2
		BottomToTop = 3

class ResizableWindow:
	class DragPosition(IntEnum):
		None_ = 0
		Top = 1
		Bottom = 2
		Left = 3
		Right = 4
		Custom = 5

class ResizeHandler(IntEnum):
	BottomRight = 0
	BottomLeft = 1
	TopLeft = 2
	TopRight = 3
	Right = 4
	Left = 5
	Bottom = 6
	Top = 7

