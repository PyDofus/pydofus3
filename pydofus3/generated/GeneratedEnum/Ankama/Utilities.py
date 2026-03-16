from enum import IntEnum

class Device:
	class Type(IntEnum):
		PC = 0
		Mobile = 1
		Tablet = 2

class StreamingAssetRequest:
	class Result(IntEnum):
		InProgress = 0
		Success = 1
		Error = 2
		FileNotFoundError = 3
		AccessDeniedError = 4

