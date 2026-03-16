from enum import IntEnum
from enum import IntFlag

class BreedingTab(IntEnum):
	None_ = -1
	Paddock = 0
	Mating = 1
	Cloning = 2
	Extraction = 3

class BreedingUi:
	class FilterEnum(IntEnum):
		MountNegativeMood = 0
		MountAverageMood = 1
		MountPositiveMood = 2
		MountNeedMaturity = 3
		MountFullMaturity = 4
		MountNeedStamina = 5
		MountFullStamina = 6
		MountNeedLove = 7
		MountFullLove = 8
		MountFertile = 9
		MountFeconde = 10
		MountSterile = 11
		MountSenile = 12
		MountNameless = 13

class CloningUi:
	class CloningDragAndDropErrorFlags(IntFlag):
		None_ = 0
		DiffGeneration = 2
		DiffFamily = 4
		Senile = 16
		SameRide = 32

	class CloningStateEnum(IntEnum):
		Reset = 0
		Preview = 1
		Result = 2

class MatingUi:
	class MatingDragAndDropErrorFlags(IntFlag):
		None_ = 0
		CannotReproduce = 2
		DiffFamily = 4
		SameGender = 8
		Senile = 16
		SameRide = 32
		LoveGaugeLow = 64
		MaturityGaugeLow = 128
		StaminaGaugeLow = 256

	class MatingStateEnum(IntEnum):
		Reset = 0
		Preview = 1
		Done = 2
		Error = 3

class OpenPaddockState(IntEnum):
	None_ = -1
	FullAccess = 0
	GaugeOnly = 1

class PaddockGauge(IntEnum):
	None_ = -1
	Slapper = 1
	Patter = 2
	Blaster = 3
	DrinkingTrough = 4
	DragoButt = 5
	Feeder = 6

class RideSource(IntEnum):
	SourceInventory = 0
	SourceStable = 1
	SourcePaddock = 2

