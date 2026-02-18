from enum import IntFlag

# Newtonsoft.Json.Schema.JsonSchemaType
class JsonSchemaType(IntFlag):
    NONE = 0
    String = 1
    Float = 2
    Integer = 4
    Boolean = 8
    Object = 16
    Array = 32
    Null = 64
    Any = 127

# Newtonsoft.Json.Schema.UndefinedSchemaIdHandling
class UndefinedSchemaIdHandling(IntFlag):
    NONE = 0
    UseTypeName = 1
    UseAssemblyQualifiedName = 2

