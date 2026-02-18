from enum import IntFlag

# Core.UILogic.GameUICore.RewardsMenuUi
class RewardsMenuUi(IntFlag):
    AchievementReward = 0
    Gift = 1

# Core.UILogic.GameUICore.SmileyUIEmoteTab
class SmileyUIEmoteTab(IntFlag):
    NONE = 0
    AlphaAsc = 1
    AlphaDsc = 2

# Core.UILogic.GameUICore.SmileyUITabsEnum
class SmileyUITabsEnum(IntFlag):
    SmileyUIEmoteTab = 0
    SmileyUISmileyTab = 1

# Core.UILogic.GameUICore.UIActionBar
class UIActionBar(IntFlag):
    Default = 69
    Horizontal = 1
    Vertical = 2
    ContextFollow = 4
    TabItems = 64
    TabSpells = 128

