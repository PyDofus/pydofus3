from enum import IntFlag

# System.Xml.Schema.AttributeMatchState
class AttributeMatchState(IntFlag):
    AttributeFound = 0
    AnyIdAttributeFound = 1
    UndeclaredElementAndAttribute = 2
    UndeclaredAttribute = 3
    AnyAttributeLax = 4
    AnyAttributeSkip = 5
    ProhibitedAnyAttribute = 6
    ProhibitedAttribute = 7
    AttributeNameMismatch = 8
    ValidateAttributeInvalidCall = 9

# System.Xml.Schema.CompiledIdentityConstraint
class CompiledIdentityConstraint(IntFlag):
    Unique = 0
    Key = 1
    Keyref = 2

# System.Xml.Schema.Compositor
class Compositor(IntFlag):
    Root = 0
    Include = 1
    Import = 2
    Redefine = 3

# System.Xml.Schema.FacetType
class FacetType(IntFlag):
    NONE = 0
    Length = 1
    MinLength = 2
    MaxLength = 3
    Pattern = 4
    Whitespace = 5
    Enumeration = 6
    MinExclusive = 7
    MinInclusive = 8
    MaxExclusive = 9
    MaxInclusive = 10
    TotalDigits = 11
    FractionDigits = 12

# System.Xml.Schema.NamespaceList
class NamespaceList(IntFlag):
    Any = 0
    Other = 1
    Set = 2

# System.Xml.Schema.RestrictionFlags
class RestrictionFlags(IntFlag):
    Length = 1
    MinLength = 2
    MaxLength = 4
    Pattern = 8
    Enumeration = 16
    WhiteSpace = 32
    MaxInclusive = 64
    MaxExclusive = 128
    MinInclusive = 256
    MinExclusive = 512
    TotalDigits = 1024
    FractionDigits = 2048

# System.Xml.Schema.SchemaAttDef
class SchemaAttDef(IntFlag):
    NONE = 0
    XmlSpace = 1
    XmlLang = 2

# System.Xml.Schema.SchemaCollectionPreprocessor
class SchemaCollectionPreprocessor(IntFlag):
    Root = 0
    Include = 1
    Import = 2

# System.Xml.Schema.SchemaDeclBase
class SchemaDeclBase(IntFlag):
    Default = 0
    Required = 1
    Implied = 2
    Fixed = 3
    RequiredFixed = 4

# System.Xml.Schema.SchemaNames
class SchemaNames(IntFlag):
    Empty = 0
    SchemaName = 1
    SchemaType = 2
    SchemaMaxOccurs = 3
    SchemaMinOccurs = 4
    SchemaInfinite = 5
    SchemaModel = 6
    SchemaOpen = 7
    SchemaClosed = 8
    SchemaContent = 9
    SchemaMixed = 10
    SchemaEmpty = 11
    SchemaElementOnly = 12
    SchemaTextOnly = 13
    SchemaOrder = 14
    SchemaSeq = 15
    SchemaOne = 16
    SchemaMany = 17
    SchemaRequired = 18
    SchemaYes = 19
    SchemaNo = 20
    SchemaString = 21
    SchemaId = 22
    SchemaIdref = 23
    SchemaIdrefs = 24
    SchemaEntity = 25
    SchemaEntities = 26
    SchemaNmtoken = 27
    SchemaNmtokens = 28
    SchemaEnumeration = 29
    SchemaDefault = 30
    XdrRoot = 31
    XdrElementType = 32
    XdrElement = 33
    XdrGroup = 34
    XdrAttributeType = 35
    XdrAttribute = 36
    XdrDatatype = 37
    XdrDescription = 38
    XdrExtends = 39
    SchemaXdrRootAlias = 40
    SchemaDtType = 41
    SchemaDtValues = 42
    SchemaDtMaxLength = 43
    SchemaDtMinLength = 44
    SchemaDtMax = 45
    SchemaDtMin = 46
    SchemaDtMinExclusive = 47
    SchemaDtMaxExclusive = 48
    SchemaTargetNamespace = 49
    SchemaVersion = 50
    SchemaFinalDefault = 51
    SchemaBlockDefault = 52
    SchemaFixed = 53
    SchemaAbstract = 54
    SchemaBlock = 55
    SchemaSubstitutionGroup = 56
    SchemaFinal = 57
    SchemaNillable = 58
    SchemaRef = 59
    SchemaBase = 60
    SchemaDerivedBy = 61
    SchemaNamespace = 62
    SchemaProcessContents = 63
    SchemaRefer = 64
    SchemaPublic = 65
    SchemaSystem = 66
    SchemaSchemaLocation = 67
    SchemaValue = 68
    SchemaSource = 69
    SchemaAttributeFormDefault = 70
    SchemaElementFormDefault = 71
    SchemaUse = 72
    SchemaForm = 73
    XsdSchema = 74
    XsdAnnotation = 75
    XsdInclude = 76
    XsdImport = 77
    XsdElement = 78
    XsdAttribute = 79
    xsdAttributeGroup = 80
    XsdAnyAttribute = 81
    XsdGroup = 82
    XsdAll = 83
    XsdChoice = 84
    XsdSequence = 85
    XsdAny = 86
    XsdNotation = 87
    XsdSimpleType = 88
    XsdComplexType = 89
    XsdUnique = 90
    XsdKey = 91
    XsdKeyref = 92
    XsdSelector = 93
    XsdField = 94
    XsdMinExclusive = 95
    XsdMinInclusive = 96
    XsdMaxExclusive = 97
    XsdMaxInclusive = 98
    XsdTotalDigits = 99
    XsdFractionDigits = 100
    XsdLength = 101
    XsdMinLength = 102
    XsdMaxLength = 103
    XsdEnumeration = 104
    XsdPattern = 105
    XsdDocumentation = 106
    XsdAppInfo = 107
    XsdComplexContent = 108
    XsdComplexContentExtension = 109
    XsdComplexContentRestriction = 110
    XsdSimpleContent = 111
    XsdSimpleContentExtension = 112
    XsdSimpleContentRestriction = 113
    XsdSimpleTypeList = 114
    XsdSimpleTypeRestriction = 115
    XsdSimpleTypeUnion = 116
    XsdWhitespace = 117
    XsdRedefine = 118
    SchemaItemType = 119
    SchemaMemberTypes = 120
    SchemaXPath = 121
    XmlLang = 122

# System.Xml.Schema.SchemaType
class SchemaType(IntFlag):
    NONE = 0
    DTD = 1
    XDR = 2
    XSD = 3

# System.Xml.Schema.ValidatorState
class ValidatorState(IntFlag):
    NONE = 0
    Start = 1
    TopLevelAttribute = 2
    TopLevelTextOrWS = 3
    Element = 4
    Attribute = 5
    EndOfAttributes = 6
    Text = 7
    Whitespace = 8
    EndElement = 9
    SkipToEndElement = 10
    Finish = 11

# System.Xml.Schema.XmlSchemaContentProcessing
class XmlSchemaContentProcessing(IntFlag):
    NONE = 0
    Skip = 1
    Lax = 2
    Strict = 3

# System.Xml.Schema.XmlSchemaContentType
class XmlSchemaContentType(IntFlag):
    TextOnly = 0
    Empty = 1
    ElementOnly = 2
    Mixed = 3

# System.Xml.Schema.XmlSchemaDatatypeVariety
class XmlSchemaDatatypeVariety(IntFlag):
    Atomic = 0
    List = 1
    Union = 2

# System.Xml.Schema.XmlSchemaDerivationMethod
class XmlSchemaDerivationMethod(IntFlag):
    Empty = 0
    Substitution = 1
    Extension = 2
    Restriction = 4
    List = 8
    Union = 16
    All = 255
    NONE = 256

# System.Xml.Schema.XmlSchemaForm
class XmlSchemaForm(IntFlag):
    NONE = 0
    Qualified = 1
    Unqualified = 2

# System.Xml.Schema.XmlSchemaInference
class XmlSchemaInference(IntFlag):
    Restricted = 0
    Relaxed = 1

# System.Xml.Schema.XmlSchemaObjectTable
class XmlSchemaObjectTable(IntFlag):
    Keys = 0
    Values = 1
    DictionaryEntry = 2

# System.Xml.Schema.XmlSchemaParticle
class XmlSchemaParticle(IntFlag):
    NONE = 0
    Min = 1
    Max = 2

# System.Xml.Schema.XmlSchemaUse
class XmlSchemaUse(IntFlag):
    NONE = 0
    Optional = 1
    Prohibited = 2
    Required = 3

# System.Xml.Schema.XmlSchemaValidationFlags
class XmlSchemaValidationFlags(IntFlag):
    NONE = 0
    ProcessInlineSchema = 1
    ProcessSchemaLocation = 2
    ReportValidationWarnings = 4
    ProcessIdentityConstraints = 8
    AllowXmlAttributes = 16

# System.Xml.Schema.XmlSchemaValidity
class XmlSchemaValidity(IntFlag):
    NotKnown = 0
    Valid = 1
    Invalid = 2

# System.Xml.Schema.XmlSchemaWhiteSpace
class XmlSchemaWhiteSpace(IntFlag):
    Preserve = 0
    Replace = 1
    Collapse = 2

# System.Xml.Schema.XmlSeverityType
class XmlSeverityType(IntFlag):
    Error = 0
    Warning = 1

# System.Xml.Schema.XmlTypeCode
class XmlTypeCode(IntFlag):
    NONE = 0
    Item = 1
    Node = 2
    Document = 3
    Element = 4
    Attribute = 5
    Namespace = 6
    ProcessingInstruction = 7
    Comment = 8
    Text = 9
    AnyAtomicType = 10
    UntypedAtomic = 11
    String = 12
    Boolean = 13
    Decimal = 14
    Float = 15
    Double = 16
    Duration = 17
    DateTime = 18
    Time = 19
    Date = 20
    GYearMonth = 21
    GYear = 22
    GMonthDay = 23
    GDay = 24
    GMonth = 25
    HexBinary = 26
    Base64Binary = 27
    AnyUri = 28
    QName = 29
    Notation = 30
    NormalizedString = 31
    Token = 32
    Language = 33
    NmToken = 34
    Name = 35
    NCName = 36
    Id = 37
    Idref = 38
    Entity = 39
    Integer = 40
    NonPositiveInteger = 41
    NegativeInteger = 42
    Long = 43
    Int = 44
    Short = 45
    Byte = 46
    NonNegativeInteger = 47
    UnsignedLong = 48
    UnsignedInt = 49
    UnsignedShort = 50
    UnsignedByte = 51
    PositiveInteger = 52
    YearMonthDuration = 53
    DayTimeDuration = 54

# System.Xml.Schema.XsdBuilder
class XsdBuilder(IntFlag):
    Root = 0
    Schema = 1
    Annotation = 2
    Include = 3
    Import = 4
    Element = 5
    Attribute = 6
    AttributeGroup = 7
    AttributeGroupRef = 8
    AnyAttribute = 9
    Group = 10
    GroupRef = 11
    All = 12
    Choice = 13
    Sequence = 14
    Any = 15
    Notation = 16
    SimpleType = 17
    ComplexType = 18
    ComplexContent = 19
    ComplexContentRestriction = 20
    ComplexContentExtension = 21
    SimpleContent = 22
    SimpleContentExtension = 23
    SimpleContentRestriction = 24
    SimpleTypeUnion = 25
    SimpleTypeList = 26
    SimpleTypeRestriction = 27
    Unique = 28
    Key = 29
    KeyRef = 30
    Selector = 31
    Field = 32
    MinExclusive = 33
    MinInclusive = 34
    MaxExclusive = 35
    MaxInclusive = 36
    TotalDigits = 37
    FractionDigits = 38
    Length = 39
    MinLength = 40
    MaxLength = 41
    Enumeration = 42
    Pattern = 43
    WhiteSpace = 44
    AppInfo = 45
    Documentation = 46
    Redefine = 47

# System.Xml.Schema.XsdDateTime
class XsdDateTime(IntFlag):
    DateTime = 0
    Time = 1
    Date = 2
    GYearMonth = 3
    GYear = 4
    GMonthDay = 5
    GDay = 6
    GMonth = 7
    XdrDateTime = 8

# System.Xml.Schema.XsdDateTime
class XsdDateTime(IntFlag):
    Unspecified = 0
    Zulu = 1
    LocalWestOfZulu = 2
    LocalEastOfZulu = 3

# System.Xml.Schema.XsdDateTimeFlags
class XsdDateTimeFlags(IntFlag):
    DateTime = 1
    Time = 2
    Date = 4
    GYearMonth = 8
    GYear = 16
    GMonthDay = 32
    GDay = 64
    GMonth = 128
    XdrDateTimeNoTz = 256
    XdrDateTime = 512
    XdrTimeNoTz = 1024
    AllXsd = 255

# System.Xml.Schema.XsdDuration
class XsdDuration(IntFlag):
    HasNone = 0
    HasYears = 1
    HasMonths = 2
    HasDays = 4
    HasHours = 8
    HasMinutes = 16
    HasSeconds = 32

# System.Xml.Schema.XsdDuration
class XsdDuration(IntFlag):
    Duration = 0
    YearMonthDuration = 1
    DayTimeDuration = 2

