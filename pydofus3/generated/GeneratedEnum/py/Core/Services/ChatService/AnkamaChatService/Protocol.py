from enum import IntFlag

# Core.Services.ChatService.AnkamaChatService.Protocol.CreateFriendInviteCmd
class CreateFriendInviteCmd(IntFlag):
    NONE = 0
    RecipientUserId = 2
    RecipientUserNameAndTag = 4

# Core.Services.ChatService.AnkamaChatService.Protocol.DeleteFriendInviteCmd
class DeleteFriendInviteCmd(IntFlag):
    Accepted = 0
    Rejected = 1
    Canceled = 2

# Core.Services.ChatService.AnkamaChatService.Protocol.Frame
class Frame(IntFlag):
    NONE = 0
    Request = 1
    Response = 2
    Event = 3

# Core.Services.ChatService.AnkamaChatService.Protocol.Frame
class Frame(IntFlag):
    Unknown = 0
    Success = 1
    Forbidden = 2
    BadRequest = 3
    Timeout = 4
    Failure = 5

# Core.Services.ChatService.AnkamaChatService.Protocol.ListChannelMessagesCmd
class ListChannelMessagesCmd(IntFlag):
    NONE = 0
    Before = 3
    After = 4

# Core.Services.ChatService.AnkamaChatService.Protocol.UserPresence
class UserPresence(IntFlag):
    Online = 0
    Offline = 1

# Core.Services.ChatService.AnkamaChatService.Protocol.UserStatus
class UserStatus(IntFlag):
    Available = 0
    Away = 1
    Busy = 2

