from enum import IntFlag

# System.Collections.Immutable.ImmutableDictionary
class ImmutableDictionary(IntFlag):
    BeforeFirst = 0
    First = 1
    Additional = 2
    End = 3

# System.Collections.Immutable.ImmutableDictionary
class ImmutableDictionary(IntFlag):
    SetValue = 0
    Skip = 1
    ThrowIfValueDifferent = 2
    ThrowAlways = 3

# System.Collections.Immutable.ImmutableDictionary
class ImmutableDictionary(IntFlag):
    AppliedWithoutSizeChange = 0
    SizeChanged = 1
    NoChangeRequired = 2

# System.Collections.Immutable.ImmutableHashSet
class ImmutableHashSet(IntFlag):
    SizeChanged = 0
    NoChangeRequired = 1

# System.Collections.Immutable.ImmutableHashSet
class ImmutableHashSet(IntFlag):
    BeforeFirst = 0
    First = 1
    Additional = 2
    End = 3

# System.Collections.Immutable.ImmutableHashSet
class ImmutableHashSet(IntFlag):
    Adjustment = 0
    FinalValue = 1

