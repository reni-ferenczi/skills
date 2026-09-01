# OldVersionPropertyValue

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1214 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/OldVersionPropertyValue.h` | C++ | 205 |
| `src/property-values/OldVersionPropertyValue.cc` | C++ | 37 |

## Overview

A property value for reading deprecated old-version property types from GPML files. It wraps an arbitrary value (via `boost::any`) along with a structural type identifier, allowing import code to deserialize obsolete property formats and then convert them to current property types. The value is immutable after creation; there are no setters, so instance-id revisioning is not needed.

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::OldVersionPropertyValue`](#gplatespropertyvaluesoldversionpropertyvalue) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements an old version PropertyValue. |

## Members

### `GPlatesPropertyValues::OldVersionPropertyValue`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<OldVersionPropertyValue>` | public | A convenience typedef for a shared pointer to a non-const OldVersionPropertyValue. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const OldVersionPropertyValue>` | public | A convenience typedef for a shared pointer to a const OldVersionPropertyValue. |
| `value_type` | typedef | `boost::any` | public | Typedef for the user-defined arbitrary property 'value'. |
| `~OldVersionPropertyValue()` | destructor | `None` | public | — |
| `create( const StructuralType &structural_type, const value_type &value_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `OldVersionPropertyValue( const StructuralType &structural_type, const value_type &value_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `OldVersionPropertyValue( const OldVersionPropertyValue &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_structural_type` | field | `StructuralType` | private | The structural type of the old property value type. |
| `d_value` | field | `value_type` | private | The arbitrary user-defined property 'value'. |
| `operator=` | field | `OldVersionPropertyValue` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTY_VALUES_OLDVERSIONPROPERTYVALUE_H` | macro | `None` | — |

## Notes

*None.*

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/OldVersionPropertyValue.h
python scripts/gpq.py def GPlatesPropertyValues::OldVersionPropertyValue --body
python scripts/gpq.py uses OldVersionPropertyValue --kind class
python scripts/gpq.py hier OldVersionPropertyValue
```
