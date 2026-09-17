from enum import IntFlag

class InstructionFieldUsage(IntFlag):
	None_ = 0
	Symbol = 1
	SymbolList = 2
	Name = 4
	Value = 8
	NumVal = 16
	NumVal2 = 32
	NumValAsCodeAddress = 32784

