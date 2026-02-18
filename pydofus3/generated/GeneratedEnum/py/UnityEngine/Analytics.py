from enum import IntFlag

# UnityEngine.Analytics.AnalyticsSessionState
class AnalyticsSessionState(IntFlag):
    kSessionStopped = 0
    kSessionStarted = 1
    kSessionPaused = 2
    kSessionResumed = 3

# UnityEngine.Analytics.SendEventOptions
class SendEventOptions(IntFlag):
    kAppendNone = 0
    kAppendBuildGuid = 1
    kAppendBuildTarget = 2

