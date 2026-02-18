from enum import IntFlag

# Core.Engine.OptionJSON.DataStoreBinding
class DataStoreBinding(IntFlag):
    Shared = 0
    Account = 1
    Character = 2
    NONE = -1

