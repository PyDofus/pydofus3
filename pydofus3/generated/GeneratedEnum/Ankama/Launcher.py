from enum import IntEnum

class ZaapWorker:
	class WorkerStatus(IntEnum):
		Stopped = 0
		Starting = 1
		Stopping = 2
		Started = 3
		Failed = 4

