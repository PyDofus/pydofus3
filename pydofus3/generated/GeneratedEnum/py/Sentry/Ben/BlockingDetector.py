from enum import IntFlag

# Sentry.Ben.BlockingDetector.DetectionSource
class DetectionSource(IntFlag):
    SynchronizationContext = 0
    EventListener = 1

