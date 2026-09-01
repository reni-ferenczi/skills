# XmlNodeUtils

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 529 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/XmlNodeUtils.h` | C++ | 387 |
| `src/model/XmlNodeUtils.cc` | C++ | 93 |

## Overview

`XmlNodeUtils` is a small toolkit of visitors and free functions built on top of the `XmlNodeVisitor`/`XmlNode` hierarchy (`XmlNode.h`), used by the GPML readers in `file-io` to pull structured values back out of a parsed XML element tree. `XmlElementNodeExtractionVisitor` narrows a generic `XmlNode` down to an `XmlElementNode`, optionally requiring it to have a specific `XmlElementName`; `NamedXmlElementNodeIterator` builds on that visitor to walk a forward-iterator range of sibling XML nodes and expose only the ones matching a given element name, which is how readers pick out repeated child elements (e.g. all `<gml:pos>` entries) without hand-rolling the filtering loop each time. `TextExtractionVisitor` concatenates the text of an element's text-node children and separately records whether it encountered any child *element* nodes, which the two `get_text`/`get_text_without_trimming` functions use to reject elements that mix text with sub-elements rather than silently returning partial text.

`get_qualified_xml_name<QualifiedXmlNameType>` builds on `get_text` to parse an element's text content as an `"alias:name"` pair, resolving the alias to a namespace via `XmlElementNode::get_namespace_from_alias` and constructing a `QualifiedXmlNameType` (for example `PropertyName` or `StructuralType`) from the result — this is the standard way GPML text content that names a type or property gets turned back into one of the qualified-name types used elsewhere in the model.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::XmlNodeUtils::XmlElementNodeExtractionVisitor`](#gplatesmodelxmlnodeutilsxmlelementnodeextractionvisitor) | class | [`XmlNodeVisitor`](XmlNode.md) | — | 0 | Determines if an XmlNode is an XmlElementNode. |
| [`GPlatesModel::XmlNodeUtils::NamedXmlElementNodeIterator`](#gplatesmodelxmlnodeutilsnamedxmlelementnodeiterator) | class | — | `<typename XmlNodeForwardIter>` | 0 | Convenience iterator wrapper over a sequence of XML element nodes with same element name. |
| [`GPlatesModel::XmlNodeUtils::TextExtractionVisitor`](#gplatesmodelxmlnodeutilstextextractionvisitor) | class | [`XmlNodeVisitor`](XmlNode.md)<br>`boost::noncopyable` | — | 0 | Extracts text from a visited XML text node. |

## Members

### `GPlatesModel::XmlNodeUtils::XmlElementNodeExtractionVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `XmlElementNodeExtractionVisitor()` | constructor | `None` | public | Constructor that does not match the XML element name. |
| `XmlElementNodeExtractionVisitor( const XmlElementName &xml_element_name)` | constructor | `None` | public | Constructor that matches the XML element name. |
| `get_xml_element_node( const XmlNode::non_null_ptr_type &xml_node)` | method | `boost::optional<XmlElementNode::non_null_ptr_type>` | public | Returns XML element node if xml\_node is a XmlElementNode and optionally matches element name passed into constructor, otherwise boost::none. |
| `visit_text_node( const XmlTextNode::non_null_ptr_type &text)` | method | `void` | private | — |
| `visit_element_node( const XmlElementNode::non_null_ptr_type &xml_element_node)` | method | `void` | private | — |
| `d_xml_element_name` | field | `boost::optional<XmlElementName>` | private | If the element name is specified then it must be matched to the visited XML element. |
| `d_xml_element_node` | field | `boost::optional<XmlElementNode::non_null_ptr_type>` | private | — |

### `GPlatesModel::XmlNodeUtils::NamedXmlElementNodeIterator`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `NamedXmlElementNodeIterator( const XmlNodeForwardIter &xml_elements_begin, const XmlNodeForwardIter &xml_elements_end, const XmlElementName &element_name)` | constructor | `None` | public | Constructor begins iteration at the first XML element node found with the element name, if any. |
| `first()` | method | `void` | public | Begins iteration at the first XML element node found with the element name, if any. |
| `next()` | method | `void` | public | Note: finished should be false when this is called. |
| `has_next()` | method | `bool` | public | Note: finished should be false when this is called. |
| `finished()` | method | `bool` | public | Returns true if finished iterating. |
| `get_xml_element()` | method | `XmlElementNode::non_null_ptr_type` | public | Note: finished should be false, if this is to be called. |
| `get_xml_node_iterator()` | method | `XmlNodeForwardIter` | public | Returns the current XML node iterator. |
| `NamedXmlElementIterator` | struct | `None` | private | An iterator over XML element node's with matching names. |
| `d_xml_element_node_visitor` | field | `XmlNodeUtils::XmlElementNodeExtractionVisitor` | private | — |
| `d_xml_nodes_begin` | field | `XmlNodeForwardIter` | private | — |
| `d_xml_nodes_end` | field | `XmlNodeForwardIter` | private | — |
| `d_named_xml_element_iterator` | field | `NamedXmlElementIterator` | private | The iterator to the current XML element node with matching name, if any. |
| `d_next_named_xml_element_iterator` | field | `boost::optional<NamedXmlElementIterator>` | private | Only used when has\_next is called - in which case it temporarily caches result of next iterator. |
| `find_xml_element_node_with_matching_name( NamedXmlElementIterator &name_xml_element_iterator)` | method | `void` | private | Finds the XML element node with matching name starting at the specified iterator. |

### `GPlatesModel::XmlNodeUtils::TextExtractionVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `TextExtractionVisitor()` | constructor | `None` | public | — |
| `visit_element_node( const XmlElementNode::non_null_ptr_type &elem)` | method | `void` | public | — |
| `visit_text_node( const XmlTextNode::non_null_ptr_type &text)` | method | `void` | public | — |
| `encountered_subelement()` | method | `bool` | public | — |
| `d_text` | field | `QString` | private | — |
| `d_encountered_subelement` | field | `bool` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_XMLNODEUTILS_H` | macro | `None` | — |
| `get_text_without_trimming( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem)` | function | `boost::optional<QString>` | Returns the text string contents of the specified XML element node. |
| `get_text( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem)` | function | `boost::optional<QString>` | Returns the text string contents of the specified XML element node. |
| `get_qualified_xml_name( const GPlatesModel::XmlElementNode::non_null_ptr_type &elem)` | function | `boost::optional<QualifiedXmlNameType>` | Reads the text string contents of the specified XML element node as a fully qualified name. |

## Notes

`NamedXmlElementNodeIterator` only stores the `XmlNodeForwardIter`s it was given plus a cached lookahead; it does not own the underlying node sequence, so the caller-supplied range must outlive the iterator. `has_next()` is `const` but mutates the cached lookahead iterator (`d_next_named_xml_element_iterator`) so the result can be reused by a following `next()` without repeating the search — calling `has_next()` more than once in a row does not advance further.

`get_text`/`get_text_without_trimming` return `boost::none`, not an empty string, whenever the element has any child *element* nodes, so a caller cannot distinguish "empty text" from "mixed content" without checking the return value.

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 21 |
| [model/Gpgim](Gpgim.md) | model | 19 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 18 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 7 |
| [model/XmlNode](XmlNode.md) | model | 6 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/XmlNodeUtils.h
python scripts/gpq.py def GPlatesModel::XmlNodeUtils::NamedXmlElementNodeIterator --body
python scripts/gpq.py uses NamedXmlElementNodeIterator --kind class
python scripts/gpq.py hier NamedXmlElementNodeIterator
```
