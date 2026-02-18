from enum import IntFlag

# Core.UILogic.CharacterBuild.CharacterPresetUi
class CharacterPresetUi(IntFlag):
    NONE = 0
    Equipment = 2
    Spell = 4
    Stat = 8
    Name = 16
    Gfx = 32

