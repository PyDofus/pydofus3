from enum import IntFlag

# Core.UILogic.Roleplay.FightMapPreviewUi
class FightMapPreviewUi(IntFlag):
    NONE = 0
    Mov = 1
    NoLos = 2
    Red = 3
    Blue = 4

# Core.UILogic.Roleplay.SpectatorUi
class SpectatorUi(IntFlag):
    NB_PLAYER = 0
    AVERAGE_LEVEL = 1
    DURATION = 2

# Core.UILogic.Roleplay.SpectatorUi
class SpectatorUi(IntFlag):
    NAME = 0
    LEVEL = 1

# Core.UILogic.Roleplay.SpectatorUi
class SpectatorUi(IntFlag):
    One = 2
    Two = 4
    Three = 6

# Core.UILogic.Roleplay.TreasureHunt
class TreasureHunt(IntFlag):
    Default = 34
    FontSmall = 1
    FontMedium = 2
    FontLarge = 4
    OpacityNone = 8
    OpacityLow = 16
    OpacityMedium = 32
    OpacityHigh = 64

