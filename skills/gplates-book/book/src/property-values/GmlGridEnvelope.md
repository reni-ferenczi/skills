# GmlGridEnvelope

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1152 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GmlGridEnvelope.h` | C++ | 202 |
| `src/property-values/GmlGridEnvelope.cc` | C++ | 85 |

## Overview

`GmlGridEnvelope` implements a property value for "gml:GridEnvelope", representing a bounding box in the GML standard format. It stores two coordinate lists—`d_low` and `d_high`—as vectors of integers, allowing each to represent arbitrary dimensions. The class follows the standard property-value factory pattern: instances must be created through the static `create()` method and held in intrusive pointers, ensuring heap allocation and shared ownership. Like other property values in this system, it uses the visitor pattern for traversing feature structures.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GmlGridEnvelope`](#gplatespropertyvaluesgmlgridenvelope) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gml:GridEnvelope". |

## Members

### `GPlatesPropertyValues::GmlGridEnvelope`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GmlGridEnvelope>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GmlGridEnvelope\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GmlGridEnvelope>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GmlGridEnvelope\>. |
| `~GmlGridEnvelope()` | destructor | `None` | public | — |
| `integer_list_type` | typedef | `std::vector<int>` | public | — |
| `create( const integer_list_type &low_, const integer_list_type &high_)` | method | `non_null_ptr_type` | public | Create a GmlGridEnvelope instance from low\_ and high\_ positions. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `set_low_and_high( const integer_list_type &low_, const integer_list_type &high_)` | method | `void` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GmlGridEnvelope( const integer_list_type &low_, const integer_list_type &high_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GmlGridEnvelope( const GmlGridEnvelope &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_low` | field | `integer_list_type` | private | — |
| `d_high` | field | `integer_list_type` | private | — |
| `operator=` | field | `GmlGridEnvelope` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GMLGRIDENVELOPE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [property-values/GmlRectifiedGrid](GmlRectifiedGrid.md) | property-values | 6 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 3 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 1 |
| [file-io/GpmlStructuralTypeReaderUtils](../file-io/GpmlStructuralTypeReaderUtils.md) | file-io | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GmlGridEnvelope.h
python scripts/gpq.py def GPlatesPropertyValues::GmlGridEnvelope --body
python scripts/gpq.py uses GmlGridEnvelope --kind class
python scripts/gpq.py hier GmlGridEnvelope
```
