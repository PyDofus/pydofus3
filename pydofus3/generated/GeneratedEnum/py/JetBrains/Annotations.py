from enum import IntFlag

# JetBrains.Annotations.CollectionAccessType
class CollectionAccessType(IntFlag):
    NONE = 0
    Read = 1
    ModifyExistingContent = 2
    UpdatedContent = 6

# JetBrains.Annotations.ImplicitUseKindFlags
class ImplicitUseKindFlags(IntFlag):
    Default = 7
    Access = 1
    Assign = 2
    InstantiatedWithFixedConstructorSignature = 4
    InstantiatedNoFixedConstructorSignature = 8

# JetBrains.Annotations.ImplicitUseTargetFlags
class ImplicitUseTargetFlags(IntFlag):
    Default = 1
    Itself = 1
    Members = 2
    WithMembers = 3

