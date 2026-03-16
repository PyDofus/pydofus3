from enum import IntEnum

class CompressionLevelWithAuto(IntEnum):
	Auto = -1
	Optimal = 0
	Fastest = 1
	NoCompression = 2

class ScreenshotQuality(IntEnum):
	Full = 0
	High = 1
	Medium = 2
	Low = 3

