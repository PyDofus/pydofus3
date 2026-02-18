from enum import IntFlag

# Core.UILogic.InfiniteDream.InfiniteDreamBestiary
class InfiniteDreamBestiary(IntFlag):
    none = 0
    name = 1
    rank = 2
    initiative = 3

# Core.UILogic.InfiniteDream.InfiniteDreamBestiary
class InfiniteDreamBestiary(IntFlag):
    NONE = 0
    Mov = 1
    NoLos = 2
    Red = 3
    Blue = 4

# Core.UILogic.InfiniteDream.InfiniteDreamDropTable
class InfiniteDreamDropTable(IntFlag):
    NONE = 0
    Percent = 1
    Name = 2

# Core.UILogic.InfiniteDream.InfiniteDreamMapInfo
class InfiniteDreamMapInfo(IntFlag):
    NotAvailable = 0
    Current = 1
    Completed = 2
    Available = 3

# Core.UILogic.InfiniteDream.InfiniteDreamTrackingUi
class InfiniteDreamTrackingUi(IntFlag):
    Default = 24
    OpacityLow = 2
    OpacityMedium = 4
    OpacityHigh = 8
    OwnerVisible = 16
    OwnerNotVisible = 32

