from enum import IntFlag

# QFSW.QC.Utilities.Commands.CommandChainingType
class CommandChainingType(IntFlag):
    Unknown = 0
    Or = 1
    And = 2
    Xor = 3

