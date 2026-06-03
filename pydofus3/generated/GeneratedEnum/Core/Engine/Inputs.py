from enum import IntEnum
from enum import IntFlag

class ActionsMapsManager:
	class ActionsMapsIndex(IntEnum):
		Common = 0
		Menu = 1
		Tooltip = 2
		Chat = 3
		Option = 4
		Fight = 5
		QuickSlot = 6
		Misc = 7
		TutorialStep11 = 8
		TutorialStep12 = 9
		TutorialStep15A = 10
		TutorialStep15B = 11

	class ActionsMapsFlags(IntFlag):
		Common = 1
		Menu = 2
		Tooltip = 4
		Chat = 8
		Option = 16
		Fight = 32
		QuickSlot = 64
		Misc = 128
		TutorialStep11 = 256
		TutorialStep12 = 512
		tutorialStep15A = 1024
		tutorialStep15B = 2048

