from enum import IntFlag

# UnityEngine.InputSystem.Utilities.JsonParser
class JsonParser(IntFlag):
    NONE = 0
    Bool = 1
    Real = 2
    Integer = 3
    String = 4
    Array = 5
    Object = 6
    Any = 7

