from enum import IntEnum

class ZaapClient:
	class ParametersSources(IntEnum):
		ENV_VARIABLES_FIRST = 0
		FILE_FIRST = 1
		ONLY_ENV_VARIABLES = 2
		ONLY_FILE = 3

