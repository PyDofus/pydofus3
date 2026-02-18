from enum import IntFlag

# Unity.Properties.InstantiationKind
class InstantiationKind(IntFlag):
    Activator = 0
    PropertyBagOverride = 1
    NotInstantiatable = 2

# Unity.Properties.PropertyCollection
class PropertyCollection(IntFlag):
    Empty = 0
    Enumerable = 1
    List = 2
    IndexedCollectionPropertyBag = 3

# Unity.Properties.PropertyPathPartKind
class PropertyPathPartKind(IntFlag):
    Name = 0
    Index = 1
    Key = 2

# Unity.Properties.TypeGenerationOptions
class TypeGenerationOptions(IntFlag):
    NONE = 0
    ValueType = 2
    ReferenceType = 4
    Default = 6

# Unity.Properties.VisitExceptionKind
class VisitExceptionKind(IntFlag):
    NONE = 0
    Internal = 1
    Visitor = 2
    All = 3

# Unity.Properties.VisitReturnCode
class VisitReturnCode(IntFlag):
    Ok = 0
    NullContainer = 1
    InvalidContainerType = 2
    MissingPropertyBag = 3
    InvalidPath = 4
    InvalidCast = 5
    AccessViolation = 6

