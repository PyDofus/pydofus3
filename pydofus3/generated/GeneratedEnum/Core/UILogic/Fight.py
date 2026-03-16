from enum import IntEnum

class BuffsFightUI:
	class BuffUiEnumTabs(IntEnum):
		Spells = 0
		Summary = 1

class FightResultResumeTab:
	class SectionEnum(IntEnum):
		Winner = 0
		Loser = 1

	class SortType(IntEnum):
		Name = 0
		Level = 1
		Experience = 2
		Kamas = 3

class FightResultTabsEnum(IntEnum):
	FightResultCharacterTab = 0
	FightResultResumeTab = 1
	FightResultStatsTab = 2

class SpellPickerUI:
	class RewardType(IntEnum):
		Spell = 0
		Kamas = 1
		Alteration = 2
		Experience = 3
		Object = 4
		TriggerSpell = 5
		Teleport = 6

