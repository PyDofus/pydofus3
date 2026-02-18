from enum import IntFlag

# UnityEngineInternal.TypeInferenceRules
class TypeInferenceRules(IntFlag):
    TypeReferencedByFirstArgument = 0
    TypeReferencedBySecondArgument = 1
    ArrayOfTypeReferencedByFirstArgument = 2
    TypeOfFirstArgument = 3

