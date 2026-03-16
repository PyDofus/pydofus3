from enum import IntEnum

class CrafterList:
	class SortType(IntEnum):
		Status = 0
		PlayerName = 1
		JobLevel = 2
		WorldPos = 3
		MinLevelCraft = 4
		FreeCraft = 5
		CanCraftLegendary = 6

class RuneMakerUi:
	class CrushState(IntEnum):
		IsCrushing = 0
		CrushResult = 1

