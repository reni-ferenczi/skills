# XmlNode

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 322 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/XmlNode.h` | C++ | 379 |
| `src/model/XmlNode.cc` | C++ | 355 |

## Overview

[[[PROSE overview unit=model/XmlNode tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::XmlNode`](#gplatesmodelxmlnode) | class | [`GPlatesUtils::ReferenceCount<XmlNode>`](../utils/ReferenceCount.md) | — | 2 | XmlNode is the base class for a hierarchy used to store an uninterpreted XML tree in memory. |
| [`GPlatesModel::XmlTextNode`](#gplatesmodelxmltextnode) | class | [`XmlNode`](XmlNode.md) | — | 0 | — |
| [`GPlatesModel::XmlElementNode`](#gplatesmodelxmlelementnode) | class | [`XmlNode`](XmlNode.md) | — | 0 | Holds information associated with a node in an XML DOM-like tree. |
| [`GPlatesModel::XmlNodeVisitor`](#gplatesmodelxmlnodevisitor) | class | — | — | 4 | — |

## Members

### `GPlatesModel::XmlNode`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<XmlNode, GPlatesUtils::NullIntrusivePointerHandler>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const XmlNode, GPlatesUtils::NullIntrusivePointerHandler>` | public | — |
| `~XmlNode()` | destructor | `None` | public | — |
| `create( QXmlStreamReader &reader)` | method | `non_null_ptr_type` | public | This is a factory method for XmlNodes. |
| `write_to( QXmlStreamWriter &writer)` | method | `void` | public | — |
| `accept_visitor( XmlNodeVisitor &visitor)` | method | `void` | public | — |
| `line_number()` | method | `qint64` | public | — |
| `column_number()` | method | `qint64` | public | — |
| `XmlNode( const qint64 &line_num, const qint64 &col_num)` | constructor | `None` | protected | — |
| `d_line_num` | field | `qint64` | private | — |
| `d_col_num` | field | `qint64` | private | — |
| `operator=` | field | `XmlNode` | private | — |

### `GPlatesModel::XmlTextNode`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<XmlTextNode, GPlatesUtils::NullIntrusivePointerHandler>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const XmlTextNode, GPlatesUtils::NullIntrusivePointerHandler>` | public | — |
| `~XmlTextNode()` | destructor | `None` | public | — |
| `create( QXmlStreamReader &reader)` | method | `non_null_ptr_type` | public | — |
| `write_to( QXmlStreamWriter &writer)` | method | `void` | public | — |
| `accept_visitor( XmlNodeVisitor &visitor)` | method | `void` | public | — |
| `d_text` | field | `QString` | private | — |
| `XmlTextNode( const qint64 &line_num, const qint64 &col_num, const QString &text)` | constructor | `None` | private | — |
| `operator=` | field | `XmlTextNode` | private | — |

### `GPlatesModel::XmlElementNode`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<XmlElementNode, GPlatesUtils::NullIntrusivePointerHandler>` | public | — |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const XmlElementNode, GPlatesUtils::NullIntrusivePointerHandler>` | public | — |
| `AttributeCollection` | typedef | `std::map<XmlAttributeName, XmlAttributeValue>` | public | Convenience typedefs for dealing with this node's attributes. |
| `Attribute` | typedef | `AttributeCollection::value_type` | public | — |
| `attribute_iterator` | typedef | `AttributeCollection::iterator` | public | — |
| `attribute_const_iterator` | typedef | `AttributeCollection::const_iterator` | public | — |
| `ChildCollection` | typedef | `std::list<XmlNode::non_null_ptr_type>` | public | Convenience typedefs for dealing with this node's children. |
| `child_iterator` | typedef | `ChildCollection::iterator` | public | — |
| `child_const_iterator` | typedef | `ChildCollection::const_iterator` | public | — |
| `named_child_const_iterator` | typedef | `std::pair<child_const_iterator, boost::optional<non_null_ptr_type> >` | public | — |
| `AliasToNamespaceMap` | typedef | `std::map<QString, QString>` | public | — |
| `get_attribute_by_name( const XmlAttributeName &name)` | method | `attribute_const_iterator` | public | — |
| `attributes_begin()` | method | `attribute_const_iterator` | public | — |
| `attributes_end()` | method | `attribute_const_iterator` | public | — |
| `number_of_attributes()` | method | `size_t` | public | Warning: O(n). |
| `attributes_empty()` | method | `bool` | public | — |
| `get_child_by_name( const XmlElementName &name)` | method | `boost::optional<non_null_ptr_type>` | public | — |
| `get_next_child_by_name( const XmlElementName &name, const child_const_iterator &begin)` | method | `named_child_const_iterator` | public | — |
| `children_begin()` | method | `child_const_iterator` | public | — |
| `children_end()` | method | `child_const_iterator` | public | — |
| `number_of_children()` | method | `size_t` | public | Warning: O(n). |
| `children_empty()` | method | `bool` | public | — |
| `get_namespace_from_alias( const QString &alias)` | method | `boost::optional<QString>` | public | — |
| `~XmlElementNode()` | destructor | `None` | public | — |
| `create( QXmlStreamReader &reader, const boost::shared_ptr<AliasToNamespaceMap> &parent_alias_map)` | method | `non_null_ptr_type` | public | — |
| `create( const XmlTextNode::non_null_ptr_type &text, const XmlElementName &element_name)` | method | `non_null_ptr_type` | public | — |
| `write_to( QXmlStreamWriter &writer)` | method | `void` | public | — |
| `accept_visitor( XmlNodeVisitor &visitor)` | method | `void` | public | — |
| `operator==( const XmlElementNode &other)` | operator | `bool` | public | — |
| `d_name` | field | `XmlElementName` | private | — |
| `d_attributes` | field | `AttributeCollection` | private | — |
| `d_children` | field | `ChildCollection` | private | — |
| `d_alias_map` | field | `boost::shared_ptr<AliasToNamespaceMap>` | private | — |
| `XmlElementNode( const qint64 &line_num, const qint64 &col_num, const XmlElementName &name)` | constructor | `None` | private | — |
| `operator=` | field | `XmlElementNode` | private | — |
| `load_attributes( const QXmlStreamAttributes &attributes)` | method | `void` | private | — |

### `GPlatesModel::XmlNodeVisitor`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `~XmlNodeVisitor()` | destructor | `None` | public | — |
| `visit_text_node( const XmlTextNode::non_null_ptr_type &text)` | method | `void` | public | — |
| `visit_element_node( const XmlElementNode::non_null_ptr_type &elem)` | method | `void` | public | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `get_qualified_xml_name( const QString &namespace_uri, const QString &namespace_prefix, const QString &local_name)` | function | `QualifiedXmlNameType` | Creates an QualifiedXmlName from a namespace URI, namespace alias (prefix) and local name. |
| `convert_qxmlstreamattribute_to_attribute( const QXmlStreamAttribute &attribute)` | function | `GPlatesModel::XmlElementNode::Attribute` | — |
| `convert_attribute_to_qxmlstreamattribute( const GPlatesModel::XmlElementNode::Attribute &attribute)` | function | `QXmlStreamAttribute` | — |
| `operator==( const XmlElementNode &other)` | operator | `bool` | — |
| `GPLATES_MODEL_XMLNODE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/XmlNode tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 233 |
| [model/Gpgim](Gpgim.md) | model | 171 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 130 |
| [model/XmlNodeUtils](XmlNodeUtils.md) | model | 43 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 35 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 21 |
| [file-io/GpmlReaderUtils](../file-io/GpmlReaderUtils.md) | file-io | 18 |
| [model/Metadata](Metadata.md) | model | 18 |
| [file-io/GpmlReader](../file-io/GpmlReader.md) | file-io | 13 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 13 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 11 |
| [file-io/GpmlReaderException](../file-io/GpmlReaderException.md) | file-io | 7 |
| [file-io/GpmlFeatureReaderInterface](../file-io/GpmlFeatureReaderInterface.md) | file-io | 5 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 5 |
| [property-values/UninterpretedPropertyValue](../property-values/UninterpretedPropertyValue.md) | property-values | 5 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 4 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 2 |
| [feature-visitors/ToQvariantConverter](../feature-visitors/ToQvariantConverter.md) | feature-visitors | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/XmlNode.h
python scripts/gpq.py def GPlatesModel::XmlElementNode --body
python scripts/gpq.py uses XmlElementNode --kind class
python scripts/gpq.py hier XmlElementNode
```
