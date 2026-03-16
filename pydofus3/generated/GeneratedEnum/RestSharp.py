from enum import IntEnum

class DataFormat(IntEnum):
	Json = 0
	Xml = 1
	None_ = 2

class Method(IntEnum):
	GET = 0
	POST = 1
	PUT = 2
	DELETE = 3
	HEAD = 4
	OPTIONS = 5
	PATCH = 6
	MERGE = 7
	COPY = 8

class ParameterType(IntEnum):
	Cookie = 0
	GetOrPost = 1
	UrlSegment = 2
	HttpHeader = 3
	RequestBody = 4
	QueryString = 5
	QueryStringWithoutEncode = 6

class ResponseStatus(IntEnum):
	None_ = 0
	Completed = 1
	Error = 2
	TimedOut = 3
	Aborted = 4

