from enum import IntFlag

# Core.UILogic.MainMenu.CharacterInformation
class CharacterInformation(IntFlag):
    LargeModule = 1
    SmallModule = 2
    Hp1Line = 4
    Hp2Lines = 8
    HpPercent = 16
    ShowPI = 32
    HidePI = 64
    Default = 69
    ShowPIGroup = 96
    HpGroup = 28
    SizeGroup = 3

