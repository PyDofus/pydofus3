from enum import IntFlag

# Polly.CircuitBreaker.CircuitState
class CircuitState(IntFlag):
    Closed = 0
    Open = 1
    HalfOpen = 2
    Isolated = 3

