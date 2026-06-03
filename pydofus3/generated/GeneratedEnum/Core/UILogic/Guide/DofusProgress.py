from enum import IntEnum

class DofusProgressUi:
	class SortType(IntEnum):
		Default = 0
		Level = 1
		Name = 2

	class FilterType(IntEnum):
		All = 0
		Event = 1
		Primordial = 2

class StepType(IntEnum):
	Achievement = 1
	Npc = 2
	Quest = 3
	Dofus = 4

