from enum import IntFlag

# Core.UILogic.Grimoire.AchievementsUI
class AchievementsUI(IntFlag):
    Achievement = 0
    Global = 1

# Core.UILogic.Grimoire.EncyclopediaBaseUi
class EncyclopediaBaseUi(IntFlag):
    Bestiary = 0
    Equipment = 1
    Consumables = 2
    Resources = 3
    Skin = 4

# Core.UILogic.Grimoire.ProgressRewardCategory
class ProgressRewardCategory(IntFlag):
    Top = 0
    Big = 1
    Small = 2

