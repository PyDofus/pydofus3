from enum import IntFlag

# Core.UILogic.Mount.BreedingLine
class BreedingLine(IntFlag):
    Stable = 0
    Paddock = 1

# Core.UILogic.Mount.BreedingLine
class BreedingLine(IntFlag):
    NONE = -1
    Type = 0
    Sex = 1
    Name = 2
    Level = 3

# Core.UILogic.Mount.MountInfo
class MountInfo(IntFlag):
    Paddock = 0
    StandAlone = 1
    StandAloneCentered = 2

# Core.UILogic.Mount.MountPaddockUi
class MountPaddockUi(IntFlag):
    Tiles = 0
    List = 1
    Details = 2
    NONE = 3

# Core.UILogic.Mount.MountPaddockUi
class MountPaddockUi(IntFlag):
    MALE = 0
    FEMALE = 1

# Core.UILogic.Mount.MountPaddockUi
class MountPaddockUi(IntFlag):
    NONE = -1
    SourceEquip = 0
    SourceInventory = 1
    SourceBarn = 2
    SourcePaddock = 3

# Core.UILogic.Mount.MountPaddockUi
class MountPaddockUi(IntFlag):
    MountNegativeSerenity = 0
    MountAverageSerenity = 1
    MountPositiveSerenity = 2
    MountNeedStamina = 3
    MountFullStamina = 4
    MountNeedLove = 5
    MountFullLove = 6
    MountFruitful = 7
    MountNoFruitful = 8
    MountFertilized = 9
    MountSterilized = 10
    MountNoTired = 11
    MountLess50Tired = 12
    MountPartiallyTired = 13
    MountMore50Tired = 14
    Mount100Tired = 15
    MountNeedEnergy = 16
    MountFullEnergy = 17
    MountImmature = 18
    MountMountable = 19
    MountTrainable = 20
    MountNameless = 21
    MountOwner = 22
    MountBaby = 23

# Core.UILogic.Mount.PaddockSellBuyUi
class PaddockSellBuyUi(IntFlag):
    Buy = 0
    Sell = 1

