# TopLevelPropertyInline

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 129 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/TopLevelPropertyInline.h` | C++ | 287 |
| `src/model/TopLevelPropertyInline.cc` | C++ | 195 |

## Overview

[[[PROSE overview unit=model/TopLevelPropertyInline tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::TopLevelPropertyInline`](#gplatesmodeltoplevelpropertyinline) | class | [`TopLevelProperty`](TopLevelProperty.md) | — | 0 | This class represents a top-level property of a feature, which is containing its property-value inline. |

## Members

### `GPlatesModel::TopLevelPropertyInline`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopLevelPropertyInline>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<TopLevelPropertyInline\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopLevelPropertyInline>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const TopLevelPropertyInline\>. |
| `container_type` | typedef | `std::vector<PropertyValue::non_null_ptr_type>` | public | The type of our container of PropertyValue pointers. |
| `iterator` | typedef | `container_type::iterator` | public | The type of an iterator that iterates over the PropertyValue instances contained in this TopLevelPropertyInline. |
| `make_const_ptr_fn_type` | typedef | `boost::function< PropertyValue::non_null_ptr_to_const_type ( const PropertyValue::non_null_ptr_type &) >` | private | The type of a function that converts a pointer to non-const PropertyValue to a pointer to const. |
| `const_iterator` | typedef | `boost::transform_iterator<make_const_ptr_fn_type, container_type::const_iterator>` | public | The type of an iterator that const-iterates over the PropertyValue instances contained in this TopLevelPropertyInline. |
| `~TopLevelPropertyInline()` | destructor | `None` | public | — |
| `create( const PropertyName &property_name_, const container_type &values_, const xml_attributes_type &xml_attributes_ = xml_attributes_type())` | method | `non_null_ptr_type` | public | — |
| `create( const PropertyName &property_name_, const PropertyValueIterator &values_begin_, const PropertyValueIterator &values_end_, const xml_attributes_type &xml_attributes_ = xml_attributes_type())` | method | `non_null_ptr_type` | public | — |
| `create( const PropertyName &property_name_, PropertyValue::non_null_ptr_type value_, const xml_attributes_type &xml_attributes_ = xml_attributes_type())` | method | `non_null_ptr_type` | public | — |
| `create( const PropertyName &property_name_, PropertyValue::non_null_ptr_type value_, const GPlatesUtils::UnicodeString &attribute_name_string, const GPlatesUtils::UnicodeString &attribute_value_string)` | method | `non_null_ptr_type` | public | — |
| `create( const PropertyName &property_name_, PropertyValue::non_null_ptr_type value_, const AttributeIterator &attributes_begin, const AttributeIterator &attributes_end)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `TopLevelProperty::non_null_ptr_type` | public | — |
| `deep_clone()` | method | `TopLevelProperty::non_null_ptr_type` | public | — |
| `begin()` | method | `const_iterator` | public | — |
| `end()` | method | `const_iterator` | public | — |
| `size()` | method | `size_t` | public | — |
| `accept_visitor( ConstFeatureVisitor &visitor)` | method | `void` | public | — |
| `accept_visitor( FeatureVisitor &visitor)` | method | `void` | public | — |
| `print_to` | field | `std::ostream` | public | — |
| `operator==( const TopLevelProperty &other)` | operator | `bool` | public | — |
| `TopLevelPropertyInline( const PropertyName &property_name_, const container_type &values_, const xml_attributes_type &xml_attributes_)` | constructor | `None` | protected | — |
| `TopLevelPropertyInline( const PropertyName &property_name_, const PropertyValueIterator &values_begin_, const PropertyValueIterator &values_end_, const xml_attributes_type &xml_attributes_)` | constructor | `None` | protected | — |
| `TopLevelPropertyInline( const PropertyName &property_name_, PropertyValue::non_null_ptr_type value_, const xml_attributes_type &xml_attributes_)` | constructor | `None` | protected | — |
| `TopLevelPropertyInline( const TopLevelPropertyInline &other)` | constructor | `None` | protected | — |
| `d_values` | field | `container_type` | private | — |
| `operator=` | field | `TopLevelPropertyInline` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `DISABLE_MSVC_WARNING` | variable | `PUSH_MSVC_WARNINGS` | — |
| `operator==( const TopLevelProperty &other)` | operator | `bool` | — |
| `GPLATES_MODEL_TOPLEVELPROPERTYINLINE_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=model/TopLevelPropertyInline tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/ModelUtils](ModelUtils.md) | model | 19 |
| [file-io/OgrReader](../file-io/OgrReader.md) | file-io | 17 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 17 |
| [file-io/OgrUtils](../file-io/OgrUtils.md) | file-io | 16 |
| [file-io/GsmlPropertyHandlers](../file-io/GsmlPropertyHandlers.md) | file-io | 13 |
| [file-io/GmapReader](../file-io/GmapReader.md) | file-io | 11 |
| [qt-widgets/CreateVGPDialog](../qt-widgets/CreateVGPDialog.md) | qt-widgets | 10 |
| [feature-visitors/TotalReconstructionSequenceTimePeriodFinder](../feature-visitors/TotalReconstructionSequenceTimePeriodFinder.md) | feature-visitors | 9 |
| [model/FeatureVisitor](FeatureVisitor.md) | model | 9 |
| [file-io/GpmlFeatureReaderImpl](../file-io/GpmlFeatureReaderImpl.md) | file-io | 7 |
| [file-io/GpmlFormatMultiPointVectorFieldExport](../file-io/GpmlFormatMultiPointVectorFieldExport.md) | file-io | 7 |
| [file-io/OgrWriter](../file-io/OgrWriter.md) | file-io | 7 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 7 |
| [feature-visitors/FeatureClassifier](../feature-visitors/FeatureClassifier.md) | feature-visitors | 6 |
| [feature-visitors/KeyValueDictionaryFinder](../feature-visitors/KeyValueDictionaryFinder.md) | feature-visitors | 6 |
| [feature-visitors/TotalReconstructionSequencePlateIdFinder](../feature-visitors/TotalReconstructionSequencePlateIdFinder.md) | feature-visitors | 6 |
| [file-io/PlatesRotationFileProxy](../file-io/PlatesRotationFileProxy.md) | file-io | 6 |
| [qt-widgets/CreateSmallCircleFeatureDialog](../qt-widgets/CreateSmallCircleFeatureDialog.md) | qt-widgets | 6 |
| [qt-widgets/MetadataDialog](../qt-widgets/MetadataDialog.md) | qt-widgets | 6 |
| [entry-points/gplates_demo_no_gui_main](../entry-points/gplates_demo_no_gui_main.md) | entry-points | 5 |

*... and 45 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/TopLevelPropertyInline.h
python scripts/gpq.py def GPlatesModel::TopLevelPropertyInline --body
python scripts/gpq.py uses TopLevelPropertyInline --kind class
python scripts/gpq.py hier TopLevelPropertyInline
```
