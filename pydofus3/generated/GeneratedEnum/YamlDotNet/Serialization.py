from enum import IntFlag

class DefaultValuesHandling(IntFlag):
	Preserve = 0
	OmitNull = 1
	OmitDefaults = 2
	OmitEmptyCollections = 4

