from enum import IntFlag

# System.Xml.XPath.XPathNamespaceScope
class XPathNamespaceScope(IntFlag):
    All = 0
    ExcludeXml = 1
    Local = 2

# System.Xml.XPath.XPathNodeType
class XPathNodeType(IntFlag):
    Root = 0
    Element = 1
    Attribute = 2
    Namespace = 3
    Text = 4
    SignificantWhitespace = 5
    Whitespace = 6
    ProcessingInstruction = 7
    Comment = 8
    All = 9

# System.Xml.XPath.XPathResultType
class XPathResultType(IntFlag):
    Number = 0
    String = 1
    Boolean = 2
    NodeSet = 3
    Navigator = 1
    Any = 5
    Error = 6

