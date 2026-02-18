from enum import IntFlag

# Core.UILogic.Party.KisPopupWarningUi
class KisPopupWarningUi(IntFlag):
    Inactivity = 0
    Prevent = 1
    Sanction = 2
    MissingEquipment = 3

# Core.UILogic.Party.PartyDisplayUi
class PartyDisplayUi(IntFlag):
    Default = 262
    Horizontal = 1
    Vertical = 2
    OneLine = 4
    TwoLines = 8
    RestrictFightToParty = 16
    PartyLocked = 32
    ArenaPartyLocked = 64
    Small = 128
    Big = 256

# Core.UILogic.Party.PvpArenaBaseUi
class PvpArenaBaseUi(IntFlag):
    Default = -1
    Fights = 0
    Rewards = 1
    Ladder = 2

