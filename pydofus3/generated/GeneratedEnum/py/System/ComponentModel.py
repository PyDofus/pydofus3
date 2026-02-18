from enum import IntFlag

# System.ComponentModel.CollectionChangeAction
class CollectionChangeAction(IntFlag):
    Add = 1
    Remove = 2
    Refresh = 3

# System.ComponentModel.DesignerSerializationVisibility
class DesignerSerializationVisibility(IntFlag):
    Hidden = 0
    Visible = 1
    Content = 2

# System.ComponentModel.EditorBrowsableState
class EditorBrowsableState(IntFlag):
    Always = 0
    Never = 1
    Advanced = 2

# System.ComponentModel.ListChangedType
class ListChangedType(IntFlag):
    Reset = 0
    ItemAdded = 1
    ItemDeleted = 2
    ItemMoved = 3
    ItemChanged = 4
    PropertyDescriptorAdded = 5
    PropertyDescriptorDeleted = 6
    PropertyDescriptorChanged = 7

# System.ComponentModel.ListSortDirection
class ListSortDirection(IntFlag):
    Ascending = 0
    Descending = 1

# System.ComponentModel.RefreshProperties
class RefreshProperties(IntFlag):
    NONE = 0
    All = 1
    Repaint = 2

