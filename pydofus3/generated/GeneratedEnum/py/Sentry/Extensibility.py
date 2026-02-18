from enum import IntFlag

# Sentry.Extensibility.RequestSize
class RequestSize(IntFlag):
    NONE = 0
    Small = 1
    Medium = 2
    Always = 3

