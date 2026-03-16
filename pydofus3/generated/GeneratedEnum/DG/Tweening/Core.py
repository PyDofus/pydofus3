from enum import IntEnum

class DOTweenSettings:
	class SettingsLocation(IntEnum):
		AssetsDirectory = 0
		DOTweenDirectory = 1
		DemigiantDirectory = 2

class SafeModeReport:
	class SafeModeReportType(IntEnum):
		Unset = 0
		TargetOrFieldMissing = 1
		Callback = 2
		StartupFailure = 3

class TweenManager:
	class CapacityIncreaseMode(IntEnum):
		TweenersAndSequences = 0
		TweenersOnly = 1
		SequencesOnly = 2

