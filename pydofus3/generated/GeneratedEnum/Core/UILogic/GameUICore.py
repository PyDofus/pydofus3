from enum import IntEnum
from enum import IntFlag

class RewardsMenuUi:
	class RewardType(IntEnum):
		AchievementReward = 0
		Gift = 1

class SmileyUIEmoteTab:
	class SortType(IntEnum):
		None_ = 0
		AlphaAsc = 1
		AlphaDsc = 2

class SmileyUITabsEnum(IntEnum):
	SmileyUIEmoteTab = 0
	SmileyUISmileyTab = 1

class UIActionBar:
	class ActionBarWidgetOption(IntFlag):
		Horizontal = 1
		Vertical = 2
		ContextFollow = 4
		TabItems = 64
		Default = 69
		TabSpells = 128

