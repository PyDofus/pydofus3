from enum import IntEnum

class CreateFriendInviteCmd:
	class RecipientOneofCase(IntEnum):
		None_ = 0
		RecipientUserId = 2
		RecipientUserNameAndTag = 4

class DeleteFriendInviteCmd:
	class Types:
		class Reason(IntEnum):
			Accepted = 0
			Rejected = 1
			Canceled = 2

class Frame:
	class ContentOneofCase(IntEnum):
		None_ = 0
		Request = 1
		Response = 2
		Event = 3

	class Types:
		class Response:
			class Types:
				class Status(IntEnum):
					Unknown = 0
					Success = 1
					Forbidden = 2
					BadRequest = 3
					Timeout = 4
					Failure = 5

class ListChannelMessagesCmd:
	class DirectionOneofCase(IntEnum):
		None_ = 0
		Before = 3
		After = 4

class UserPresence(IntEnum):
	Online = 0
	Offline = 1

class UserStatus(IntEnum):
	Available = 0
	Away = 1
	Busy = 2

