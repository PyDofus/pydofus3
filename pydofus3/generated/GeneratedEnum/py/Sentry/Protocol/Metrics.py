from enum import IntFlag

# Sentry.Protocol.Metrics.MetricType
class MetricType(IntFlag):
    Counter = 0
    Gauge = 1
    Distribution = 2
    Set = 3

