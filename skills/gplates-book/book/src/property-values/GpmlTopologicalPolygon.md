# GpmlTopologicalPolygon

[Book TOC](../../TOC.md) · [property-values](../../components/property-values.md) · cluster Community 1004 · tier 2

| Source file | Kind | Lines |
|---|---|---|
| `src/property-values/GpmlTopologicalPolygon.h` | C++ | 219 |
| `src/property-values/GpmlTopologicalPolygon.cc` | C++ | 109 |

## Overview

[[[PROSE overview unit=property-values/GpmlTopologicalPolygon tier=2]]]
Replace this whole block, markers included, with 1-3 paragraphs: what this unit is, why it exists, and how it fits the surrounding design. Do not restate the tables below.
[[[/PROSE]]]

## Declared types

| Name | Kind | Bases | Template | Subclasses | Description |
|---|---|---|---|---|---|
| [`GPlatesPropertyValues::GpmlTopologicalPolygon`](#gplatespropertyvaluesgpmltopologicalpolygon) | class | [`GPlatesModel::PropertyValue`](../model/PropertyValue.md) | — | 0 | This class implements the PropertyValue which corresponds to "gpml:TopologicalPolygon". |

## Members

### `GPlatesPropertyValues::GpmlTopologicalPolygon`

| Member | Kind | Type | Access | Description |
|---|---|---|---|---|
| `non_null_ptr_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<GpmlTopologicalPolygon>` | public | A convenience typedef for a shared pointer to a non-const GpmlTopologicalPolygon. |
| `non_null_ptr_to_const_type` | typedef | `GPlatesUtils::non_null_intrusive_ptr<const GpmlTopologicalPolygon>` | public | A convenience typedef for a shared pointer to a const GpmlTopologicalPolygon. |
| `sections_seq_type` | typedef | `std::vector<GpmlTopologicalSection::non_null_ptr_type>` | public | Typedef for a sequence of boundary sections. |
| `sections_const_iterator` | typedef | `sections_seq_type::const_iterator` | public | Typedef for a const iterator over the topological sections. |
| `~GpmlTopologicalPolygon()` | destructor | `None` | public | — |
| `create( const TopologicalSectionsIterator &exterior_sections_begin_, const TopologicalSectionsIterator &exterior_sections_end_)` | method | `non_null_ptr_type` | public | Create a GpmlTopologicalPolygon instance from the specified sequence of topological sections representing the exterior of the topological polygon. |
| `clone()` | method | `non_null_ptr_type` | public | — |
| `deep_clone()` | method | `non_null_ptr_type` | public | — |
| `DEFINE_FUNCTION_DEEP_CLONE_AS_PROP_VAL()` | method | `None` | public | — |
| `exterior_sections_begin()` | method | `sections_const_iterator` | public | Return the "begin" const iterator to iterate over the exterior topological sections. |
| `exterior_sections_end()` | method | `sections_const_iterator` | public | Return the "end" const iterator for iterating over the exterior topological sections. |
| `get_structural_type()` | method | `StructuralType` | public | Returns the structural type associated with this property value class. |
| `accept_visitor( GPlatesModel::ConstFeatureVisitor &visitor)` | method | `void` | public | Accept a ConstFeatureVisitor instance. |
| `accept_visitor( GPlatesModel::FeatureVisitor &visitor)` | method | `void` | public | Accept a FeatureVisitor instance. |
| `print_to` | field | `std::ostream` | public | — |
| `GpmlTopologicalPolygon( const TopologicalSectionsIterator &exterior_sections_begin_, const TopologicalSectionsIterator &exterior_sections_end_)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `GpmlTopologicalPolygon( const GpmlTopologicalPolygon &other)` | constructor | `None` | protected | This constructor should not be public, because we don't want to allow instantiation of this type on the stack. |
| `directly_modifiable_fields_equal( const PropertyValue &other)` | method | `bool` | protected | Need to compare all data members (recursively) since our boundary sections are \*non-const\* non\_null\_intrusive\_ptr and hence can be modified by clients. |
| `d_exterior_sections` | field | `sections_seq_type` | private | — |
| `operator=` | field | `GpmlTopologicalPolygon` | private | This operator should never be defined, because we don't want/need to allow copy-assignment: All copying should use the virtual copy-constructor 'clone' (which will in turn use the copy-constructor); all "assignment" should really only be ... |

## Free functions and macros

| Name | Kind | Type / body | Description |
|---|---|---|---|
| `section_eq( const GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type &p1, const GPlatesPropertyValues::GpmlTopologicalSection::non_null_ptr_type &p2)` | function | `bool` | — |
| `GPLATES_PROPERTYVALUES_GPMLTOPOLOGICALPOLYGON_H` | macro | `None` | — |

## Notes

[[[PROSE notes unit=property-values/GpmlTopologicalPolygon tier=2]]]
Replace this whole block, markers included, with invariants, ownership, threading or gotchas that are not visible in the tables. Write *None.* if there is nothing worth saying.
[[[/PROSE]]]

## Used by

| Unit | Component | References |
|---|---|---|
| [app-logic/TopologyInternalUtils](../app-logic/TopologyInternalUtils.md) | app-logic | 4 |
| [file-io/GpmlPropertyStructuralTypeReaderUtils](../file-io/GpmlPropertyStructuralTypeReaderUtils.md) | file-io | 4 |
| [app-logic/TopologyGeometryResolver](../app-logic/TopologyGeometryResolver.md) | app-logic | 3 |
| [feature-visitors/TopologySectionsFinder](../feature-visitors/TopologySectionsFinder.md) | feature-visitors | 3 |
| [file-io/GpmlOutputVisitor](../file-io/GpmlOutputVisitor.md) | file-io | 3 |
| [app-logic/TopologyNetworkResolver](../app-logic/TopologyNetworkResolver.md) | app-logic | 1 |
| [data-mining/GetValueFromPropertyVisitor](../data-mining/GetValueFromPropertyVisitor.md) | data-mining | 1 |
| [file-io/GpmlUpgradeReaderUtils](../file-io/GpmlUpgradeReaderUtils.md) | file-io | 1 |
| [file-io/PlatesLineFormatReader](../file-io/PlatesLineFormatReader.md) | file-io | 1 |
| [gui/TopologyTools](../gui/TopologyTools.md) | gui | 1 |
| [model/ModelUtils](../model/ModelUtils.md) | model | 1 |
| [qt-widgets/CreateFeatureDialog](../qt-widgets/CreateFeatureDialog.md) | qt-widgets | 1 |
| [utils/GetPropertyAsPythonObjVisitor](../utils/GetPropertyAsPythonObjVisitor.md) | utils | 1 |

## Related

*None.*

## Explore

Run these from the `gplates-code` skill directory:

```bash
python scripts/gpq.py file src/property-values/GpmlTopologicalPolygon.h
python scripts/gpq.py def GPlatesPropertyValues::GpmlTopologicalPolygon --body
python scripts/gpq.py uses GpmlTopologicalPolygon --kind class
python scripts/gpq.py hier GpmlTopologicalPolygon
```
