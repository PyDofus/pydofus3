from enum import IntFlag

class ChangeLocaleResult(IntFlag):
	None_ = 0
	Success = 1
	Cancelled = 2
	Failed = 3

class LoadBankResult(IntFlag):
	None_ = 0
	Completed = 1
	Loaded = 3
	Pending = 4
	Loading = 8
	Error = 17
	Cancelled = 49
	ManagerNotInitialized = 81
	BankNotFound = 145
	LoadError = 273

class LoadBankSampleDataResult(IntFlag):
	None_ = 0
	Completed = 1
	Loaded = 3
	Pending = 4
	Loading = 8
	Error = 17
	Cancelled = 49
	ManagerNotInitialized = 81
	BankNotFound = 145
	LoadError = 273

class LoadEventSampleDataResult(IntFlag):
	None_ = 0
	Completed = 1
	Loaded = 3
	Loading = 4
	Error = 9
	Cancelled = 25
	ManagerNotInitialized = 41
	EventNotFound = 73
	LoadError = 137

class UnloadBankResult(IntFlag):
	None_ = 0
	Completed = 1
	Unloaded = 3
	Pending = 4
	Unloading = 8
	Error = 17
	Cancelled = 49
	ManagerNotInitialized = 81
	BankNotFound = 145
	UnloadError = 273

class UnloadBankSampleDataResult(IntFlag):
	None_ = 0
	Completed = 1
	Unloaded = 3
	Pending = 4
	Unloading = 8
	Error = 17
	Cancelled = 49
	ManagerNotInitialized = 81
	BankNotFound = 145
	UnloadError = 273

class UnloadEventSampleDataResult(IntFlag):
	None_ = 0
	Completed = 1
	Unloaded = 3
	Unloading = 4
	Error = 9
	Cancelled = 25
	ManagerNotInitialized = 41
	EventNotFound = 73
	UnloadError = 137

