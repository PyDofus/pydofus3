from enum import IntFlag

# System.Data.AcceptRejectRule
class AcceptRejectRule(IntFlag):
    NONE = 0
    Cascade = 1

# System.Data.Aggregate
class Aggregate(IntFlag):
    NONE = -1
    Sum = 30
    Avg = 31
    Min = 32
    Max = 33
    Count = 34
    StDev = 35
    Var = 37

# System.Data.AggregateType
class AggregateType(IntFlag):
    NONE = 0
    Sum = 4
    Mean = 5
    Min = 6
    Max = 7
    First = 8
    Count = 9
    Var = 10
    StDev = 11

# System.Data.BinaryNode
class BinaryNode(IntFlag):
    SqlDateTime = 25
    DateTimeOffset = 24
    DateTime = 23
    TimeSpan = 20
    SqlDouble = 19
    Double = 18
    SqlSingle = 17
    Single = 16
    SqlDecimal = 15
    Decimal = 14
    SqlMoney = 13
    UInt64 = 12
    SqlInt64 = 11
    Int64 = 10
    UInt32 = 9
    SqlInt32 = 8
    Int32 = 7
    UInt16 = 6
    SqlInt16 = 5
    Int16 = 4
    Byte = 3
    SqlByte = 2
    SByte = 1
    Error = 0
    SqlBoolean = -1
    Boolean = -2
    SqlGuid = -3
    SqlString = -4
    String = -5
    SqlXml = -6
    SqlChars = -7
    Char = -8
    SqlBytes = -9
    SqlBinary = -10

# System.Data.DataRowAction
class DataRowAction(IntFlag):
    Nothing = 0
    Delete = 1
    Change = 2
    Rollback = 4
    Commit = 8
    Add = 16
    ChangeOriginal = 32
    ChangeCurrentAndOriginal = 64

# System.Data.DataRowState
class DataRowState(IntFlag):
    Detached = 1
    Unchanged = 2
    Added = 4
    Deleted = 8
    Modified = 16

# System.Data.DataRowVersion
class DataRowVersion(IntFlag):
    Original = 256
    Current = 512
    Proposed = 1024
    Default = 1536

# System.Data.DataSetDateTime
class DataSetDateTime(IntFlag):
    Local = 1
    Unspecified = 2
    UnspecifiedLocal = 3
    Utc = 4

# System.Data.DataViewRowState
class DataViewRowState(IntFlag):
    NONE = 0
    Unchanged = 2
    Added = 4
    Deleted = 8
    ModifiedCurrent = 16
    ModifiedOriginal = 32
    OriginalRows = 42
    CurrentRows = 22

# System.Data.FunctionId
class FunctionId(IntFlag):
    none = -1
    Ascii = 0
    Char = 1
    Charindex = 2
    Difference = 3
    Len = 4
    Lower = 5
    LTrim = 6
    Patindex = 7
    Replicate = 8
    Reverse = 9
    Right = 10
    RTrim = 11
    Soundex = 12
    Space = 13
    Str = 14
    Stuff = 15
    Substring = 16
    Upper = 17
    IsNull = 18
    Iif = 19
    Convert = 20
    cInt = 21
    cBool = 22
    cDate = 23
    cDbl = 24
    cStr = 25
    Abs = 26
    Acos = 27
    In = 28
    Trim = 29
    Sum = 30
    Avg = 31
    Min = 32
    Max = 33
    Count = 34
    StDev = 35
    Var = 37
    DateTimeOffset = 38

# System.Data.MappingType
class MappingType(IntFlag):
    Element = 1
    Attribute = 2
    SimpleContent = 3
    Hidden = 4

# System.Data.MissingSchemaAction
class MissingSchemaAction(IntFlag):
    Add = 1
    Ignore = 2
    Error = 3
    AddWithKey = 4

# System.Data.Nodes
class Nodes(IntFlag):
    Noop = 0
    Unop = 1
    UnopSpec = 2
    Binop = 3
    BinopSpec = 4
    Zop = 5
    Call = 6
    Const = 7
    Name = 8
    Paren = 9
    Conv = 10

# System.Data.RBTree
class RBTree(IntFlag):
    red = 0
    black = 1

# System.Data.RBTreeError
class RBTreeError(IntFlag):
    InvalidPageSize = 1
    PagePositionInSlotInUse = 3
    NoFreeSlots = 4
    InvalidStateinInsert = 5
    InvalidNextSizeInDelete = 7
    InvalidStateinDelete = 8
    InvalidNodeSizeinDelete = 9
    InvalidStateinEndDelete = 10
    CannotRotateInvalidsuccessorNodeinDelete = 11
    IndexOutOFRangeinGetNodeByIndex = 13
    RBDeleteFixup = 14
    UnsupportedAccessMethod1 = 15
    UnsupportedAccessMethod2 = 16
    UnsupportedAccessMethodInNonNillRootSubtree = 17
    AttachedNodeWithZerorbTreeNodeId = 18
    CompareNodeInDataRowTree = 19
    CompareSateliteTreeNodeInDataRowTree = 20
    NestedSatelliteTreeEnumerator = 21

# System.Data.Rule
class Rule(IntFlag):
    NONE = 0
    Cascade = 1
    SetNull = 2
    SetDefault = 3

# System.Data.SchemaFormat
class SchemaFormat(IntFlag):
    Public = 1
    Remoting = 2
    WebService = 3
    RemotingSkipSchema = 4
    WebServiceSkipSchema = 5

# System.Data.SchemaSerializationMode
class SchemaSerializationMode(IntFlag):
    IncludeSchema = 1
    ExcludeSchema = 2

# System.Data.SerializationFormat
class SerializationFormat(IntFlag):
    Xml = 0
    Binary = 1

# System.Data.Tokens
class Tokens(IntFlag):
    NONE = 0
    Name = 1
    Numeric = 2
    Decimal = 3
    Float = 4
    BinaryConst = 5
    StringConst = 6
    Date = 7
    ListSeparator = 8
    LeftParen = 9
    RightParen = 10
    ZeroOp = 11
    UnaryOp = 12
    BinaryOp = 13
    Child = 14
    Parent = 15
    Dot = 16
    Unknown = 17
    EOS = 18

# System.Data.TreeAccessMethod
class TreeAccessMethod(IntFlag):
    KEY_SEARCH_AND_INDEX = 1
    INDEX_ONLY = 2

# System.Data.ValueType
class ValueType(IntFlag):
    Unknown = -1
    Null = 0
    Bool = 1
    Numeric = 2
    Str = 3
    Float = 4
    Decimal = 5
    Object = 6
    Date = 7

# System.Data.XmlReadMode
class XmlReadMode(IntFlag):
    Auto = 0
    ReadSchema = 1
    IgnoreSchema = 2
    InferSchema = 3
    DiffGram = 4
    Fragment = 5
    InferTypedSchema = 6

# System.Data.XmlWriteMode
class XmlWriteMode(IntFlag):
    WriteSchema = 0
    IgnoreSchema = 1
    DiffGram = 2

