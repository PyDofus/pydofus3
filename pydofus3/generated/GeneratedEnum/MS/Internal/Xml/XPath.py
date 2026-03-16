from enum import IntEnum

class AstNode:
	class AstType(IntEnum):
		Axis = 0
		Operator = 1
		Filter = 2
		ConstantOperand = 3
		Function = 4
		Group = 5
		Root = 6
		Variable = 7
		Error = 8

class Axis:
	class AxisType(IntEnum):
		Ancestor = 0
		AncestorOrSelf = 1
		Attribute = 2
		Child = 3
		Descendant = 4
		DescendantOrSelf = 5
		Following = 6
		FollowingSibling = 7
		Namespace = 8
		Parent = 9
		Preceding = 10
		PrecedingSibling = 11
		Self = 12
		None_ = 13

class Function:
	class FunctionType(IntEnum):
		FuncLast = 0
		FuncPosition = 1
		FuncCount = 2
		FuncID = 3
		FuncLocalName = 4
		FuncNameSpaceUri = 5
		FuncName = 6
		FuncString = 7
		FuncBoolean = 8
		FuncNumber = 9
		FuncTrue = 10
		FuncFalse = 11
		FuncNot = 12
		FuncConcat = 13
		FuncStartsWith = 14
		FuncContains = 15
		FuncSubstringBefore = 16
		FuncSubstringAfter = 17
		FuncSubstring = 18
		FuncStringLength = 19
		FuncNormalize = 20
		FuncTranslate = 21
		FuncLang = 22
		FuncSum = 23
		FuncFloor = 24
		FuncCeiling = 25
		FuncRound = 26
		FuncUserDefined = 27

class Operator:
	class Op(IntEnum):
		INVALID = 0
		OR = 1
		AND = 2
		EQ = 3
		NE = 4
		LT = 5
		LE = 6
		GT = 7
		GE = 8
		PLUS = 9
		MINUS = 10
		MUL = 11
		DIV = 12
		MOD = 13
		UNION = 14

class QueryBuilder:
	class Flags(IntEnum):
		None_ = 0
		SmartDesc = 1
		PosFilter = 2
		Filter = 4

	class Props(IntEnum):
		None_ = 0
		PosFilter = 1
		HasPosition = 2
		HasLast = 4
		NonFlat = 8

class QueryProps(IntEnum):
	None_ = 0
	Position = 1
	Count = 2
	Cached = 4
	Reverse = 8
	Merge = 16

class XPathScanner:
	class LexKind(IntEnum):
		Bang = 33
		Quote = 34
		Dollar = 36
		Apos = 39
		LParens = 40
		RParens = 41
		Star = 42
		Plus = 43
		Comma = 44
		Minus = 45
		Dot = 46
		Slash = 47
		Lt = 60
		Eq = 61
		Gt = 62
		At = 64
		And = 65
		DotDot = 68
		Eof = 69
		Ge = 71
		Le = 76
		Ne = 78
		Or = 79
		SlashSlash = 83
		LBracket = 91
		RBracket = 93
		Axe = 97
		Number = 100
		Name = 110
		String = 115
		Union = 124

