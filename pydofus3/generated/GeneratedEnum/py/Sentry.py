from enum import IntFlag

# Sentry.AttachmentType
class AttachmentType(IntFlag):
    Default = 0
    Minidump = 1
    AppleCrashReport = 2
    UnrealContext = 3
    UnrealLogs = 4
    ViewHierarchy = 5

# Sentry.BreadcrumbLevel
class BreadcrumbLevel(IntFlag):
    Debug = -1
    Info = 0
    Warning = 1
    Error = 2
    Critical = 3

# Sentry.CheckInStatus
class CheckInStatus(IntFlag):
    InProgress = 0
    Ok = 1
    Error = 2

# Sentry.CrashType
class CrashType(IntFlag):
    Managed = 0
    ManagedBackgroundThread = 1

# Sentry.DeduplicateMode
class DeduplicateMode(IntFlag):
    SameEvent = 1
    SameExceptionInstance = 2
    InnerException = 4
    AggregateException = 8
    All = 2147483647

# Sentry.InstructionAddressAdjustment
class InstructionAddressAdjustment(IntFlag):
    Auto = 0
    All = 1
    AllButFirst = 2
    NONE = 3

# Sentry.Instrumenter
class Instrumenter(IntFlag):
    Sentry = 0
    OpenTelemetry = 1

# Sentry.MeasurementUnit
class MeasurementUnit(IntFlag):
    Nanosecond = 0
    Microsecond = 1
    Millisecond = 2
    Second = 3
    Minute = 4
    Hour = 5
    Day = 6
    Week = 7

# Sentry.MeasurementUnit
class MeasurementUnit(IntFlag):
    Ratio = 0
    Percent = 1

# Sentry.MeasurementUnit
class MeasurementUnit(IntFlag):
    Bit = 0
    Byte = 1
    Kilobyte = 2
    Kibibyte = 3
    Megabyte = 4
    Mebibyte = 5
    Gigabyte = 6
    Gibibyte = 7
    Terabyte = 8
    Tebibyte = 9
    Petabyte = 10
    Pebibyte = 11
    Exabyte = 12
    Exbibyte = 13

# Sentry.ReportAssembliesMode
class ReportAssembliesMode(IntFlag):
    NONE = 0
    Version = 1
    InformationalVersion = 2

# Sentry.SentryLevel
class SentryLevel(IntFlag):
    Debug = 0
    Info = 1
    Warning = 2
    Error = 3
    Fatal = 4

# Sentry.SentryMonitorInterval
class SentryMonitorInterval(IntFlag):
    Year = 0
    Month = 1
    Week = 2
    Day = 3
    Hour = 4
    Minute = 5

# Sentry.SentryMonitorScheduleType
class SentryMonitorScheduleType(IntFlag):
    NONE = 0
    Crontab = 1
    Interval = 2

# Sentry.SentryOptions
class SentryOptions(IntFlag):
    AutoSessionTrackingIntegration = 1
    AppDomainUnhandledExceptionIntegration = 2
    AppDomainProcessExitIntegration = 4
    UnobservedTaskExceptionIntegration = 8

# Sentry.SessionEndStatus
class SessionEndStatus(IntFlag):
    Exited = 0
    Crashed = 1
    Abnormal = 2

# Sentry.SpanStatus
class SpanStatus(IntFlag):
    Ok = 0
    DeadlineExceeded = 1
    Unauthenticated = 2
    PermissionDenied = 3
    NotFound = 4
    ResourceExhausted = 5
    InvalidArgument = 6
    Unimplemented = 7
    Unavailable = 8
    InternalError = 9
    UnknownError = 10
    Cancelled = 11
    AlreadyExists = 12
    FailedPrecondition = 13
    Aborted = 14
    OutOfRange = 15
    DataLoss = 16

# Sentry.StackTraceMode
class StackTraceMode(IntFlag):
    Original = 0
    Enhanced = 1

# Sentry.StartupTimeDetectionMode
class StartupTimeDetectionMode(IntFlag):
    NONE = 0
    Fast = 1
    Best = 2

# Sentry.TransactionNameSource
class TransactionNameSource(IntFlag):
    Custom = 0
    Url = 1
    Route = 2
    View = 3
    Component = 4
    Task = 5

