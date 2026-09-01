# XMLParser

[Book TOC](../../../TOC.md) · [file-io](../../../components/file-io.md) · cluster Community 884 · tier 3 · **deprecated**

| Source file | Kind | Lines |
|---|---|---|
| `src/file-io/deprecated/XMLParser.h` | C++ | 201 |
| `src/file-io/deprecated/XMLParser.cc` | C++ | 262 |

## Overview

A DOM-like wrapper around the expat XML parser library. `XMLParser::Parse()` reads an XML document from an input stream and builds a tree of `Element` nodes, where each `Element` holds a name, text content, attributes (as name/value pairs), and links to parent and child elements. The implementation uses expat callbacks to incrementally construct the tree as the parser encounters start tags, end tags, and character data.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`Element`](#element) | typedef | — | — | 0 | — |
| [`GPlatesFileIO::XMLParser`](#gplatesfileioxmlparser) | class | — | — | 0 | XMLParser is a simple DOM-like wrapper around the eXpat XML parser \[http://expat.sourceforge.net\]. |
| [`GPlatesFileIO::XMLParser::Element`](#gplatesfileioxmlparserelement) | class | — | — | 0 | The main node in the document tree. |

## Members

### `Element`

*None.*

### `GPlatesFileIO::XMLParser`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Element` | class | `None` | public | — |
| `Parse(std::istream& is)` | method | `Element` | public | Convert the given istream into an XML document tree. |
| `XMLParser()` | constructor | `None` | private | — |

### `GPlatesFileIO::XMLParser::Element`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `Attribute_type` | typedef | `std::pair< std::string, std::string >` | public | A name/value pair. |
| `ElementList_type` | typedef | `std::list< const Element* >` | public | A list of Elements; used when returning those elements that match a given Element name query. |
| `ElementMap_type` | typedef | `std::map< std::string, ElementList_type >` | public | Maps Element names to a list of the corresponding Element pointers. |
| `AttributeMap_type` | typedef | `std::map< std::string, Attribute_type >` | public | Maps Attribute\_type names to the corresponding Attribute\_types. |
| `Element(const std::string& name, unsigned int line_num)` | method | `None` | public | Create an Element in the XML document tree that has the given name, and which begins on the given line\_num. |
| `~Element()` | destructor | `None` | public | — |
| `GetName()` | method | `std::string` | public | — |
| `GetLineNumber()` | method | `unsigned int` | public | — |
| `GetContent()` | method | `std::string` | public | — |
| `GetAttribute(const std::string& name)` | method | `std::pair< Attribute_type, bool >` | public | Get the Attribute that has the given name. |
| `InsertAttribute(const Attribute_type& attr)` | method | `bool` | public | Insert an Attribute into the map of Attributes. true if the operation was successful, or false if an attribute with the same name was already present. |
| `GetParent()` | method | `Element` | public | — |
| `SetParent(Element* parent)` | method | `void` | public | — |
| `GetChildren(const std::string& name)` | method | `ElementList_type` | public | Get a list of child Elements of this Element whose names are name. |
| `InsertChild(const Element* element)` | method | `void` | public | — |
| `_name` | field | `std::string` | private | — |
| `_attributes` | field | `AttributeMap_type` | private | — |
| `_content` | field | `std::string` | private | — |
| `_parent` | field | `Element` | private | — |
| `_children` | field | `ElementMap_type` | private | — |
| `_line_num` | field | `unsigned int` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `cmp_space(char c1, char c2)` | function | `bool` | Returns true when both of the parameters are space characters. |
| `CompressWhitespace(std::string& str)` | function | `void` | Replace contiguous blocks of whitespace with a single space character. |
| `parser` | variable | `XML_Parser` | — |
| `StartElementHandler(void* userdata, const XML_Char* name, const XML_Char** attrs)` | function | `void` | Called for start tags, such as \\\<datagroup\> or \<meta ... attrs is an array of XML\_Char\* strings, arranged in name/value pairs. |
| `EndElementHandler(void* userdata, const XML_Char* name)` | function | `void` | Called for an end tag, such as \\\</datagroup\> or ... /\>. |
| `CharacterDataHandler(void* userdata, const XML_Char* str, int len)` | function | `void` | Called for character data within an element. |
| `SetCallbacks(Element** root)` | function | `void` | Set the callbacks for the parser. |
| `_GPLATES_FILEIO_XMLPARSER_H_` | macro | `None` | — |

## Notes

The caller is responsible for deleting the returned `Element` tree; the destructor recursively cleans up all children. Contiguous blocks of whitespace in element content are compressed to a single space. `Parse()` throws `FileFormatException` on parse errors, including malformed XML or stream failures. The parser uses a stack-based approach with callbacks; a stack mismatch (mismatched tags) terminates with an error message to stderr.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/deprecated/GPlatesReader](GPlatesReader.md) | file-io | 23 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/file-io/deprecated/XMLParser.h
python scripts/gpq.py def GPlatesFileIO::XMLParser::Element --body
python scripts/gpq.py uses XMLParser::Element --kind class
python scripts/gpq.py hier XMLParser::Element
```
