from enum import IntEnum

class Algorithm(IntEnum):
	X32 = 0
	X64 = 1

class LL:
	class limitedOutput_directive(IntEnum):
		notLimited = 0
		limitedOutput = 1
		fillOutput = 2

	class tableType_t(IntEnum):
		clearedTable = 0
		byPtr = 1
		byU32 = 2
		byU16 = 3

	class dict_directive(IntEnum):
		noDict = 0
		withPrefix64k = 1
		usingExtDict = 2
		usingDictCtx = 3

	class dictIssue_directive(IntEnum):
		noDictIssue = 0
		dictSmall = 1

	class endCondition_directive(IntEnum):
		endOnOutputSize = 0
		endOnInputSize = 1

	class earlyEnd_directive(IntEnum):
		full = 0
		partial = 1

	class variable_length_error(IntEnum):
		loop_error = -2
		initial_error = -1
		ok = 0

	class dictCtx_directive(IntEnum):
		noDictCtx = 0
		usingDictCtxHc = 1

	class repeat_state_e(IntEnum):
		rep_untested = 0
		rep_not = 1
		rep_confirmed = 2

	class HCfavor_e(IntEnum):
		favorCompressionRatio = 0
		favorDecompressionSpeed = 1

	class lz4hc_strat_e(IntEnum):
		lz4hc = 0
		lz4opt = 1

