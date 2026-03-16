from enum import IntEnum
from enum import IntFlag

class AttachmentType(IntEnum):
	Default = 0
	Minidump = 1
	AppleCrashReport = 2
	UnrealContext = 3
	UnrealLogs = 4
	ViewHierarchy = 5

class BreadcrumbLevel(IntEnum):
	Debug = -1
	Info = 0
	Warning = 1
	Error = 2
	Critical = 3

class CheckInStatus(IntEnum):
	InProgress = 0
	Ok = 1
	Error = 2

class CrashType(IntEnum):
	Managed = 0
	ManagedBackgroundThread = 1

class DeduplicateMode(IntFlag):
	SameEvent = 1
	SameExceptionInstance = 2
	InnerException = 4
	AggregateException = 8
	All = 2147483647

class InstructionAddressAdjustment(IntEnum):
	Auto = 0
	All = 1
	AllButFirst = 2
	None_ = 3

class Instrumenter(IntEnum):
	Sentry = 0
	OpenTelemetry = 1

class MeasurementUnit:
	class Duration(IntEnum):
		Nanosecond = 0
		Microsecond = 1
		Millisecond = 2
		Second = 3
		Minute = 4
		Hour = 5
		Day = 6
		Week = 7

	class Fraction(IntEnum):
		Ratio = 0
		Percent = 1

	class Information(IntEnum):
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

class ReportAssembliesMode(IntEnum):
	None_ = 0
	Version = 1
	InformationalVersion = 2

class SentryLevel(IntEnum):
	Debug = 0
	Info = 1
	Warning = 2
	Error = 3
	Fatal = 4

class SentryMonitorInterval(IntEnum):
	Year = 0
	Month = 1
	Week = 2
	Day = 3
	Hour = 4
	Minute = 5

class SentryMonitorScheduleType(IntEnum):
	None_ = 0
	Crontab = 1
	Interval = 2

class SentryOptions:
	class DefaultIntegrations(IntFlag):
		AutoSessionTrackingIntegration = 1
		AppDomainUnhandledExceptionIntegration = 2
		AppDomainProcessExitIntegration = 4
		UnobservedTaskExceptionIntegration = 8

class SessionEndStatus(IntEnum):
	Exited = 0
	Crashed = 1
	Abnormal = 2

class SpanStatus(IntEnum):
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

class StackTraceMode(IntEnum):
	Original = 0
	Enhanced = 1

class StartupTimeDetectionMode(IntEnum):
	None_ = 0
	Fast = 1
	Best = 2

class TransactionNameSource(IntEnum):
	Custom = 0
	Url = 1
	Route = 2
	View = 3
	Component = 4
	Task = 5

