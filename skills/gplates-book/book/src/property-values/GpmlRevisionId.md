# GpmlRevisionId

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 204 · tier 3

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlRevisionId.h` | C++ | 180 |
| `src/property-values/GpmlRevisionId.cc` | C++ | 39 |

## Overview

[[[PROSE overview unit=property-values/GpmlRevisionId tier=3]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlRevisionId`](#gplatespropertyvaluesgpmlrevisionid) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | — |

## Members

### `GPlatesPropertyValues::GpmlRevisionId`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlRevisionId>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<GpmlRevisionId\>. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlRevisionId>` | public | A convenience typedef for GPlatesUtils::non\_null\_intrusive\_ptr\<const GpmlRevisionId\>. |
| `~GpmlRevisionId()` | destructor | `None` | public | — |
| `create( const GPlatesModel::RevisionId &value_)` | method | `non_null_ptr_type` | public | — |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlRevisionId( const GPlatesModel::RevisionId &value_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlRevisionId( const GpmlRevisionId &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `d_value` | field | `GPlatesModel::RevisionId` | private | — |
| `operator=` | field | `GpmlRevisionId` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `GPLATES_PROPERTYVALUES_GPMLREVISIONID_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlRevisionId tier=3]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 3 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 1 |
| [file-io/GMTFormatHeader](../file-io/GMTFormatHeader.md) | file-io | 1 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlRevisionId.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlRevisionId --body
python scripts/gpq.py uses GpmlRevisionId --kind class
python scripts/gpq.py hier GpmlRevisionId
```
