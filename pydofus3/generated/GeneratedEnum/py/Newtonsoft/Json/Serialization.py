from enum import IntFlag

# Newtonsoft.Json.Serialization.JsonContractType
class JsonContractType(IntFlag):
    NONE = 0
    Object = 1
    Array = 2
    Primitive = 3
    String = 4
    Dictionary = 5
    Dynamic = 6
    Serializable = 7
    Linq = 8

# Newtonsoft.Json.Serialization.JsonSerializerInternalReader
class JsonSerializerInternalReader(IntFlag):
    NONE = 0
    Null = 1
    Value = 2

