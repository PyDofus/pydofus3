from enum import IntEnum

class LoadPhase(IntEnum):
	FromStartToLauncher = 0
	FromLauncherToCharacterSelection = 1
	FromCharacterSelectionToGame = 2

