from enum import IntEnum

class LabelEventParamType:
	class Bool(IntEnum):
		pass

	class Int(IntEnum):
		ShakeStrength = 0
		ShakeRotation = 1

	class Float(IntEnum):
		ShakeDuration = 0

	class String(IntEnum):
		pass

class LabelEventType(IntEnum):
	LabelShot = 0
	ShakeCam = 1
	Transfo = 2

