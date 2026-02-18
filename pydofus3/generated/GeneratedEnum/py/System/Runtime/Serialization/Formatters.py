from enum import IntFlag

# System.Runtime.Serialization.Formatters.FormatterAssemblyStyle
class FormatterAssemblyStyle(IntFlag):
    Simple = 0
    Full = 1

# System.Runtime.Serialization.Formatters.FormatterTypeStyle
class FormatterTypeStyle(IntFlag):
    TypesWhenNeeded = 0
    TypesAlways = 1
    XsdString = 2

# System.Runtime.Serialization.Formatters.TypeFilterLevel
class TypeFilterLevel(IntFlag):
    Low = 2
    Full = 3

