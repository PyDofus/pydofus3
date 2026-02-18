from enum import IntFlag

# Core.UILogic.Fight.BuffsFightUI
class BuffsFightUI(IntFlag):
    Spells = 0
    Summary = 1

# Core.UILogic.Fight.FightResultResumeTab
class FightResultResumeTab(IntFlag):
    Winner = 0
    Loser = 1

# Core.UILogic.Fight.FightResultResumeTab
class FightResultResumeTab(IntFlag):
    Name = 0
    Level = 1
    Experience = 2
    Kamas = 3

# Core.UILogic.Fight.FightResultTabsEnum
class FightResultTabsEnum(IntFlag):
    FightResultCharacterTab = 0
    FightResultResumeTab = 1
    FightResultStatsTab = 2

# Core.UILogic.Fight.SpellPickerUI
class SpellPickerUI(IntFlag):
    Spell = 0
    Kamas = 1
    Alteration = 2
    Experience = 3
    Object = 4
    TriggerSpell = 5
    Teleport = 6

