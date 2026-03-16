from enum import IntEnum

class CodeGeneratorResponse:
	class Types:
		class Feature(IntEnum):
			None_ = 0
			Proto3Optional = 1
			SupportsEditions = 2

