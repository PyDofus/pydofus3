from enum import IntFlag

# Core.UILogic.Quest.QuestList
class QuestList(IntFlag):
    Default = 1196
    FollowFew = 1
    FollowNormal = 2
    FollowLot = 4
    AutoFollow = 8
    FontSmall = 16
    FontMedium = 32
    FontLarge = 64
    FontXLarge = 2048
    AutoResize = 128
    OpacityLow = 256
    OpacityMedium = 512
    OpacityHigh = 1024

# Core.UILogic.Quest.QuestsUI
class QuestsUI(IntFlag):
    InProgress = 0
    Done = 1
    Hidden = 2

