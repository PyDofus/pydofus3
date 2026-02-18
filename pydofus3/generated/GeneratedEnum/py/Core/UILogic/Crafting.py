from enum import IntFlag

# Core.UILogic.Crafting.CrafterList
class CrafterList(IntFlag):
    Status = 0
    PlayerName = 1
    JobLevel = 2
    WorldPos = 3
    MinLevelCraft = 4
    FreeCraft = 5
    CanCraftLegendary = 6

# Core.UILogic.Crafting.RuneMakerUi
class RuneMakerUi(IntFlag):
    IsCrushing = 0
    CrushResult = 1

