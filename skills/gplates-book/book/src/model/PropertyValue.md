# PropertyValue

[Book TOC](../../TOC.md) · [model](../../components/model.md) · cluster Community 931 · tier 1

| Source file | Kind | Lines |
|---|---|---|
| `src/model/PropertyValue.h` | C++ | 296 |
| `src/model/PropertyValue.cc` | C++ | 56 |

## Overview

[[[PROSE overview unit=model/PropertyValue tier=1]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesModel::FeatureVisitor`](#gplatesmodelfeaturevisitor) | typedef | — | — | 0 | — |
| [`GPlatesModel::ConstFeatureVisitor`](#gplatesmodelconstfeaturevisitor) | typedef | — | — | 0 | — |
| [`GPlatesModel::PropertyValue`](#gplatesmodelpropertyvalue) | class | [`GPlatesUtils::ReferenceCount<PropertyValue>`](../utils/ReferenceCount.md)<br>[`GPlatesUtils::QtStreamable<PropertyValue>`](../utils/QtStreamable.md) | — | 46 | This class is the abstract base of all property values. |

## Members

### `GPlatesModel::FeatureVisitor`

*None.*

### `GPlatesModel::ConstFeatureVisitor`

*None.*

### `GPlatesModel::PropertyValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<PropertyValue, GPlatesUtils::NullIntrusivePointerHandler>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<PropertyValue, GPlatesUtils::NullIntrusivePointerHandler\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const PropertyValue, GPlatesUtils::NullIntrusivePointerHandler>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const PropertyValue, GPlatesUtils::NullIntrusivePointerHandler\>. |
| `PropertyValue()` | constructor | `None` | public | Construct a PropertyValue instance. |
| `PropertyValue( const PropertyValue &other)` | constructor | `None` | public | Construct a PropertyValue instance which is a copy of other. |
| `~PropertyValue()` | destructor | `None` | public | — |
| `deep_clone_as_prop_val()` | method | `non_null_ptr_type` | public | Create a duplicate of this PropertyValue instance, including a recursive copy of any property values this instance might contain. |
| `get_structural_type()` | method | `GPlatesPropertyValues::StructuralType` | public | Returns the structural type associated with the type of the derived property value class. |
| `accept_visitor( ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | Prints the contents of this PropertyValue to the stream os. |
| `operator==( const PropertyValue &other)` | operator | `bool` | public | — |
| `update_instance_id()` | method | `void` | protected | Give this PropertyValue instance a new instance id. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | Reimplement in derived classes where there are instance variables that can be modified by client code without using a set\_\*() function. |
| `operator=` | field | `PropertyValue` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |
| `instance_id_type` | class | `None` | private | Just in case we happen to run into a compiler without 64-bit integers. |
| `d_instance_id` | field | `instance_id_type` | private | Assists in speeding up operator==. |
| `s_next_instance_id` | field | `instance_id_type` | private | — |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `s_next_instance_id` | variable | `GPlatesModel::PropertyValue::instance_id_type` | — |
| `operator==( const PropertyValue &other)` | operator | `bool` | — |
| `GPLATES_MODEL_PROPERTYVALUE_H` | macro | `None` | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL` | macro_function | `virtual \ const GPlatesModel::PropertyValue::non_null_ptr_type \ deep_clone_as_prop_val() const \ { \ return deep_clone(); \ }` | This macro is used to define the virtual function 'deep\_clone\_as\_prop\_val' inside a class which derives from PropertyValue. |
| `operator<<` | variable | `std::ostream` | operator\<\< for PropertyValue. |

## Notes

[[[PROSE notes unit=model/PropertyValue tier=1]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [model/ModelUtils](ModelUtils.md) | model | 50 |
| [file-io/GpmlPropertyStructuralTypeReader](../file-io/GpmlPropertyStructuralTypeReader.md) | file-io | 39 |
| [file-io/GpmlPropertyReader](../file-io/GpmlPropertyReader.md) | file-io | 25 |
| [feature-visitors/PropertyValueFinder](../feature-visitors/PropertyValueFinder.md) | feature-visitors | 24 |
| [property-values/GpmlAge](../property-values/GpmlAge.md) | property-values | 23 |
| [property-values/GpmlArray](../property-values/GpmlArray.md) | property-values | 23 |
| [property-values/GmlRectifiedGrid](../property-values/GmlRectifiedGrid.md) | property-values | 22 |
| [property-values/GpmlConstantValue](../property-values/GpmlConstantValue.md) | property-values | 22 |
| [property-values/GmlFile](../property-values/GmlFile.md) | property-values | 21 |
| [property-values/GmlTimePeriod](../property-values/GmlTimePeriod.md) | property-values | 20 |
| [app-logic/GeometryUtils](../app-logic/GeometryUtils.md) | app-logic | 19 |
| [model/TopLevelPropertyInline](TopLevelPropertyInline.md) | model | 18 |
| [property-values/GpmlOldPlatesHeader](../property-values/GpmlOldPlatesHeader.md) | property-values | 18 |
| [qt-widgets/ImportRasterDialog](../qt-widgets/ImportRasterDialog.md) | qt-widgets | 18 |
| [property-values/GpmlHotSpotTrailMark](../property-values/GpmlHotSpotTrailMark.md) | property-values | 17 |
| [property-values/GpmlKeyValueDictionaryElement](../property-values/GpmlKeyValueDictionaryElement.md) | property-values | 17 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 16 |
| [property-values/GpmlTopologicalNetwork](../property-values/GpmlTopologicalNetwork.md) | property-values | 16 |
| [feature-visitors/FromQvariantConverter](../feature-visitors/FromQvariantConverter.md) | feature-visitors | 13 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 13 |

*... and 119 more units.*

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/model/PropertyValue.h
python scripts/gpq.py def GPlatesModel::PropertyValue --body
python scripts/gpq.py uses PropertyValue --kind class
python scripts/gpq.py hier PropertyValue
```
