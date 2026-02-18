from enum import IntFlag

# Ankama.AudioManagement.AsyncOperations.ChangeLocaleResult
class ChangeLocaleResult(IntFlag):
    NONE = 0
    Success = 1
    Cancelled = 2
    Failed = 3

# Ankama.AudioManagement.AsyncOperations.LoadBankResult
class LoadBankResult(IntFlag):
    NONE = 0
    Completed = 1
    Loaded = 3
    Pending = 4
    Loading = 8
    Error = 17
    Cancelled = 49
    ManagerNotInitialized = 81
    BankNotFound = 145
    LoadError = 273

# Ankama.AudioManagement.AsyncOperations.LoadBankSampleDataResult
class LoadBankSampleDataResult(IntFlag):
    NONE = 0
    Completed = 1
    Loaded = 3
    Pending = 4
    Loading = 8
    Error = 17
    Cancelled = 49
    ManagerNotInitialized = 81
    BankNotFound = 145
    LoadError = 273

# Ankama.AudioManagement.AsyncOperations.LoadEventSampleDataResult
class LoadEventSampleDataResult(IntFlag):
    NONE = 0
    Completed = 1
    Loaded = 3
    Loading = 4
    Error = 9
    Cancelled = 25
    ManagerNotInitialized = 41
    EventNotFound = 73
    LoadError = 137

# Ankama.AudioManagement.AsyncOperations.UnloadBankResult
class UnloadBankResult(IntFlag):
    NONE = 0
    Completed = 1
    Unloaded = 3
    Pending = 4
    Unloading = 8
    Error = 17
    Cancelled = 49
    ManagerNotInitialized = 81
    BankNotFound = 145
    UnloadError = 273

# Ankama.AudioManagement.AsyncOperations.UnloadBankSampleDataResult
class UnloadBankSampleDataResult(IntFlag):
    NONE = 0
    Completed = 1
    Unloaded = 3
    Pending = 4
    Unloading = 8
    Error = 17
    Cancelled = 49
    ManagerNotInitialized = 81
    BankNotFound = 145
    UnloadError = 273

# Ankama.AudioManagement.AsyncOperations.UnloadEventSampleDataResult
class UnloadEventSampleDataResult(IntFlag):
    NONE = 0
    Completed = 1
    Unloaded = 3
    Unloading = 4
    Error = 9
    Cancelled = 25
    ManagerNotInitialized = 41
    EventNotFound = 73
    UnloadError = 137

