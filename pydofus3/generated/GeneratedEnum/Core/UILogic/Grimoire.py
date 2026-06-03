from enum import IntEnum

class AchievementsUI:
	class AchievementView(IntEnum):
		Achievement = 0
		Global = 1

class EncyclopediaBaseUi:
	class TitleTabs(IntEnum):
		Guide = 0
		Bestiary = 1
		Equipment = 2
		Consumables = 3
		Resources = 4
		Skin = 5

class ProgressRewardCategory(IntEnum):
	Top = 0
	Big = 1
	Small = 2

