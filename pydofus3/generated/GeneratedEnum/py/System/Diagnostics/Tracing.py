from enum import IntFlag

# System.Diagnostics.Tracing.EventKeywords
class EventKeywords(IntFlag):
    NONE = 0
    All = -1
    MicrosoftTelemetry = 562949953421312
    WdiContext = 562949953421312
    WdiDiagnostic = 1125899906842624
    Sqm = 2251799813685248
    AuditFailure = 4503599627370496
    AuditSuccess = 9007199254740992
    CorrelationHint = 4503599627370496
    EventLogClassic = 36028797018963968

# System.Diagnostics.Tracing.EventLevel
class EventLevel(IntFlag):
    LogAlways = 0
    Critical = 1
    Error = 2
    Warning = 3
    Informational = 4
    Verbose = 5

# System.Diagnostics.Tracing.EventOpcode
class EventOpcode(IntFlag):
    Info = 0
    Start = 1
    Stop = 2
    DataCollectionStart = 3
    DataCollectionStop = 4
    Extension = 5
    Reply = 6
    Resume = 7
    Suspend = 8
    Send = 9
    Receive = 240

# System.Diagnostics.Tracing.EventTask
class EventTask(IntFlag):
    NONE = 0

