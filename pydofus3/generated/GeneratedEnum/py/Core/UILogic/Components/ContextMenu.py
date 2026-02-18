from enum import IntFlag

# Core.UILogic.Components.ContextMenu.ContextMenuItem
class ContextMenuItem(IntFlag):
    NONE = 0
    Checkbox = 1
    RadioButton = 2
    AssetToggle = 3
    ColorSquare = 4

# Core.UILogic.Components.ContextMenu.ContextMenuPageSwitchItem
class ContextMenuPageSwitchItem(IntFlag):
    Previous = 0
    Next = 1

