from enum import IntFlag

# Core.DataCenter.LoadPhase
class LoadPhase(IntFlag):
    FromStartToLauncher = 0
    FromLauncherToCharacterSelection = 1
    FromCharacterSelectionToGame = 2

