# GpmlArray

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1002 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlArray.h` | C++ | 206 |
| `src/property-values/GpmlArray.cc` | C++ | 92 |

## Overview

`GpmlArray` represents a GPML array property value—a heterogeneous collection of `PropertyValue` objects held in a vector. Each array instance stores both the member elements and a `StructuralType` describing the type of elements it contains. The class is used where feature properties need to hold multiple values of potentially different kinds. It follows the standard property-value factory pattern with heap-only allocation via intrusive pointers and visitor-pattern traversal. Unlike shallow-cloned property values, `GpmlArray` requires deep cloning to recursively copy its member elements.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlArray`](#gplatespropertyvaluesgpmlarray) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlArray`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlArray>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlArray\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlArray>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlArray\>. |
| `~GpmlArray()` | destructor | `None` | public | — |
| `create( const std::vector<GPlatesModel::PropertyValue::non_null_ptr_type> &members, const StructuralType &value_type_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `is_empty()` | method | `bool` | public | — |
| `num_elements()` | method | `std::vector<GPlatesModel::PropertyValue::non_null_ptr_type>::size_type` | public | — |
| `print_to` | field | `std::ostream` | public | — |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | public | — |
| `GpmlArray( const std::vector<GPlatesModel::PropertyValue::non_null_ptr_type> &members_, const StructuralType &value_type_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlArray( const GpmlArray &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_members` | field | `std::vector<GPlatesModel::PropertyValue::non_null_ptr_type>` | private | — |
| `d_type` | field | `StructuralType` | private | — |
| `operator=` | field | `GpmlArray` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLARRAY_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [app-logic/FlowlineUtils](../app-logic/FlowlineUtils.md) | app-logic | 2 |
| [app-logic/MotionPathUtils](../app-logic/MotionPathUtils.md) | app-logic | 2 |
| [qt-widgets/EditTimeSequenceWidget](../qt-widgets/EditTimeSequenceWidget.md) | qt-widgets | 2 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/QueryFeaturePropertiesWidgetPopulator](../feature-visitors/QueryFeaturePropertiesWidgetPopulator.md) | feature-visitors | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [qt-widgets/EditWidgetChooser](../qt-widgets/EditWidgetChooser.md) | qt-widgets | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlArray.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlArray --body
python scripts/gpq.py uses GpmlArray --kind class
python scripts/gpq.py hier GpmlArray
```
