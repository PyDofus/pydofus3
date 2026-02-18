from enum import IntFlag

# System.Reflection.Emit.AssemblyBuilderAccess
class AssemblyBuilderAccess(IntFlag):
    Run = 1
    Save = 2
    RunAndSave = 3
    ReflectionOnly = 6
    RunAndCollect = 9

# System.Reflection.Emit.OpCodeType
class OpCodeType(IntFlag):
    Annotation = 0
    Macro = 1
    Nternal = 2
    Objmodel = 3
    Prefix = 4
    Primitive = 5

# System.Reflection.Emit.OperandType
class OperandType(IntFlag):
    InlineBrTarget = 0
    InlineField = 1
    InlineI = 2
    InlineI8 = 3
    InlineMethod = 4
    InlineNone = 5
    InlinePhi = 6
    InlineR = 7
    InlineSig = 9
    InlineString = 10
    InlineSwitch = 11
    InlineTok = 12
    InlineType = 13
    InlineVar = 14
    ShortInlineBrTarget = 15
    ShortInlineI = 16
    ShortInlineR = 17
    ShortInlineVar = 18

# System.Reflection.Emit.PEFileKinds
class PEFileKinds(IntFlag):
    Dll = 1
    ConsoleApplication = 2
    WindowApplication = 3

