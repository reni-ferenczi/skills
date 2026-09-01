# TopLevelProperty

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 1298 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/model/TopLevelProperty.h` | C++ | 253 |
| `src/model/TopLevelProperty.cc` | C++ | 38 |

## Overview

[[[PROSE overview unit=model/TopLevelProperty tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureVisitor`](#gplatesmodelfeaturevisitor) | typedef | — | — | 0 | — |
| [`GPlatesModel::ConstFeatureVisitor`](#gplatesmodelconstfeaturevisitor) | typedef | — | — | 0 | — |
| [`GPlatesModel::TopLevelProperty`](#gplatesmodeltoplevelproperty) | class | [`GPlatesUtils::ReferenceCount<TopLevelProperty>`](../utils/ReferenceCount.md)<br>[`GPlatesUtils::QtStreamable<TopLevelProperty>`](../utils/QtStreamable.md) | — | 1 | This abstract base class (ABC) represents the top-level property of a feature. |

## Members

### `GPlatesModel::FeatureVisitor`

*None.*

### `GPlatesModel::ConstFeatureVisitor`

*None.*

### `GPlatesModel::TopLevelProperty`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<TopLevelProperty, GPlatesUtils::NullIntrusivePointerHandler>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<TopLevelProperty, GPlatesUtils::NullIntrusivePointerHandler\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const TopLevelProperty, GPlatesUtils::NullIntrusivePointerHandler>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const TopLevelProperty, GPlatesUtils::NullIntrusivePointerHandler\>. |
| `xml_attributes_type` | typedef | `std::map<XmlAttributeName, XmlAttributeValue>` | public | The type of the container of XML attributes. |
| `~TopLevelProperty()` | destructor | `None` | public | — |
| `TopLevelProperty( const PropertyName &property_name_, const xml_attributes_type &xml_attributes_)` | constructor | `None` | public | Construct a TopLevelProperty instance with the given property name. |
| `TopLevelProperty( const TopLevelProperty &other)` | constructor | `None` | public | Construct a TopLevelProperty instance which is a copy of other. |
| `clone()` | method | `non_null_ptr_type` | public | Create a duplicate of this TopLevelProperty instance. |
| `deep_clone()` | method | `non_null_ptr_type` | public | Create a duplicate of this TopLevelProperty instance, plus any property values which it might contain. |
| `set_xml_attributes( const xml_attributes_type &xml_attributes_)` | method | `void` | public | Set the XML attributes. |
| `accept_visitor( ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | Prints the contents of this TopLevelProperty to the stream os. |
| `operator==( const TopLevelProperty &other)` | operator | `bool` | public | — |
| `d_property_name` | field | `PropertyName` | private | — |
| `d_xml_attributes` | field | `xml_attributes_type` | private | — |
| `operator=` | field | `TopLevelProperty` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_MODEL_TOPLEVELPROPERTY_H` | macro | `None` | — |
| `operator<<` | variable | `std::ostream` | — |

## Notes

[[[PROSE notes unit=model/TopLevelProperty tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/TopLevelPropertyInline](TopLevelPropertyInline.md) | model | 23 |
| [data-mining/deprecated/LookupDataOperator](../data-mining/deprecated/LookupDataOperator.md) | data-mining | 11 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 10 |
| [file-io/GpmlFormatDeformationExport](../file-io/GpmlFormatDeformationExport.md) | file-io | 7 |
| [app-logic/PartitionFeatureUtils](../app-logic/PartitionFeatureUtils.md) | app-logic | 6 |
| [data-mining/deprecated/DataOperator](../data-mining/deprecated/DataOperator.md) | data-mining | 5 |
| [data-mining/deprecated/MinDataOperator](../data-mining/deprecated/MinDataOperator.md) | data-mining | 5 |
| [qt-widgets/CreateFeatureAddOrEditPropertyDialog](../qt-widgets/CreateFeatureAddOrEditPropertyDialog.md) | qt-widgets | 5 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 5 |
| [qt-widgets/CreateFeaturePropertiesPage](../qt-widgets/CreateFeaturePropertiesPage.md) | qt-widgets | 4 |
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 3 |
| [file-io/GpmlFormatReconstructedScalarCoverageExport](../file-io/GpmlFormatReconstructedScalarCoverageExport.md) | file-io | 3 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 3 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 2 |
| [qt-widgets/EditWidgetGroupBox](../qt-widgets/EditWidgetGroupBox.md) | qt-widgets | 2 |
| [view-operations/FocusedFeatureGeometryManipulator](../view-operations/FocusedFeatureGeometryManipulator.md) | view-operations | 2 |
| [view-operations/SplitFeatureUndoCommand](../view-operations/SplitFeatureUndoCommand.md) | view-operations | 2 |
| [data-mining/deprecated/DistanceDataOperator](../data-mining/deprecated/DistanceDataOperator.md) | data-mining | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [model/BasicHandle](BasicHandle.md) | model | 1 |

*... and 8 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/TopLevelProperty.h
python scripts/gpq.py def GPlatesModel::TopLevelProperty --body
python scripts/gpq.py uses TopLevelProperty --kind class
python scripts/gpq.py hier TopLevelProperty
```
