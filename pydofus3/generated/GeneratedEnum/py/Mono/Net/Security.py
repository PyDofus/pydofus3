from enum import IntFlag

# Mono.Net.Security.AsyncOperationStatus
class AsyncOperationStatus(IntFlag):
    Initialize = 0
    Continue = 1
    ReadDone = 2
    Complete = 3

# Mono.Net.Security.MobileAuthenticatedStream
class MobileAuthenticatedStream(IntFlag):
    NONE = 0
    Handshake = 1
    Authenticated = 2
    Renegotiate = 3
    Read = 4
    Write = 5
    Close = 6

# Mono.Net.Security.MobileAuthenticatedStream
class MobileAuthenticatedStream(IntFlag):
    Read = 0
    Write = 1
    Renegotiate = 2
    Shutdown = 3

