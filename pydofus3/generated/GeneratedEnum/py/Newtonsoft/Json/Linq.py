from enum import IntFlag

# Newtonsoft.Json.Linq.CommentHandling
class CommentHandling(IntFlag):
    Ignore = 0
    Load = 1

# Newtonsoft.Json.Linq.DuplicatePropertyNameHandling
class DuplicatePropertyNameHandling(IntFlag):
    Replace = 0
    Ignore = 1
    Error = 2

# Newtonsoft.Json.Linq.JTokenType
class JTokenType(IntFlag):
    NONE = 0
    Object = 1
    Array = 2
    Constructor = 3
    Property = 4
    Comment = 5
    Integer = 6
    Float = 7
    String = 8
    Boolean = 9
    Null = 10
    Undefined = 11
    Date = 12
    Raw = 13
    Bytes = 14
    Guid = 15
    Uri = 16
    TimeSpan = 17

# Newtonsoft.Json.Linq.LineInfoHandling
class LineInfoHandling(IntFlag):
    Ignore = 0
    Load = 1

# Newtonsoft.Json.Linq.MergeArrayHandling
class MergeArrayHandling(IntFlag):
    Concat = 0
    Union = 1
    Replace = 2
    Merge = 3

# Newtonsoft.Json.Linq.MergeNullValueHandling
class MergeNullValueHandling(IntFlag):
    Ignore = 0
    Merge = 1

