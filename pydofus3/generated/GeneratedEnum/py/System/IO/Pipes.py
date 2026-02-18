from enum import IntFlag

# System.IO.Pipes.PipeAccessRights
class PipeAccessRights(IntFlag):
    ReadData = 1
    WriteData = 2
    ReadAttributes = 128
    WriteAttributes = 256
    ReadExtendedAttributes = 8
    WriteExtendedAttributes = 16
    CreateNewInstance = 4
    Delete = 65536
    ReadPermissions = 131072
    ChangePermissions = 262144
    TakeOwnership = 524288
    Synchronize = 1048576
    FullControl = 2032031
    Read = 131209
    Write = 274
    ReadWrite = 131483
    AccessSystemSecurity = 16777216

# System.IO.Pipes.PipeDirection
class PipeDirection(IntFlag):
    In = 1
    Out = 2
    InOut = 3

# System.IO.Pipes.PipeOptions
class PipeOptions(IntFlag):
    NONE = 0
    WriteThrough = -2147483648
    Asynchronous = 1073741824
    CurrentUserOnly = 536870912

# System.IO.Pipes.PipeState
class PipeState(IntFlag):
    WaitingToConnect = 0
    Connected = 1
    Broken = 2
    Disconnected = 3
    Closed = 4

# System.IO.Pipes.PipeTransmissionMode
class PipeTransmissionMode(IntFlag):
    Byte = 0
    Message = 1

