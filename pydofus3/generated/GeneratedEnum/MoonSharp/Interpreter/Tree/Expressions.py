from enum import IntFlag

class BinaryOperatorExpression:
	class Operator(IntFlag):
		NotAnOperator = 0
		Or = 1
		And = 2
		Less = 4
		Greater = 8
		LessOrEqual = 16
		GreaterOrEqual = 32
		NotEqual = 64
		Equal = 128
		StrConcat = 256
		Add = 512
		Sub = 1024
		Mul = 4096
		Div = 8192
		Mod = 16384
		Power = 32768

