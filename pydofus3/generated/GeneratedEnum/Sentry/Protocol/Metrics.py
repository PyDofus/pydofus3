from enum import IntEnum

class MetricType(IntEnum):
	Counter = 0
	Gauge = 1
	Distribution = 2
	Set = 3

