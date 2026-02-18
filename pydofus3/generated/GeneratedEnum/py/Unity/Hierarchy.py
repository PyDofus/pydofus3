from enum import IntFlag

# Unity.Hierarchy.HierarchyNodeFlags
class HierarchyNodeFlags(IntFlag):
    NONE = 0
    Expanded = 1
    Selected = 2
    Cut = 4
    Hidden = 8

# Unity.Hierarchy.HierarchyPropertyStorageType
class HierarchyPropertyStorageType(IntFlag):
    Sparse = 0
    Dense = 1
    Blob = 2
    Default = 1

# Unity.Hierarchy.HierarchySearchFilterOperator
class HierarchySearchFilterOperator(IntFlag):
    Equal = 0
    Contains = 1
    Greater = 2
    GreaterOrEqual = 3
    Lesser = 4
    LesserOrEqual = 5
    NotEqual = 6
    Not = 7

