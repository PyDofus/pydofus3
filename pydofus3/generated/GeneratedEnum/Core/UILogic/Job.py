from enum import IntEnum

class JobCraftAndSkillsHandler:
	class JobCraftUITabsEnum(IntEnum):
		Recipes = 0
		Skills = 1

class JobProgressUIHandler:
	class JobProgressSortEnum(IntEnum):
		Name = 0
		Level = 1

class JobSkillsUI:
	class SortType(IntEnum):
		Name = 0
		Level = 1
		Resources = 2
		Experience = 3

