from enum import IntFlag

# System.Xml.AttributeProperties
class AttributeProperties(IntFlag):
    DEFAULT = 0
    URI = 1
    BOOLEAN = 2
    NAME = 4

# System.Xml.BinXmlToken
class BinXmlToken(IntFlag):
    Error = 0
    NotImpl = -2
    EOF = -1
    XmlDecl = 254
    Encoding = 253
    DocType = 252
    System = 251
    Public = 250
    Subset = 249
    Element = 248
    EndElem = 247
    Attr = 246
    EndAttrs = 245
    PI = 244
    Comment = 243
    CData = 242
    EndCData = 241
    Name = 240
    QName = 239
    XmlText = 237
    Nest = 236
    EndNest = 235
    Extn = 234
    NmFlush = 233
    SQL_BIT = 6
    SQL_TINYINT = 7
    SQL_SMALLINT = 1
    SQL_INT = 2
    SQL_BIGINT = 8
    SQL_REAL = 3
    SQL_FLOAT = 4
    SQL_MONEY = 5
    SQL_SMALLMONEY = 20
    SQL_DATETIME = 18
    SQL_SMALLDATETIME = 19
    SQL_DECIMAL = 10
    SQL_NUMERIC = 11
    SQL_UUID = 9
    SQL_VARBINARY = 15
    SQL_BINARY = 12
    SQL_IMAGE = 23
    SQL_CHAR = 13
    SQL_VARCHAR = 16
    SQL_TEXT = 22
    SQL_NVARCHAR = 17
    SQL_NCHAR = 14
    SQL_NTEXT = 24
    SQL_UDT = 27
    XSD_KATMAI_DATE = 127
    XSD_KATMAI_DATETIME = 126
    XSD_KATMAI_TIME = 125
    XSD_KATMAI_DATEOFFSET = 124
    XSD_KATMAI_DATETIMEOFFSET = 123
    XSD_KATMAI_TIMEOFFSET = 122
    XSD_BOOLEAN = 134
    XSD_TIME = 129
    XSD_DATETIME = 130
    XSD_DATE = 131
    XSD_BINHEX = 132
    XSD_BASE64 = 133
    XSD_DECIMAL = 135
    XSD_BYTE = 136
    XSD_UNSIGNEDSHORT = 137
    XSD_UNSIGNEDINT = 138
    XSD_UNSIGNEDLONG = 139
    XSD_QNAME = 140

# System.Xml.ConformanceLevel
class ConformanceLevel(IntFlag):
    Auto = 0
    Fragment = 1
    Document = 2

# System.Xml.DtdParser
class DtdParser(IntFlag):
    CDATA = 0
    ID = 1
    IDREF = 2
    IDREFS = 3
    ENTITY = 4
    ENTITIES = 5
    NMTOKEN = 6
    NMTOKENS = 7
    NOTATION = 8
    NONE = 9
    PERef = 10
    AttlistDecl = 11
    ElementDecl = 12
    EntityDecl = 13
    NotationDecl = 14
    Comment = 15
    PI = 16
    CondSectionStart = 17
    CondSectionEnd = 18
    Eof = 19
    REQUIRED = 20
    IMPLIED = 21
    FIXED = 22
    QName = 23
    Name = 24
    Nmtoken = 25
    Quote = 26
    LeftParen = 27
    RightParen = 28
    GreaterThan = 29
    Or = 30
    LeftBracket = 31
    RightBracket = 32
    PUBLIC = 33
    SYSTEM = 34
    Literal = 35
    DOCTYPE = 36
    NData = 37
    Percent = 38
    Star = 39
    QMark = 40
    Plus = 41
    PCDATA = 42
    Comma = 43
    ANY = 44
    EMPTY = 45
    IGNORE = 46
    INCLUDE = 47

# System.Xml.DtdParser
class DtdParser(IntFlag):
    SubsetContent = 0
    Name = 1
    QName = 2
    Nmtoken = 3
    Doctype1 = 4
    Doctype2 = 5
    Element1 = 6
    Element2 = 7
    Element3 = 8
    Element4 = 9
    Element5 = 10
    Element6 = 11
    Element7 = 12
    Attlist1 = 13
    Attlist2 = 14
    Attlist3 = 15
    Attlist4 = 16
    Attlist5 = 17
    Attlist6 = 18
    Attlist7 = 19
    Entity1 = 20
    Entity2 = 21
    Entity3 = 22
    Notation1 = 23
    CondSection1 = 24
    CondSection2 = 25
    CondSection3 = 26
    Literal = 27
    SystemId = 28
    PublicId1 = 29
    PublicId2 = 30
    ClosingTag = 31
    ParamEntitySpace = 32
    NONE = 33

# System.Xml.DtdParser
class DtdParser(IntFlag):
    AttributeValue = 0
    EntityReplText = 1
    SystemOrPublicID = 2

# System.Xml.DtdProcessing
class DtdProcessing(IntFlag):
    Prohibit = 0
    Ignore = 1
    Parse = 2

# System.Xml.ElementProperties
class ElementProperties(IntFlag):
    DEFAULT = 0
    URI_PARENT = 1
    BOOL_PARENT = 2
    NAME_PARENT = 4
    EMPTY = 8
    NO_ENTITIES = 16
    HEAD = 32
    BLOCK_WS = 64
    HAS_NS = 128

# System.Xml.EntityHandling
class EntityHandling(IntFlag):
    ExpandEntities = 1
    ExpandCharEntities = 2

# System.Xml.ExceptionType
class ExceptionType(IntFlag):
    ArgumentException = 0
    XmlException = 1

# System.Xml.Formatting
class Formatting(IntFlag):
    NONE = 0
    Indented = 1

# System.Xml.NamespaceHandling
class NamespaceHandling(IntFlag):
    Default = 0
    OmitDuplicates = 1

# System.Xml.NewLineHandling
class NewLineHandling(IntFlag):
    Replace = 0
    Entitize = 1
    NONE = 2

# System.Xml.ReadContentAsBinaryHelper
class ReadContentAsBinaryHelper(IntFlag):
    NONE = 0
    InReadContent = 1
    InReadElementContent = 2

# System.Xml.ReadState
class ReadState(IntFlag):
    Initial = 0
    Interactive = 1
    Error = 2
    EndOfFile = 3
    Closed = 4

# System.Xml.TriState
class TriState(IntFlag):
    Unknown = -1
    FALSE = 0
    TRUE = 1

# System.Xml.ValidationType
class ValidationType(IntFlag):
    NONE = 0
    Auto = 1
    DTD = 2
    XDR = 3
    Schema = 4

# System.Xml.WhitespaceHandling
class WhitespaceHandling(IntFlag):
    All = 0
    Significant = 1
    NONE = 2

# System.Xml.WriteState
class WriteState(IntFlag):
    Start = 0
    Prolog = 1
    Element = 2
    Attribute = 3
    Content = 4
    Closed = 5
    Error = 6

# System.Xml.XmlDateTimeSerializationMode
class XmlDateTimeSerializationMode(IntFlag):
    Local = 0
    Utc = 1
    Unspecified = 2
    RoundtripKind = 3

# System.Xml.XmlEventCache
class XmlEventCache(IntFlag):
    Unknown = 0
    DocType = 1
    StartElem = 2
    StartAttr = 3
    EndAttr = 4
    CData = 5
    Comment = 6
    PI = 7
    Whitespace = 8
    String = 9
    Raw = 10
    EntRef = 11
    CharEnt = 12
    SurrCharEnt = 13
    Base64 = 14
    BinHex = 15
    XmlDecl1 = 16
    XmlDecl2 = 17
    StartContent = 18
    EndElem = 19
    FullEndElem = 20
    Nmsp = 21
    EndBase64 = 22
    Close = 23
    Flush = 24
    Dispose = 25

# System.Xml.XmlNamespaceScope
class XmlNamespaceScope(IntFlag):
    All = 0
    ExcludeXml = 1
    Local = 2

# System.Xml.XmlNodeChangedAction
class XmlNodeChangedAction(IntFlag):
    Insert = 0
    Remove = 1
    Change = 2

# System.Xml.XmlNodeOrder
class XmlNodeOrder(IntFlag):
    Before = 0
    After = 1
    Same = 2
    Unknown = 3

# System.Xml.XmlNodeType
class XmlNodeType(IntFlag):
    NONE = 0
    Element = 1
    Attribute = 2
    Text = 3
    CDATA = 4
    EntityReference = 5
    Entity = 6
    ProcessingInstruction = 7
    Comment = 8
    Document = 9
    DocumentType = 10
    DocumentFragment = 11
    Notation = 12
    Whitespace = 13
    SignificantWhitespace = 14
    EndElement = 15
    EndEntity = 16
    XmlDeclaration = 17

# System.Xml.XmlOutputMethod
class XmlOutputMethod(IntFlag):
    Xml = 0
    Html = 1
    Text = 2
    AutoDetect = 3

# System.Xml.XmlSpace
class XmlSpace(IntFlag):
    NONE = 0
    Default = 1
    Preserve = 2

# System.Xml.XmlSqlBinaryReader
class XmlSqlBinaryReader(IntFlag):
    Doc = 0
    XmlText = 1
    Attr = 2
    AttrVal = 3
    AttrValPseudoValue = 4
    Init = 5
    Error = 6
    EOF = 7
    Closed = 8

# System.Xml.XmlStandalone
class XmlStandalone(IntFlag):
    Omit = 0
    Yes = 1
    No = 2

# System.Xml.XmlTextReaderImpl
class XmlTextReaderImpl(IntFlag):
    ElementContent = 0
    NoData = 1
    OpenUrl = 2
    SwitchToInteractive = 3
    SwitchToInteractiveXmlDecl = 4
    DocumentContent = 5
    MoveToElementContent = 6
    PopElementContext = 7
    PopEmptyElementContext = 8
    ResetAttributesRootLevel = 9
    Error = 10
    Eof = 11
    ReaderClosed = 12
    EntityReference = 13
    InIncrementalRead = 14
    FragmentAttribute = 15
    ReportEndEntity = 16
    AfterResolveEntityInContent = 17
    AfterResolveEmptyEntityInContent = 18
    XmlDeclarationFragment = 19
    GoToEof = 20
    PartialTextValue = 21
    InReadAttributeValue = 22
    InReadValueChunk = 23
    InReadContentAsBinary = 24
    InReadElementContentAsBinary = 25

# System.Xml.XmlTextReaderImpl
class XmlTextReaderImpl(IntFlag):
    Full = 0
    SkipNode = 1
    SkipContent = 2

# System.Xml.XmlTextReaderImpl
class XmlTextReaderImpl(IntFlag):
    CharacterDec = 0
    CharacterHex = 1
    CharacterNamed = 2
    Expanded = 3
    Skipped = 4
    FakeExpanded = 5
    Unexpanded = 6
    ExpandedInAttribute = 7

# System.Xml.XmlTextReaderImpl
class XmlTextReaderImpl(IntFlag):
    All = 0
    OnlyGeneral = 1
    OnlyCharacter = 2

# System.Xml.XmlTextReaderImpl
class XmlTextReaderImpl(IntFlag):
    Text = 0
    StartTag = 1
    PI = 2
    CDATA = 3
    Comment = 4
    Attributes = 5
    AttributeValue = 6
    ReadData = 7
    EndElement = 8
    End = 9
    ReadValueChunk_OnCachedValue = 10
    ReadValueChunk_OnPartialValue = 11
    ReadContentAsBinary_OnCachedValue = 12
    ReadContentAsBinary_OnPartialValue = 13
    ReadContentAsBinary_End = 14

# System.Xml.XmlTextReaderImpl
class XmlTextReaderImpl(IntFlag):
    UriString = 0
    Stream = 1
    TextReader = 2
    Invalid = 3

# System.Xml.XmlTextReaderImpl
class XmlTextReaderImpl(IntFlag):
    CheckEndTag = 0
    ReadData = 1
    Done = 2

# System.Xml.XmlTextReaderImpl
class XmlTextReaderImpl(IntFlag):
    ParseText = 0
    Entity = 1
    Surrogate = 2
    ReadData = 3
    NoValue = 4
    PartialValue = 5

# System.Xml.XmlTextWriter
class XmlTextWriter(IntFlag):
    Uninitialized = 0
    NotDeclaredButInScope = 1
    DeclaredButNotWrittenOut = 2
    DeclaredAndWrittenOut = 3

# System.Xml.XmlTextWriter
class XmlTextWriter(IntFlag):
    NONE = 0
    XmlSpace = 1
    XmlLang = 2
    XmlNs = 3

# System.Xml.XmlTextWriter
class XmlTextWriter(IntFlag):
    Start = 0
    Prolog = 1
    PostDTD = 2
    Element = 3
    Attribute = 4
    Content = 5
    AttrOnly = 6
    Epilog = 7
    Error = 8
    Closed = 9

# System.Xml.XmlTextWriter
class XmlTextWriter(IntFlag):
    PI = 0
    Doctype = 1
    Comment = 2
    CData = 3
    StartElement = 4
    EndElement = 5
    LongEndElement = 6
    StartAttribute = 7
    EndAttribute = 8
    Content = 9
    Base64 = 10
    RawData = 11
    Whitespace = 12
    Empty = 13

# System.Xml.XmlTokenizedType
class XmlTokenizedType(IntFlag):
    CDATA = 0
    ID = 1
    IDREF = 2
    IDREFS = 3
    ENTITY = 4
    ENTITIES = 5
    NMTOKEN = 6
    NMTOKENS = 7
    NOTATION = 8
    ENUMERATION = 9
    QName = 10
    NCName = 11
    NONE = 12

# System.Xml.XmlValidatingReaderImpl
class XmlValidatingReaderImpl(IntFlag):
    Read = 0
    Init = 1
    ParseDtdFromContext = 2
    ResolveEntityInternally = 3
    InReadBinaryContent = 4
    ReaderClosed = 5
    Error = 6
    NONE = 7

# System.Xml.XmlWellFormedWriter
class XmlWellFormedWriter(IntFlag):
    Start = 0
    TopLevel = 1
    Document = 2
    Element = 3
    Content = 4
    B64Content = 5
    B64Attribute = 6
    AfterRootEle = 7
    Attribute = 8
    SpecialAttr = 9
    EndDocument = 10
    RootLevelAttr = 11
    RootLevelSpecAttr = 12
    RootLevelB64Attr = 13
    AfterRootLevelAttr = 14
    Closed = 15
    Error = 16
    StartContent = 101
    StartContentEle = 102
    StartContentB64 = 103
    StartDoc = 104
    StartDocEle = 106
    EndAttrSEle = 107
    EndAttrEEle = 108
    EndAttrSCont = 109
    EndAttrSAttr = 111
    PostB64Cont = 112
    PostB64Attr = 113
    PostB64RootAttr = 114
    StartFragEle = 115
    StartFragCont = 116
    StartFragB64 = 117
    StartRootLevelAttr = 118

# System.Xml.XmlWellFormedWriter
class XmlWellFormedWriter(IntFlag):
    StartDocument = 0
    EndDocument = 1
    PI = 2
    Comment = 3
    Dtd = 4
    StartElement = 5
    EndElement = 6
    StartAttribute = 7
    EndAttribute = 8
    Text = 9
    CData = 10
    AtomicValue = 11
    Base64 = 12
    RawData = 13
    Whitespace = 14

# System.Xml.XmlWellFormedWriter
class XmlWellFormedWriter(IntFlag):
    Written = 0
    NeedToWrite = 1
    Implied = 2
    Special = 3

# System.Xml.XmlWellFormedWriter
class XmlWellFormedWriter(IntFlag):
    No = 0
    DefaultXmlns = 1
    PrefixedXmlns = 2
    XmlSpace = 3
    XmlLang = 4

# System.Xml.XmlWellFormedWriter
class XmlWellFormedWriter(IntFlag):
    EntityRef = 0
    CharEntity = 1
    SurrogateCharEntity = 2
    Whitespace = 3
    String = 4
    StringChars = 5
    Raw = 6
    RawChars = 7
    ValueString = 8

# System.Xml.XsdCachingReader
class XsdCachingReader(IntFlag):
    NONE = 0
    Init = 1
    Record = 2
    Replay = 3
    ReaderClosed = 4
    Error = 5

# System.Xml.XsdValidatingReader
class XsdValidatingReader(IntFlag):
    NONE = 0
    Init = 1
    Read = 2
    OnDefaultAttribute = -1
    OnReadAttributeValue = -2
    OnAttribute = 3
    ClearAttributes = 4
    ParseInlineSchema = 5
    ReadAhead = 6
    OnReadBinaryContent = 7
    ReaderClosed = 8
    EOF = 9
    Error = 10

