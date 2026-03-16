from enum import IntFlag

class CharacterPresetUi:
	class BuildComponent(IntFlag):
		None_ = 0
		Equipment = 2
		Spell = 4
		Stat = 8
		Name = 16
		Gfx = 32

