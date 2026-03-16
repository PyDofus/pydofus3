from enum import IntFlag

class CharacterInformation:
	class CharacterInfosWidgetOptions(IntFlag):
		LargeModule = 1
		SmallModule = 2
		SizeGroup = 3
		Hp1Line = 4
		Hp2Lines = 8
		HpPercent = 16
		HpGroup = 28
		ShowPI = 32
		HidePI = 64
		Default = 69
		ShowPIGroup = 96

