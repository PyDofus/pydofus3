from enum import IntFlag

# System.Collections.Specialized.NotifyCollectionChangedAction
class NotifyCollectionChangedAction(IntFlag):
    Add = 0
    Remove = 1
    Replace = 2
    Move = 3
    Reset = 4

