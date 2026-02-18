from enum import IntFlag

# System.Text.NormalizationCheck
class NormalizationCheck(IntFlag):
    Yes = 0
    No = 1
    Maybe = 2

# System.Text.NormalizationForm
class NormalizationForm(IntFlag):
    FormC = 1
    FormD = 2
    FormKC = 5
    FormKD = 6

