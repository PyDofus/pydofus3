from enum import IntEnum

class AllianceAvaUi:
	class SortingCriteriaAva(IntEnum):
		None_ = -1
		Name = 0
		Character = 1
		Domination = 2
		Fight = 3
		Map = 4
		Scout = 5
		TotalScore = 6
		AVA = 7

	class AvaView(IntEnum):
		Big = 0
		Small = 1

	class ScoreType(IntEnum):
		Map = 0
		Fight = 1
		Prism = 2

class AllianceConquestsUi:
	class AllianceConquestSortEnum(IntEnum):
		None_ = 0
		SortByType = 1
		SortBySubarea = 2
		SortByState = 3
		SortByOwner = 4
		SortByCreationDate = 5
		SortByPods = 6

	class ComboboxFilterType(IntEnum):
		All = 0
		Prisms = 1
		TaxCollectors = 2
		Village = 3

