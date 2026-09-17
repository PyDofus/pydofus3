from enum import IntEnum

class HierarchyPathQuery:
	class LogSeverity(IntEnum):
		Debug = 1
		Trace = 2
		Info = 4
		Warn = 8
		Error = 16
		LogTree = 32
		Performance = 64
		FlushFile = 128

class HierarchyPathVM:
	class Operation(IntEnum):
		Exit = 0
		EvaluateNode = 1
		EvaluateOperator = 2
		EvaluateLeftOp = 3
		EvaluateRightOp = 4
		EvaluatePredicateContext = 5
		EvaluatePredicateCondition = 6
		ProcessFunction = 7
		EvaluateFunctionContext = 8
		EvaluateFunctionCondition = 9
		RetrieveResult = 10
		StoreResult = 11
		Break = 12

class HNodeType(IntEnum):
	Object = 0
	Number = 1
	String = 2
	Variable = 3
	Function = 4
	Predicate = 5
	Operator = 6
	Step = 7
	Axis = 8
	UNASSIGNED = 9

