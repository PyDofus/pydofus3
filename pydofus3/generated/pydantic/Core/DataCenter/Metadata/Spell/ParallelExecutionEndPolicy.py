from pydofus3.not_generated.base import OpenAPIIntEnum


class ParallelExecutionEndPolicy(OpenAPIIntEnum):
	Unknown = 0
	WaitForFirstOne = 1
	WaitForAll = 2
	DontWait = 3

