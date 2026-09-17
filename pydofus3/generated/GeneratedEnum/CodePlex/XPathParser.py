from enum import IntEnum

class LexKind(IntEnum):
	Unknown = 0
	Or = 1
	And = 2
	Eq = 3
	Ne = 4
	Lt = 5
	Le = 6
	Gt = 7
	Ge = 8
	Plus = 9
	Minus = 10
	Multiply = 11
	Divide = 12
	Modulo = 13
	UnaryMinus = 14
	Union = 15
	LastOperator = 15
	DotDot = 16
	ColonColon = 17
	SlashSlash = 18
	Number = 19
	Axis = 20
	Name = 21
	FirstStringable = 21
	String = 22
	Eof = 23
	LastNonChar = 23
	Dollar = 36
	LParens = 40
	RParens = 41
	Star = 42
	Comma = 44
	Dot = 46
	Slash = 47
	At = 64
	LBracket = 91
	RBracket = 93
	RBrace = 125

class XPathAxis(IntEnum):
	Unknown = 0
	Ancestor = 1
	AncestorOrSelf = 2
	Attribute = 3
	Child = 4
	Descendant = 5
	DescendantOrSelf = 6
	Following = 7
	FollowingSibling = 8
	Namespace = 9
	Parent = 10
	Preceding = 11
	PrecedingSibling = 12
	Self = 13
	Root = 14

class XPathOperator(IntEnum):
	Unknown = 0
	Or = 1
	And = 2
	Eq = 3
	Ne = 4
	Lt = 5
	Le = 6
	Gt = 7
	Ge = 8
	Plus = 9
	Minus = 10
	Multiply = 11
	Divide = 12
	Modulo = 13
	UnaryMinus = 14
	Union = 15

class XPathParserException:
	class TrimType(IntEnum):
		Left = 0
		Right = 1
		Middle = 2

