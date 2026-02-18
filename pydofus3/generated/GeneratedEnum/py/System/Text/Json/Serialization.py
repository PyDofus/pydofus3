from enum import IntFlag

# System.Text.Json.Serialization.JsonIgnoreCondition
class JsonIgnoreCondition(IntFlag):
    Never = 0
    Always = 1
    WhenWritingDefault = 2
    WhenWritingNull = 3

# System.Text.Json.Serialization.JsonKnownNamingPolicy
class JsonKnownNamingPolicy(IntFlag):
    Unspecified = 0
    CamelCase = 1

# System.Text.Json.Serialization.JsonNumberHandling
class JsonNumberHandling(IntFlag):
    Strict = 0
    AllowReadingFromString = 1
    WriteAsString = 2
    AllowNamedFloatingPointLiterals = 4

# System.Text.Json.Serialization.JsonSourceGenerationMode
class JsonSourceGenerationMode(IntFlag):
    Default = 0
    Metadata = 1
    Serialization = 2

# System.Text.Json.Serialization.JsonUnknownTypeHandling
class JsonUnknownTypeHandling(IntFlag):
    JsonElement = 0
    JsonNode = 1

# System.Text.Json.Serialization.ReferenceHandlingStrategy
class ReferenceHandlingStrategy(IntFlag):
    NONE = 0
    Preserve = 1
    IgnoreCycles = 2

