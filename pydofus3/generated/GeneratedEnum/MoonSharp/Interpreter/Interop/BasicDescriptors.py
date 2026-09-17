from enum import IntFlag

class MemberDescriptorAccess(IntFlag):
	CanRead = 1
	CanWrite = 2
	CanExecute = 4

