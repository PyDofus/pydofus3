from enum import IntEnum

class ResourceLeakDetector:
	class DetectionLevel(IntEnum):
		Disabled = 0
		Simple = 1
		Advanced = 2
		Paranoid = 3

