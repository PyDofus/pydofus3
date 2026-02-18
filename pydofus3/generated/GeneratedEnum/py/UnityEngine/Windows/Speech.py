from enum import IntFlag

# UnityEngine.Windows.Speech.ConfidenceLevel
class ConfidenceLevel(IntFlag):
    High = 0
    Medium = 1
    Low = 2
    Rejected = 3

# UnityEngine.Windows.Speech.DictationCompletionCause
class DictationCompletionCause(IntFlag):
    Complete = 0
    AudioQualityFailure = 1
    Canceled = 2
    TimeoutExceeded = 3
    PauseLimitExceeded = 4
    NetworkFailure = 5
    MicrophoneUnavailable = 6
    UnknownError = 7

# UnityEngine.Windows.Speech.SpeechError
class SpeechError(IntFlag):
    NoError = 0
    TopicLanguageNotSupported = 1
    GrammarLanguageMismatch = 2
    GrammarCompilationFailure = 3
    AudioQualityFailure = 4
    PauseLimitExceeded = 5
    TimeoutExceeded = 6
    NetworkFailure = 7
    MicrophoneUnavailable = 8
    UnknownError = 9

# UnityEngine.Windows.Speech.SpeechSystemStatus
class SpeechSystemStatus(IntFlag):
    Stopped = 0
    Running = 1
    Failed = 2

