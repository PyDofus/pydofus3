from enum import IntFlag

# Mono.CompilerServices.SymbolWriter.CapturedVariable
class CapturedVariable(IntFlag):
    Local = 0
    Parameter = 1
    This = 2

# Mono.CompilerServices.SymbolWriter.CodeBlockEntry
class CodeBlockEntry(IntFlag):
    Lexical = 1
    CompilerGenerated = 2
    IteratorBody = 3
    IteratorDispatcher = 4

# Mono.CompilerServices.SymbolWriter.MethodEntry
class MethodEntry(IntFlag):
    LocalNamesAmbiguous = 1
    ColumnsInfoIncluded = 2
    EndInfoIncluded = 4

# Mono.CompilerServices.SymbolWriter.OffsetTable
class OffsetTable(IntFlag):
    IsAspxSource = 1
    WindowsFileNames = 2

