from enum import IntFlag

# Core.UILogic.Job.JobCraftAndSkillsHandler
class JobCraftAndSkillsHandler(IntFlag):
    Recipes = 0
    Skills = 1

# Core.UILogic.Job.JobProgressUIHandler
class JobProgressUIHandler(IntFlag):
    Name = 0
    Level = 1

# Core.UILogic.Job.JobSkillsUI
class JobSkillsUI(IntFlag):
    Name = 0
    Level = 1
    Resources = 2
    Experience = 3

