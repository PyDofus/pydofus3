from enum import IntEnum

class AchievementsUI:
	class AchievementView(IntEnum):
		Achievement = 0
		Global = 1

class EncyclopediaBaseUi:
	class TitleTabs(IntEnum):
		Bestiary = 0
		Equipment = 1
		Consumables = 2
		Resources = 3
		Skin = 4

class ProgressRewardCategory(IntEnum):
	Top = 0
	Big = 1
	Small = 2

